---
title: "swsAddDefaultStaticStudyPlotResultError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsAddDefaultStaticStudyPlotResultError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsAddDefaultStaticStudyPlotResultError_e.html"
---

# swsAddDefaultStaticStudyPlotResultError_e Enumeration

Static study result plot errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsAddDefaultStaticStudyPlotResultError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsAddDefaultStaticStudyPlotResultError_e
```

### C#

```csharp
public enum swsAddDefaultStaticStudyPlotResultError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsAddDefaultStaticStudyPlotResultError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsStaticResultDisplacementComponentRangeError | 3 = The value of the displacement component is not within the supported range |
| swsStaticResultElementalStrainRangeError | 5 = The value of the elemental strain component is not within the supported range |
| swsStaticResultElementalStressComponentRangeError | 2 = The value of the elemental stress component is not within the supported range |
| swsStaticResultNodalStrainRangeError | 4 = The value of the nodal strain component is not within the supported range |
| swsStaticResultNodalStressComponentRangeError | 6 = The value of the nodal stress component is not within the supported range |
| swsStaticResultNoErrror | 0 = No error |
| swsStaticResultTypeRangeError | 1 = The result type is not supported or is an invalid result type |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
