---
title: "swsResultPlotErrorCode_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsResultPlotErrorCode_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html"
---

# swsResultPlotErrorCode_e Enumeration

Result plot error codes

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsResultPlotErrorCode_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsResultPlotErrorCode_e
```

### C#

```csharp
public enum swsResultPlotErrorCode_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsResultPlotErrorCode_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsResultPlot_CosworksViewNotPresent | 16 = Cosmos view is not present |
| swsResultPlot_EquivalentStressNotApplicable | 15 = Equivalent stress plot is not applicable |
| swsResultPlot_FailedPlotCreation | 2 = Plot not created |
| swsResultPlot_ImproperResultsEquation | 13 = Invalid results equation |
| swsResultPlot_InvalidComponentType | 6 = Invalid result component type |
| swsResultPlot_InvalidExternalResultsFile | 17 |
| swsResultPlot_InvalidInputArgInCombiWithTensorVectorFlag | 4 = Tensor plot cannot be rendered when "Render Shell in 3D" or "Show plot on selected entities" is selected |
| swsResultPlot_InvalidIsoValueRange | 18 |
| swsResultPlot_InvalidMeshAppliedToStudy | 9 = Mesh not compatible with study type |
| swsResultPlot_InvalidResultType | 5 = Invalid result type |
| swsResultPlot_InvalidSelectedEntities | 3 = Invalid selected entities |
| swsResultPlot_InvalidSmoothingCycleRange | 19 |
| swsResultPlot_InvalidStudy | 1 = Study is missing important internal components |
| swsResultPlot_InvalidStudyType | 12 = Step numbers not compatible with study type |
| swsResultPlot_InvalidUnitType | 7 = Invalid unit type |
| swsResultPlot_IsAvailableOnlyForElements | 8 = Plot is valid only for elements |
| swsResultPlot_IsAvailableOnlyForNodes | 11 = Plot is valid only for nodes |
| swsResultPlot_MeshInformationNotFound | 20 |
| swsResultPlot_NoError | 0 = No error |
| swsResultPlot_PlotDoesNotExist | 14 = Result plot does not exist |
| swsResultPlot_TryingToSetInvalidProperty | 10 = Invalid property |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
