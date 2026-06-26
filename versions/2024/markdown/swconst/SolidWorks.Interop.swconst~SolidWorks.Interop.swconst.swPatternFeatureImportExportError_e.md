---
title: "swPatternFeatureImportExportError_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swPatternFeatureImportExportError_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternFeatureImportExportError_e.html"
---

# swPatternFeatureImportExportError_e Enumeration

Variable pattern feature errors when importing or exporting Microsoft Excel data.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swPatternFeatureImportExportError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swPatternFeatureImportExportError_e
```

### C#

```csharp
public enum swPatternFeatureImportExportError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swPatternFeatureImportExportError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swPatternFeatureImportExportError_AccessDeniedOrInvalidPath | 19 = Access denied or invalid path |
| swPatternFeatureImportExportError_ColumnARows1And2Error | 5 = Column A, Rows 1 and 2 must be merged and named Instance |
| swPatternFeatureImportExportError_ColumnBRows1And2Error | 7 = Column B, Rows 1 and 2 must be merged and named Instances to Skip |
| swPatternFeatureImportExportError_DimensionNameDoesNotExist | 12 = Dimension name does not exist in the parent feature |
| swPatternFeatureImportExportError_DimValueFormatIncorrect | 15 = Dimension is incorrectly formatted |
| swPatternFeatureImportExportError_DuplicateDimensions | 10 = Duplicate dimensions are not allowed in the import file |
| swPatternFeatureImportExportError_EmptyRowsOrColumns | 4 = Empty rows or columns are not allowed |
| swPatternFeatureImportExportError_Failed | 1 = Failed |
| swPatternFeatureImportExportError_FailedToRetrieveExcelApp | 20 = Failed to find Microsoft Excel application |
| swPatternFeatureImportExportError_FailedToRetrieveModelDocument | 16 = Failed to retrieve model document |
| swPatternFeatureImportExportError_FeatureDoesNotExist | 9 = Feature does not exist in the selected features or references to pattern |
| swPatternFeatureImportExportError_FeatureOrDimDoesNotExist | 13 = Feature does not exist in the selected features or references to pattern, or the dimension name does not exist in the parent feature |
| swPatternFeatureImportExportError_FileExistsAndOverwriteIsFalse | 17 = Microsoft Excel file exists, but the file cannot be overwritten |
| swPatternFeatureImportExportError_ImproperValuesForColumnB | 8 = Invalid value; valid values are 0 (not skipped) or 1 (skipped) |
| swPatternFeatureImportExportError_InstNumStartsFromNonZero | 6 = Instances in the Microsoft Excel table must start at 0 |
| swPatternFeatureImportExportError_NoValidDimensionToImport | 14 = No valid dimensions to import from this Microsoft Excel file |
| swPatternFeatureImportExportError_OutOfRangeDimensionValue | 11 = Dimension in this cell in is not in the range of dimensions |
| swPatternFeatureImportExportError_ReadOnlyFile | 18 = Microsoft Excel file is read only |
| swPatternFeatureImportExportError_Succeed | 0 = Succeeded |
| swPatternFeatureImportExportError_UnequalNumOfCellsInColumn | 2 = All columns containing dimensions in this imported table must have the same number of cells; these columns cannot be empty or merged |
| swPatternFeatureImportExportError_UnequalNumOfCellsInRow | 3 = All rows containing dimensions in this imported table must have the same number of cells; these rows cannot be empty or merged |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
