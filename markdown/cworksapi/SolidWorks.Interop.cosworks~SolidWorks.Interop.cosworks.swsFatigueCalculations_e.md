---
title: "swsFatigueCalculations_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsFatigueCalculations_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFatigueCalculations_e.html"
---

# swsFatigueCalculations_e Enumeration

Options for calculating fatigue in fatigue studies

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsFatigueCalculations_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsFatigueCalculations_e
```

### C#

```csharp
public enum swsFatigueCalculations_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsFatigueCalculations_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsFatigueCalculations_SurfaceOnly | 1 = Calculate damage only at boundary nodes of the model. |
| swsFatigueCalculations_WholeModel | 0 = Calculate damage at all nodes of the model. |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
