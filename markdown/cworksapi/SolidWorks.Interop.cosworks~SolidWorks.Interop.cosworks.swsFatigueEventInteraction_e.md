---
title: "swsFatigueEventInteraction_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsFatigueEventInteraction_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFatigueEventInteraction_e.html"
---

# swsFatigueEventInteraction_e Enumeration

Types of fatigue event interactions

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsFatigueEventInteraction_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsFatigueEventInteraction_e
```

### C#

```csharp
public enum swsFatigueEventInteraction_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsFatigueEventInteraction_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsFatigueEventInteraction_NoInteraction | 1 = Events occur sequentially without any interaction; predicts lower damage |
| swsFatigueEventInteraction_Random | 0 = Peak stresses from different events may intermingle; predicts higher damage |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
