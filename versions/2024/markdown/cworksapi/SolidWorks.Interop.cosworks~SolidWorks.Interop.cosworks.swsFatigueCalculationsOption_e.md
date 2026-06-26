---
title: "swsFatigueCalculationsOption_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsFatigueCalculationsOption_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFatigueCalculationsOption_e.html"
---

# swsFatigueCalculationsOption_e Enumeration

Options for calculating fatigue in fatigue studies

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsFatigueCalculationsOption_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsFatigueCalculationsOption_e
```

### C#

```csharp
public enum swsFatigueCalculationsOption_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsFatigueCalculationsOption_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsFatigueCalculationsOption_SurfaceOnly | 1 = Calculate damage only at boundary nodes of the model |
| swsFatigueCalculationsOption_WholeModel | 0 = Calculate damage at all nodes of the model |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
