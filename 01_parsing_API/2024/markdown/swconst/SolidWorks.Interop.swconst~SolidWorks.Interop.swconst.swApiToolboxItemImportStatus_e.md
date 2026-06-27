---
title: "swApiToolboxItemImportStatus_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swApiToolboxItemImportStatus_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swApiToolboxItemImportStatus_e.html"
---

# swApiToolboxItemImportStatus_e Enumeration

Return codes for toolbox item import.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swApiToolboxItemImportStatus_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swApiToolboxItemImportStatus_e
```

### C#

```csharp
public enum swApiToolboxItemImportStatus_e : System.Enum
```

### C++/CLI

```cpp
public enum class swApiToolboxItemImportStatus_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swApiToolboxItemImportStatus_ExcelCouldNotOpenFile | 6 |
| swApiToolboxItemImportStatus_ExcelImportDidNotFindColumn | 4 |
| swApiToolboxItemImportStatus_ExcelImportWrongFile | 5 |
| swApiToolboxItemImportStatus_FailedToSaveFile | 3 |
| swApiToolboxItemImportStatus_FailedUnspecifiedError | 8 |
| swApiToolboxItemImportStatus_InvalidArgument | 1 |
| swApiToolboxItemImportStatus_InvalidPartNumber | 7 |
| swApiToolboxItemImportStatus_MicrosoftExcelNotInstalled | 2 |
| swApiToolboxItemImportStatus_Success | 0 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
