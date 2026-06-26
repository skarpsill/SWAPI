---
title: "swBoundType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swBoundType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundType_e.html"
---

# swBoundType_e Enumeration

Boundary behaviors at the start and end of UV parameter ranges.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swBoundType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swBoundType_e
```

### C#

```csharp
public enum swBoundType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swBoundType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swBoundType_Degenerate | 13741 ( see Remarks ) |
| swBoundType_Extendable | 13734 |
| swBoundType_Infinite | 13733 |
| swBoundType_NotExtendable | 13735 |
| swBoundType_Periodic | 13701 |
| swBoundType_PeriodicNotDifferentiable | 13736 = Not continuously differentiable across the boundary. |

## Remarks

If the behavior at the start of the U range is Degenerate', then the V parameter is degenerate when U = urange[0]'. The derivative of the parameterization function with respect to v is 0 whenever u = urange[0]', for all values of v, and the parameter curve corresponding to u = urange[0]' degenerates to a single point. A parameterization can only degenerate at the end of its range, unless the surface is a B-spline surface.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
