---
title: "swSurfaceFinishSymbolOrientation_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swSurfaceFinishSymbolOrientation_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSurfaceFinishSymbolOrientation_e.html"
---

# swSurfaceFinishSymbolOrientation_e Enumeration

Surface finish symbol orientations.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swSurfaceFinishSymbolOrientation_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swSurfaceFinishSymbolOrientation_e
```

### C#

```csharp
public enum swSurfaceFinishSymbolOrientation_e : System.Enum
```

### C++/CLI

```cpp
public enum class swSurfaceFinishSymbolOrientation_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swSFOrientation_Perpendicular | 3 = Symbol is displayed at the same angle as the attached entity |
| swSFOrientation_PerpendicularFlipped | 4 = Symbol is displayed at the same angle as the attached entity, but the symbol is flipped to the other side of the entity |
| swSFOrientation_Rotated90 | 2 = Symbol is displayed vertical (rotated 90 clockwise) |
| swSFOrientation_Upright | 1 = Symbol is displayed horizontal |
| swSFOrientation_UserDefined | 5 = Symbol is displayed at a user-specified angle |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
