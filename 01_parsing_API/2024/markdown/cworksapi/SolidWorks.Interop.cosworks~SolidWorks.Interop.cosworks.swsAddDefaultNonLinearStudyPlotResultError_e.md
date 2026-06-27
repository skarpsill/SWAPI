---
title: "swsAddDefaultNonLinearStudyPlotResultError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsAddDefaultNonLinearStudyPlotResultError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsAddDefaultNonLinearStudyPlotResultError_e.html"
---

# swsAddDefaultNonLinearStudyPlotResultError_e Enumeration

Nonlinear study result plot errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsAddDefaultNonLinearStudyPlotResultError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsAddDefaultNonLinearStudyPlotResultError_e
```

### C#

```csharp
public enum swsAddDefaultNonLinearStudyPlotResultError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsAddDefaultNonLinearStudyPlotResultError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsNonLinearResultDisplacementComponentRangeError | 4 = Displacement component is outside the range of supported values |
| swsNonLinearResultElementalStrainComponentRangeError | 6 = Elemental strain component is outside the range of supported values |
| swsNonLinearResultElementalStressComponentRangeError | 3 = Elemental stress component is outside the range of supported values |
| swsNonLinearResultNodalStrainComponentRangeError | 5 = Nodal strain component is outside the range of supported values |
| swsNonLinearResultNodalStressComponentRangeError | 2 = Nodal stress component is outside the range of supported values |
| swsNonLinearResultNoError | 0 |
| swsNonLinearResultRangeError | 1 = Elemental strain component value is outside the range of supported values |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
