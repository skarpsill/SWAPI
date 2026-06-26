---
title: "swsFatigueComponent_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsFatigueComponent_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFatigueComponent_e.html"
---

# swsFatigueComponent_e Enumeration

Fatigue components

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsFatigueComponent_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsFatigueComponent_e
```

### C#

```csharp
public enum swsFatigueComponent_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsFatigueComponent_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsFatigueComponent_BiaxialityIndicator | 3 = Report the ratio of the smaller alternating principal stress to the larger alternating principal stress |
| swsFatigueComponent_Damage | 1 = Report the cumulative damage factor at each node |
| swsFatigueComponent_Life | 0 = Report the number of cycles required to cause failure at each node |
| swsFatigueComponent_LoadFactor | 2 = Report the load factor of safety at each node |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
