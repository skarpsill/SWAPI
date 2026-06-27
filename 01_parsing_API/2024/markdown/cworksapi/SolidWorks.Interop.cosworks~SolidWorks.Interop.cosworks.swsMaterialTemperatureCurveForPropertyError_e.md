---
title: "swsMaterialTemperatureCurveForPropertyError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsMaterialTemperatureCurveForPropertyError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMaterialTemperatureCurveForPropertyError_e.html"
---

# swsMaterialTemperatureCurveForPropertyError_e Enumeration

Temperature curve data errors for materials

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsMaterialTemperatureCurveForPropertyError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsMaterialTemperatureCurveForPropertyError_e
```

### C#

```csharp
public enum swsMaterialTemperatureCurveForPropertyError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsMaterialTemperatureCurveForPropertyError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsMaterialTemperatureCurveForPropertyErrorInvalidArray | 4 = Invalid array |
| swsMaterialTemperatureCurveForPropertyErrorNeedDataPoints | 5 = Curve must have at least two data points |
| swsMaterialTemperatureCurveForPropertyErrorNotAllowed | 3 = Temperature curve not allowed for Nitinol material |
| swsMaterialTemperatureCurveForPropertyErrorNotApplicable | 2 = Temperature curve is not applicable for this property |
| swsMaterialTemperatureCurveForPropertyErrorPropertyNotDefined | 1 = Property not defined for this material model |
| swsMaterialTemperatureCurveForPropertyErrorSuccessful | 0 = Successful |
| swsMaterialTemperatureCurveForPropertyErrorTermperatures | 6 = Temperature values should be monotonically increasing |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
