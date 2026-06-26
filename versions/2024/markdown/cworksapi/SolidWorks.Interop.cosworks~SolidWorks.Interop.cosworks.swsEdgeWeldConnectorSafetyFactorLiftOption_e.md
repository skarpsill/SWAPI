---
title: "swsEdgeWeldConnectorSafetyFactorLiftOption_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsEdgeWeldConnectorSafetyFactorLiftOption_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsEdgeWeldConnectorSafetyFactorLiftOption_e.html"
---

# swsEdgeWeldConnectorSafetyFactorLiftOption_e Enumeration

Lift safety factors used in calculating weld ultimate shear strength in edge weld connectors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsEdgeWeldConnectorSafetyFactorLiftOption_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsEdgeWeldConnectorSafetyFactorLiftOption_e
```

### C#

```csharp
public enum swsEdgeWeldConnectorSafetyFactorLiftOption_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsEdgeWeldConnectorSafetyFactorLiftOption_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsEdgeWeldConnectorSafetyFactorLiftOption_UnderTheHookLifting | 1 = American National Standard for Automotive Lifts: Reduces the weld's ultimate shear strength by a default factor of 5 (ANSI/ASME B30.20) |
| swsEdgeWeldConnectorSafetyFactorLiftOption_USAutomotiveLifts | 0 = Under the Hook Lifting Devices: Reduces the weld's ultimate shear strength by a default factor of 3 (ANSI/ALI B153.1-90) |

## Remarks

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
