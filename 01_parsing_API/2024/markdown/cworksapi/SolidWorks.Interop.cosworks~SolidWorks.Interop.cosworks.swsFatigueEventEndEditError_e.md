---
title: "swsFatigueEventEndEditError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsFatigueEventEndEditError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFatigueEventEndEditError_e.html"
---

# swsFatigueEventEndEditError_e Enumeration

Fatigue event editing errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsFatigueEventEndEditError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsFatigueEventEndEditError_e
```

### C#

```csharp
public enum swsFatigueEventEndEditError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsFatigueEventEndEditError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsFatigueEventError_AssociatedStudyShouldBeStaticNonlinearOrDynamicModalTimeHistory | 21 = Associated study should be a static, nonlinear, or dynamic modal time history study |
| swsFatigueEventError_CannotApplyLoadingRatio | 12 = Loading ratio is invalid |
| swsFatigueEventError_CannotApplyRepeats | 13 = Cannot apply the specified number of repeats |
| swsFatigueEventError_CannotApplyStartTime | 15 = Cannot apply the specified start time of the fatigue event |
| swsFatigueEventError_ImproperEvent | 2 = Improper fatigue event |
| swsFatigueEventError_ImproperNoOfCycles | 10 = Number of cycles must be greater than 1 and less than 2000000000 |
| swsFatigueEventError_ImproperStudy | 1 = Improper fatigue study |
| swsFatigueEventError_ImproperStudyNames | 3 = Improper associated study names |
| swsFatigueEventError_ImproperVarNamesOrVarScalesOrVarSteps | 18 = Improper variable names, scales, or steps |
| swsFatigueEventError_InvalidLoadingtype | 11 = Loading type must be a number as defined in swsFatigueLoadingType_e |
| swsFatigueEventError_InvalidRepeats | 14 = Number of repeats must be greater than 0 and less than 1000000 |
| swsFatigueEventError_InvalidStartTime | 16 = Start time must be greater than 0 |
| swsFatigueEventError_LoadHistoryCurveTypeImproper | 4 = Load history curve type must be a number as defined in swsFatigueLoadHistoryCurveType_e |
| swsFatigueEventError_NoError | 0 = Success |
| swsFatigueEventError_NoOfPointsShouldBeMoreThan3 | 8 = Load history curve data must have more than 3 points |
| swsFatigueEventError_NumberOfStudiesAssociationShouldbeAtleast1 | 19 = Number of associated studies must be greater than 1 |
| swsFatigueEventError_NumberOfStudiesAssociationShouldbeAtleast2 | 20 = Number of associated studies must be greater than 2 |
| swsFatigueEventError_StudyNamesScalesAndStepsDifferentInNumber | 17 = Study names, scales, and steps are all different in number |
| swsFatigueEventError_XAndYPointsNotSameInNumber | 7 = X and Y values of the load history curve data are not the same in number |
| swsFatigueEventError_XCurveDataImproper | 5 = X values of load history curve data are improper |
| swsFatigueEventError_XPointsShouldBeInIncreasingOrder | 9 = X coordinate values of the load history curve data must be in order of increasing value |
| swsFatigueEventError_YCurveDataImproper | 6 = Y values of load history curve data are improper |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
