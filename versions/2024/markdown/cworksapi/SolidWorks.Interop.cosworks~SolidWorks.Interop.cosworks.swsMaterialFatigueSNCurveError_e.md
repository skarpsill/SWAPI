---
title: "swsMaterialFatigueSNCurveError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsMaterialFatigueSNCurveError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMaterialFatigueSNCurveError_e.html"
---

# swsMaterialFatigueSNCurveError_e Enumeration

Material stress-number (SN) curve data errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsMaterialFatigueSNCurveError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsMaterialFatigueSNCurveError_e
```

### C#

```csharp
public enum swsMaterialFatigueSNCurveError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsMaterialFatigueSNCurveError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsMaterialFatigueSNCurveErrorCurveDataPoints | 4 = Curve must have at least two data points |
| swsMaterialFatigueSNCurveErrorCycles | 3 = Cycle values should be monotonically increasing |
| swsMaterialFatigueSNCurveErrorIndexValues | 1 = Valid index values are 0 to 9 |
| swsMaterialFatigueSNCurveErrorInvalidArray | 2 = Invalid array |
| swsMaterialFatigueSNCurveErrorStressValuesMustBeUnique | 5 = Stress values must be unique for each number of cycles |
| swsMaterialFatigueSNCurveErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
