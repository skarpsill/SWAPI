---
title: "swAdvancedRouteSelectionOutput_e Enumeration"
project: "SOLIDWORKS Routing API Help"
interface: "swAdvancedRouteSelectionOutput_e"
member: ""
kind: "enum"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.swAdvancedRouteSelectionOutput_e.html"
---

# swAdvancedRouteSelectionOutput_e Enumeration

Highlight Search output types.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swAdvancedRouteSelectionOutput_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swAdvancedRouteSelectionOutput_e
```

### C#

```csharp
public enum swAdvancedRouteSelectionOutput_e : System.Enum
```

### C++/CLI

```cpp
public enum class swAdvancedRouteSelectionOutput_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swBoth | 0 = Both swSelectOnly and swDataOnly; default |
| swDataOnly | 2 = Returns data, but does not select the item |
| swSelectOnly | 1 = Selects the item but does not get its data |

## See Also

[SolidWorks.Interop.SWRoutingLib Namespace](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib_namespace.html)
