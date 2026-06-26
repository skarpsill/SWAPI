---
title: "swArrowPlacement_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swArrowPlacement_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swArrowPlacement_e.html"
---

# swArrowPlacement_e Enumeration

Smart arrow placement.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swArrowPlacement_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swArrowPlacement_e
```

### C#

```csharp
public enum swArrowPlacement_e : System.Enum
```

### C++/CLI

```cpp
public enum class swArrowPlacement_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swArrowPlacementLegacy | 0 = Vary Smart arrow placement as in SOLIDWORKS 2012 and earlier (see Remarks ) |
| swArrowPlacementSmartArrowFollowText | 1 |
| swArrowPlacementSmartArrowRemainAttachedToArc | 2 |

## Remarks

In SOLIDWORKS 2012 and earlier, Smart arrows sometimes:

- Remained on the far side of an arc when moved to its other side.
- Were attached to an extension line.
- Pointed out to space.
- Were placed on the part.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
