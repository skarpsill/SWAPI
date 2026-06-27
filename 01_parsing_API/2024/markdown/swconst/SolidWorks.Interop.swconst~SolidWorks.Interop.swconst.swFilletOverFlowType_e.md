---
title: "swFilletOverFlowType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swFilletOverFlowType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFilletOverFlowType_e.html"
---

# swFilletOverFlowType_e Enumeration

Fillet overflow types.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swFilletOverFlowType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swFilletOverFlowType_e
```

### C#

```csharp
public enum swFilletOverFlowType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swFilletOverFlowType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swFilletOverFlowType_Default | 0 = Default; system picks the appropriate method to create a fillet when the fillet surface overflows to adjacent surfaces; it either smoothly blends with adjacent surfaces or limits the fillet surface with the adjacent edges, thereby not changing the edge, or trims the fillet surface by the adjacent surface onto which the fillet overflows; the method actually used by default depending on the geometric condition; this option always tries to create a fillet if possible |
| swFilletOverFlowType_KeepEdge | 1 = Edges that are overflowed by the fillet are not modified; the fillet surface is trimmed by all the adjacent edges; as a result, an additional transition fillet surface might be needed to complete the fillet |
| swFilletOverFlowType_KeepSurface | 2 = Fillet surface is either merged with the adjacent surfaces smoothly or trimmed by the adjacent surfaces; as a result, it is unlikely that an additional transition fillet surface is created |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
