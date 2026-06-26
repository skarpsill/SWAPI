---
title: "swsMaterialDataCurveError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsMaterialDataCurveError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMaterialDataCurveError_e.html"
---

# swsMaterialDataCurveError_e Enumeration

Material curve data errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsMaterialDataCurveError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsMaterialDataCurveError_e
```

### C#

```csharp
public enum swsMaterialDataCurveError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsMaterialDataCurveError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsMaterialDataCurveErrorCannotBeDefined | 1 = Material data curve cannot be defined for this material model |
| swsMaterialDataCurveErrorIndexForMooneyRivlinAndOgeden | 3 = Index must be 0, 1, or 2 for Mooney-Rivlin and Ogeden material models |
| swsMaterialDataCurveErrorIndexForViscoElastic | 4 = Index must be 3 or 4 for the Visco-elastic material model |
| swsMaterialDataCurveErrorIndexValues | 2 = Valid index values are 0 to 4 |
| swsMaterialDataCurveErrorInvalidArray | 5 = Invalid array |
| swsMaterialDataCurveErrorNeedDataPoints | 7 = Curve must have at least two data points nIndex = 0; simple tension curve nIndex = 1; planar tension curve nIndex = 2; biaxial tension curve nIndex = 3; shear relaxation curve nIndex = 4; bulk relaxation curve |
| swsMaterialDataCurveErrorSuccessful | 0 = Successful |
| swsMaterialDataCurveErrorTemperatures | 6 = Temperature values should be monotonically increasing |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
