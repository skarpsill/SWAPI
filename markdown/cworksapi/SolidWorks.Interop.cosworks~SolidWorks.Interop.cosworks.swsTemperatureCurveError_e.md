---
title: "swsTemperatureCurveError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsTemperatureCurveError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTemperatureCurveError_e.html"
---

# swsTemperatureCurveError_e Enumeration

Temperature curve errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsTemperatureCurveError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsTemperatureCurveError_e
```

### C#

```csharp
public enum swsTemperatureCurveError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsTemperatureCurveError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsTemperatureCurveErrorCurveCannotBeUsed | 2 = Temperature curve cannot be used with this object |
| swsTemperatureCurveErrorInvalidStudy | 1 = Invalid study type for curve |
| swsTemperatureCurveErrorNeedDataPoints | 3 = Temperature curve must have two or more data points |
| swsTemperatureCurveErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
