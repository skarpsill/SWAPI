---
title: "swWireRouteError_e Enumeration"
project: "SOLIDWORKS Routing API Help"
interface: "swWireRouteError_e"
member: ""
kind: "enum"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.swWireRouteError_e.html"
---

# swWireRouteError_e Enumeration

Routing status.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swWireRouteError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swWireRouteError_e
```

### C#

```csharp
public enum swWireRouteError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swWireRouteError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swWireRouteError_WireMismatchedFromComponent | 5 |
| swWireRouteError_WireMismatchedFromPin | 7 |
| swWireRouteError_WireMismatchedToComponent | 6 |
| swWireRouteError_WireMismatchedToPin | 8 |
| swWireRouteError_WireMissingFromToComponent | 4 |
| swWireRouteError_WireNotRouted | 1 |
| swWireRouteError_WirePathViolatesBendRadius | 9 |
| swWireRouteError_WireSegmentsBranching | 2 |
| swWireRouteError_WireSegmentsDisjoint | 3 |

## See Also

[SolidWorks.Interop.SWRoutingLib Namespace](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib_namespace.html)
