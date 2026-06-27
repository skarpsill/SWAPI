---
title: "swsFatiguePlotType_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsFatiguePlotType_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFatiguePlotType_e.html"
---

# swsFatiguePlotType_e Enumeration

Types of fatigue result plots

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsFatiguePlotType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsFatiguePlotType_e
```

### C#

```csharp
public enum swsFatiguePlotType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsFatiguePlotType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsFatiguePlotType_BiaxialityIndicator | 3 = Plot the ratio of the smaller alternating principal stress to the larger alternating principal stress |
| swsFatiguePlotType_Damage | 1 = Plot the cumulative damage factor at each node |
| swsFatiguePlotType_Life | 0 = Plot the number of cycles required to cause failure at each node |
| swsFatiguePlotType_LoadFactor | 2 = Plot the load factor of safety at each node |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
