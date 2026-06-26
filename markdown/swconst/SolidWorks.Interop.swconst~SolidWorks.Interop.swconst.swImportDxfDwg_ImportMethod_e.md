---
title: "swImportDxfDwg_ImportMethod_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swImportDxfDwg_ImportMethod_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swImportDxfDwg_ImportMethod_e.html"
---

# swImportDxfDwg_ImportMethod_e Enumeration

DXF/DWG import methods.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swImportDxfDwg_ImportMethod_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swImportDxfDwg_ImportMethod_e
```

### C#

```csharp
public enum swImportDxfDwg_ImportMethod_e : System.Enum
```

### C++/CLI

```cpp
public enum class swImportDxfDwg_ImportMethod_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swImportDxfDwg_DoNotImportSheet | 0 = Do not import this sheet (layout) |
| swImportDxfDwg_ImportToDrawing | 1 = Import this sheet (layout) to a sheet in a new drawing |
| swImportDxfDwg_ImportToExistingDrawing | 3 = Import this sheet (layout) into an existing drawing |
| swImportDxfDwg_ImportToExistingPart | 4 = Import this sheet (layout) into an existing part |
| swImportDxfDwg_ImportToPartSketch | 2 = Import this sheet (layout) into a sketch in a new part |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
