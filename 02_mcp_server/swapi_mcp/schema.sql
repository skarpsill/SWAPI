CREATE EXTENSION IF NOT EXISTS pg_trgm;

CREATE TABLE IF NOT EXISTS api_versions (
    id BIGSERIAL PRIMARY KEY,
    version TEXT NOT NULL UNIQUE,
    markdown_root TEXT NOT NULL,
    index_root TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS documents (
    version_id BIGINT NOT NULL REFERENCES api_versions(id) ON DELETE CASCADE,
    id TEXT NOT NULL,
    path TEXT NOT NULL,
    module TEXT NOT NULL DEFAULT '',
    kind TEXT NOT NULL DEFAULT '',
    title TEXT NOT NULL DEFAULT '',
    symbol TEXT NOT NULL DEFAULT '',
    interface TEXT NOT NULL DEFAULT '',
    member TEXT NOT NULL DEFAULT '',
    project TEXT NOT NULL DEFAULT '',
    headings JSONB NOT NULL DEFAULT '[]'::jsonb,
    signatures JSONB NOT NULL DEFAULT '{}'::jsonb,
    token_estimate INTEGER,
    words INTEGER,
    link_count INTEGER,
    markdown TEXT NOT NULL DEFAULT '',
    search_vector TSVECTOR GENERATED ALWAYS AS (
        to_tsvector(
            'english',
            coalesce(symbol, '') || ' ' ||
            coalesce(title, '') || ' ' ||
            coalesce(interface, '') || ' ' ||
            coalesce(member, '') || ' ' ||
            coalesce(path, '') || ' ' ||
            coalesce(markdown, '')
        )
    ) STORED,
    PRIMARY KEY (version_id, id)
);

CREATE TABLE IF NOT EXISTS symbols (
    version_id BIGINT NOT NULL REFERENCES api_versions(id) ON DELETE CASCADE,
    id TEXT NOT NULL,
    symbol TEXT NOT NULL DEFAULT '',
    kind TEXT NOT NULL DEFAULT '',
    module TEXT NOT NULL DEFAULT '',
    path TEXT NOT NULL DEFAULT '',
    title TEXT NOT NULL DEFAULT '',
    interface TEXT NOT NULL DEFAULT '',
    member TEXT NOT NULL DEFAULT '',
    project TEXT NOT NULL DEFAULT '',
    PRIMARY KEY (version_id, id)
);

CREATE TABLE IF NOT EXISTS interface_members (
    version_id BIGINT NOT NULL REFERENCES api_versions(id) ON DELETE CASCADE,
    id TEXT NOT NULL,
    interface TEXT NOT NULL DEFAULT '',
    module TEXT NOT NULL DEFAULT '',
    path TEXT NOT NULL DEFAULT '',
    title TEXT NOT NULL DEFAULT '',
    members JSONB NOT NULL DEFAULT '[]'::jsonb,
    PRIMARY KEY (version_id, id)
);

CREATE TABLE IF NOT EXISTS edges (
    version_id BIGINT NOT NULL REFERENCES api_versions(id) ON DELETE CASCADE,
    module TEXT NOT NULL DEFAULT '',
    source TEXT NOT NULL,
    target TEXT NOT NULL,
    type TEXT NOT NULL,
    label TEXT NOT NULL DEFAULT ''
);

CREATE INDEX IF NOT EXISTS documents_version_path_idx ON documents (version_id, path);
CREATE INDEX IF NOT EXISTS documents_version_module_kind_idx ON documents (version_id, module, kind);
CREATE INDEX IF NOT EXISTS documents_search_idx ON documents USING GIN (search_vector);
CREATE INDEX IF NOT EXISTS documents_symbol_trgm_idx ON documents USING GIN (symbol gin_trgm_ops);
CREATE INDEX IF NOT EXISTS documents_title_trgm_idx ON documents USING GIN (title gin_trgm_ops);

CREATE INDEX IF NOT EXISTS symbols_version_symbol_idx ON symbols (version_id, symbol);
CREATE INDEX IF NOT EXISTS symbols_version_module_kind_idx ON symbols (version_id, module, kind);
CREATE INDEX IF NOT EXISTS symbols_symbol_trgm_idx ON symbols USING GIN (symbol gin_trgm_ops);
CREATE INDEX IF NOT EXISTS symbols_title_trgm_idx ON symbols USING GIN (title gin_trgm_ops);

CREATE INDEX IF NOT EXISTS interface_members_version_interface_idx
    ON interface_members (version_id, interface);

CREATE INDEX IF NOT EXISTS edges_version_source_idx ON edges (version_id, source);
CREATE INDEX IF NOT EXISTS edges_version_target_idx ON edges (version_id, target);
CREATE INDEX IF NOT EXISTS edges_version_type_idx ON edges (version_id, type);
