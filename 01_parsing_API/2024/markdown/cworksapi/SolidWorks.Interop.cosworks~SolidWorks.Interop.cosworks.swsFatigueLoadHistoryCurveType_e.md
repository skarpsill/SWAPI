---
title: "swsFatigueLoadHistoryCurveType_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsFatigueLoadHistoryCurveType_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFatigueLoadHistoryCurveType_e.html"
---

# swsFatigueLoadHistoryCurveType_e Enumeration

Types of fatigue load history curves

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsFatigueLoadHistoryCurveType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsFatigueLoadHistoryCurveType_e
```

### C#

```csharp
public enum swsFatigueLoadHistoryCurveType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsFatigueLoadHistoryCurveType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsFatigueLoadHistoryCurveType_AmplitudeOnly | 0 = Define curve by one column of data representing amplitude; do not use this option if your study has multiple fatigue events |
| swsFatigueLoadHistoryCurveType_SamplingRateAndAmplitude | 1 = Define curve by one column of data representing amplitude and specify a value in seconds for the sampling rate; do not use this option if your study has multiple fatigue events |
| swsFatigueLoadHistoryCurveType_TimeAndAmplitude | 2 = Define curve by two columns of data representing pairs of time and amplitude; use this option if your study has multiple fatigue events |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
