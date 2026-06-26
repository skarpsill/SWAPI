---
title: "swTolerances_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swTolerances_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTolerances_e.html"
---

# swTolerances_e Enumeration

Tolerance types.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swTolerances_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swTolerances_e
```

### C#

```csharp
public enum swTolerances_e : System.Enum
```

### C++/CLI

```cpp
public enum class swTolerances_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swBSCurveNonRationalOutputTol | 1 = 3D nonrational b-spline curve output tolerance (meters) |
| swBSCurveOutputTol | 0 = 3D b-spline curve output tolerance (meters) |
| swCurveChordTessellationTol | 5 = Chord tolerance or deviation for tessellation for curves |
| swSurfAngularTessellationTol | 4 = Angular tolerance or deviation for tessellation for surfaces |
| swSurfChordTessellationTol | 3 = Chord tolerance or deviation for tessellation for surfaces |
| swUVCurveOutputTol | 2 = 2D trim curve output tolerance (fraction of characteristic minimum face dimension) |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
