---
title: "swsFatigueAlternatingStressOption_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsFatigueAlternatingStressOption_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFatigueAlternatingStressOption_e.html"
---

# swsFatigueAlternatingStressOption_e Enumeration

Options for calculating alternating stress in fatigue studies

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsFatigueAlternatingStressOption_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsFatigueAlternatingStressOption_e
```

### C#

```csharp
public enum swsFatigueAlternatingStressOption_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsFatigueAlternatingStressOption_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsFatigueAlternatingStressOption_EquivalentStress | 1 = Calculate the von Mises stress |
| swsFatigueAlternatingStressOption_MaxAbsPrincipal | 2 = Calculate the larger alternating principal stress (P1) |
| swsFatigueAlternatingStressOption_StressIntensity | 0 = Calculate the difference between the larger alternating principal stress and the smaller alternating principal stress (P3 - P1) |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
