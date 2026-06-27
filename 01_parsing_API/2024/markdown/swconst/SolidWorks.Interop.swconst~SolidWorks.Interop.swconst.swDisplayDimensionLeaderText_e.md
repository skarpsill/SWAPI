---
title: "swDisplayDimensionLeaderText_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swDisplayDimensionLeaderText_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDisplayDimensionLeaderText_e.html"
---

# swDisplayDimensionLeaderText_e Enumeration

Display dimension leaders and text placement.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swDisplayDimensionLeaderText_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swDisplayDimensionLeaderText_e
```

### C#

```csharp
public enum swDisplayDimensionLeaderText_e : System.Enum
```

### C++/CLI

```cpp
public enum class swDisplayDimensionLeaderText_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swBrokenLeaderAlignedText | 3 = Leader is broken and the text is aligned with the leader |
| swBrokenLeaderHorizontalText | 2 = Leader is broken and the text is horizontal |
| swSolidLeaderAlignedText | 1 = Leader is solid (not broken) and the text is aligned with the leader |
| swSolidLeaderHorizontalText | 4 = The leader is solid and the text is horizontal; although this value can be applied to any type of dimension where the dimension text is not between the extension lines, it is currently only implemented by SOLIDWORKS for chamfer dimensions |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
