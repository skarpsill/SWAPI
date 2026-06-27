---
title: "swAcisOutputGeometryPreference_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swAcisOutputGeometryPreference_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAcisOutputGeometryPreference_e.html"
---

# swAcisOutputGeometryPreference_e Enumeration

ACIS output geometry types.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swAcisOutputGeometryPreference_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swAcisOutputGeometryPreference_e
```

### C#

```csharp
public enum swAcisOutputGeometryPreference_e : System.Enum
```

### C++/CLI

```cpp
public enum class swAcisOutputGeometryPreference_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAcisOutputAs3DCurves | 1 = 3D curves without export sketch entities |
| swAcisOutputAs3DCurves_IncludeSketchEnts | 2 = 3D curves with export sketch entities |
| swAcisOutputAsSolidAndSurface | 0 = Solid/surface geometry |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
