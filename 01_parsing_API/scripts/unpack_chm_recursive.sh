#!/usr/bin/env bash
set -uo pipefail

INPUT_DIR="${1:-api}"
OUTPUT_DIR="${2:-extracted}"

if ! command -v extract_chmLib >/dev/null 2>&1; then
    echo "ERROR: extract_chmLib is not available in PATH." >&2
    echo "Install chmlib tools first. On Debian/Ubuntu this is usually: sudo apt install libchm-bin" >&2
    exit 127
fi

mkdir -p "$OUTPUT_DIR"

INPUT_DIR="$(cd "$INPUT_DIR" && pwd)"
OUTPUT_DIR="$(cd "$OUTPUT_DIR" && pwd)"

pass=1
total_processed=0
total_skipped=0
total_errors=0

while true; do
    echo "========================================"
    echo "PASS $pass"
    echo "INPUT:  $INPUT_DIR"
    echo "OUTPUT: $OUTPUT_DIR"
    echo "========================================"

    processed_this_pass=0
    skipped_this_pass=0
    errors_this_pass=0

    while IFS= read -r -d '' chm_file; do
        chm_dir="$(dirname "$chm_file")"
        chm_base="$(basename "$chm_file")"
        chm_name="${chm_base%.*}"

        if [[ "$chm_file" == "$INPUT_DIR"/* ]]; then
            rel_dir="${chm_dir#"$INPUT_DIR"}"
        elif [[ "$chm_file" == "$OUTPUT_DIR"/* ]]; then
            rel_dir="${chm_dir#"$OUTPUT_DIR"}"
        else
            rel_dir=""
        fi
        rel_dir="${rel_dir#/}"
        out_dir="$OUTPUT_DIR/$rel_dir/$chm_name"
        marker_file="$out_dir/.chm_extracted"

        echo
        echo "CHM : $chm_file"
        echo "OUT : $out_dir"

        # Skip only if this exact CHM was already unpacked by this script.
        if [ -f "$marker_file" ]; then
            echo "SKIP: marker exists"
            skipped_this_pass=$((skipped_this_pass + 1))
            continue
        fi

        mkdir -p "$out_dir"

        # extract_chmLib: extract_chmLib <chmfile> <dir>
        if extract_chmLib "$chm_file" "$out_dir"; then
            touch "$marker_file"
            echo "OK"
            processed_this_pass=$((processed_this_pass + 1))
        else
            echo "ERROR"
            errors_this_pass=$((errors_this_pass + 1))
        fi

    done < <(
        {
            find "$INPUT_DIR" -type f -iname "*.chm" -print0
            find "$OUTPUT_DIR" -type f -iname "*.chm" -print0
        } | sort -z
    )

    total_processed=$((total_processed + processed_this_pass))
    total_skipped=$((total_skipped + skipped_this_pass))
    total_errors=$((total_errors + errors_this_pass))

    echo
    echo "PASS $pass SUMMARY:"
    echo "processed: $processed_this_pass"
    echo "skipped:   $skipped_this_pass"
    echo "errors:    $errors_this_pass"

    # Stop when a pass does not discover any new CHM files.
    if [ "$processed_this_pass" -eq 0 ]; then
        break
    fi

    pass=$((pass + 1))
done

echo
echo "========================================"
echo "FINAL SUMMARY"
echo "processed: $total_processed"
echo "skipped:   $total_skipped"
echo "errors:    $total_errors"
echo "passes:    $pass"
echo "========================================"
