---
title: "swsSaveeDrawingsErrorCode_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsSaveeDrawingsErrorCode_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSaveeDrawingsErrorCode_e.html"
---

# swsSaveeDrawingsErrorCode_e Enumeration

Result plots error codes when saving results as eDrawings files

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsSaveeDrawingsErrorCode_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsSaveeDrawingsErrorCode_e
```

### C#

```csharp
public enum swsSaveeDrawingsErrorCode_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsSaveeDrawingsErrorCode_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsSaveeDrawings_CosworksViewNotPresent | 1 = There is no view present |
| swsSaveeDrawings_DatabaseNotFound | 4 = Database not found |
| swsSaveeDrawings_NoError | 0 = No error |
| swsSaveeDrawings_NoPlots | 9 = There are no plots |
| swsSaveeDrawings_NotAvailableForCurrentMesh | 7 = Cannot save plot as an eDrawings file for current mesh type |
| swsSaveeDrawings_PlotNotActive | 6 = There is no active plot |
| swsSaveeDrawings_PlotNotFoundError | 2 = The specified plot is not present |
| swsSaveeDrawings_PlotSaveError | 10 = An error occurred when saving the plot as an eDrawings file |
| swsSaveeDrawings_PostDataFilesNotPresent | 9 = The post data files are not available |
| swsSaveeDrawings_PostFilesNull | 5 = The objects for the post files are not instantiated |
| swsSaveeDrawings_ResultFolderNotFound | 3 = The results folder is not available |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
