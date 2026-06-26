---
title: "swArcEndCondition_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swArcEndCondition_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swArcEndCondition_e.html"
---

# swArcEndCondition_e Enumeration

Arc endpoint conditions for linear dimensions.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swArcEndCondition_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swArcEndCondition_e
```

### C#

```csharp
public enum swArcEndCondition_e : System.Enum
```

### C++/CLI

```cpp
public enum class swArcEndCondition_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swArcEndConditionCenter | 1 = End point is the center of the arc |
| swArcEndConditionMax | 3 = End point is the furthest point on the arc |
| swArcEndConditionMin | 2 = End point is the nearest point on the arc |
| swArcEndConditionNone | 0 = End point is not related to an arc |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
