---
title: "swsTimeCurveError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsTimeCurveError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTimeCurveError_e.html"
---

# swsTimeCurveError_e Enumeration

Time curve data errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsTimeCurveError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsTimeCurveError_e
```

### C#

```csharp
public enum swsTimeCurveError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsTimeCurveError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsTimeCurveErrorCannotUseWithRestraint | 2 = Time curve cannot be used with this restraint |
| swsTimeCurveErrorInvalidDataPoints | 4 = Invalid data points |
| swsTimeCurveErrorInvalidStudyType | 1 = Invalid study type for time curve |
| swsTimeCurveErrorNeedTwoOrMoreDataPoints | 3 = A time curve must have two or more data points |
| swsTimeCurveErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
