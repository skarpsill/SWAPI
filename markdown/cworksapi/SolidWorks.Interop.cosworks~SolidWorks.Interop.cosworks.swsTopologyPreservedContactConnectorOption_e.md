---
title: "swsTopologyPreservedContactConnectorOption_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsTopologyPreservedContactConnectorOption_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyPreservedContactConnectorOption_e.html"
---

# swsTopologyPreservedContactConnectorOption_e Enumeration

Topology study preserved region manufacturing control contacts and connectors options

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsTopologyPreservedContactConnectorOption_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsTopologyPreservedContactConnectorOption_e
```

### C#

```csharp
public enum swsTopologyPreservedContactConnectorOption_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsTopologyPreservedContactConnectorOption_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| PreservedContactConnectorOption_ConnectorsOnly | 1 = Exclude from optimization regions that have connectors |
| PreservedContactConnectorOption_ContactsAndConnectors | 2 = Exclude from optimization regions that have contacts or connectors |
| PreservedContactConnectorOption_ContactsOnly | 0 = Exclude from optimization regions that have contacts |
| PreservedContactConnectorOption_None | 3 = Specify the region to exclude from optimization |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
