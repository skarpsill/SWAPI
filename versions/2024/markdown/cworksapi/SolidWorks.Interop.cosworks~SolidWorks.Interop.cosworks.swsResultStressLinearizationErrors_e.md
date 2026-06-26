---
title: "swsResultStressLinearizationErrors_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsResultStressLinearizationErrors_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultStressLinearizationErrors_e.html"
---

# swsResultStressLinearizationErrors_e Enumeration

Linearized stress errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsResultStressLinearizationErrors_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsResultStressLinearizationErrors_e
```

### C#

```csharp
public enum swsResultStressLinearizationErrors_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsResultStressLinearizationErrors_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsStressLinearization_AllElementsNotFoundForIntermediatePoints | 8 = No elements were found near any of the intermediate points |
| swsStressLinearization_DatabaseNotAvailable | 4 = Mesh or study results are not available |
| swsStressLinearization_ElementalValuesNotSupported | 10 = Plotting with elemental values is not supported |
| swsStressLinearization_ElementsFromDifferentComponents | 7 = Elements at the end points are from different bodies |
| swsStressLinearization_ElementsNotFoundForEndPoints | 6 = No elements were found near the specified end points |
| swsStressLinearization_IncorrectNumberOfIntermediatePoints | 5 = Number of intermediate points must be greater than 0 and less than 100 |
| swsStressLinearization_InvalidNumberOfPointsSelected | 13 = Number of points must be 2 |
| swsStressLinearization_InvalidReferencePlane | 3 = Only SWDATUMPLANES are supported |
| swsStressLinearization_InvalidResultComponent | 12 = Invalid result component |
| swsStressLinearization_MeshTypeNotSupported | 2 = Only solid meshes are supported |
| swsStressLinearization_SpecifiedPointsNotOnSectionPlane | 9 = The specified points are not on the section plane |
| swsStressLinearization_StudyNotSupported | 1 = Only pressure vessel studies are supported |
| swsStressLinearization_Success | 0 |
| swsStressLinearization_VectorPlotNotSupported | 11 = Vector plots are not supported |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
