---
title: "swsRandomVibrationCorrelationOption_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsRandomVibrationCorrelationOption_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRandomVibrationCorrelationOption_e.html"
---

# swsRandomVibrationCorrelationOption_e Enumeration

Options for load correlation in random vibration dynamic studies

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsRandomVibrationCorrelationOption_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsRandomVibrationCorrelationOption_e
```

### C#

```csharp
public enum swsRandomVibrationCorrelationOption_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsRandomVibrationCorrelationOption_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsRandomVibrationCorrelationOption_FullyCorrelated | 0 = Fully correlated; the distance between load nodes is smaller than a user-defined minimum radius |
| swsRandomVibrationCorrelationOption_FullyUnCorrelated | 1 = Fully uncorrelated; the distance between load nodes is larger than a user-defined maximum radius |
| swsRandomVibrationCorrelationOption_PartiallyCorrelated | 2 = Partially correlated; the distance between load nodes is between a user-defined minimum radius and a user-defined maximum radius |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
