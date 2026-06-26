---
title: "swHoleTableTagOrder_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swHoleTableTagOrder_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swHoleTableTagOrder_e.html"
---

# swHoleTableTagOrder_e Enumeration

Method by which to assign tag numbers to holes of the same size.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swHoleTableTagOrder_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swHoleTableTagOrder_e
```

### C#

```csharp
public enum swHoleTableTagOrder_e : System.Enum
```

### C++/CLI

```cpp
public enum class swHoleTableTagOrder_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swHoleTableTagOrder_Radial | 3 = Number holes in order of increasing radial angle from the table view origin, starting at -180 degrees in a counterclockwise direction |
| swHoleTableTagOrder_ReduceToolPath | 2 = Number holes in next nearest order, starting at the table view origin |
| swHoleTableTagOrder_XY | 1 = Number holes in order of their XLoc and YLoc |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
