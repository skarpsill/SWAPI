---
title: "swDimensionArrowsSide_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swDimensionArrowsSide_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDimensionArrowsSide_e.html"
---

# swDimensionArrowsSide_e Enumeration

Dimension arrow directions.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swDimensionArrowsSide_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swDimensionArrowsSide_e
```

### C#

```csharp
public enum swDimensionArrowsSide_e : System.Enum
```

### C++/CLI

```cpp
public enum class swDimensionArrowsSide_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDimArrowsFollowDoc | 3 = As per the document's default setting |
| swDimArrowsInside | 0 = Always positioned on the inside |
| swDimArrowsOutside | 1 = Always positioned on the outside |
| swDimArrowsSmart | 2 = Positioned on the inside, if there is room; otherwise, positioned on the outside |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
