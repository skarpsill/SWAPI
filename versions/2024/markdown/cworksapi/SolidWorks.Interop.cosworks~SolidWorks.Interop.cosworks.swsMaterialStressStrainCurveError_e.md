---
title: "swsMaterialStressStrainCurveError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsMaterialStressStrainCurveError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMaterialStressStrainCurveError_e.html"
---

# swsMaterialStressStrainCurveError_e Enumeration

Stress-strain curve data errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsMaterialStressStrainCurveError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsMaterialStressStrainCurveError_e
```

### C#

```csharp
public enum swsMaterialStressStrainCurveError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsMaterialStressStrainCurveError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsMaterialStressStrainCurveErrorInvalidArray | 2 = Invalid array |
| swsMaterialStressStrainCurveErrorInvalidForMaterial | 1 = Stress-strain curve invalid for this material |
| swsMaterialStressStrainCurveErrorNeedDataPoints | 4 = Curve must have at least two data points |
| swsMaterialStressStrainCurveErrorSuccessful | 0 = Successful |
| swsMaterialStressStrainCurveErrorTemperatures | 3 = Temperature values should be monotonically increasing |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
