---
title: "swsNonLinearStudyOptionsError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsNonLinearStudyOptionsError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsNonLinearStudyOptionsError_e.html"
---

# swsNonLinearStudyOptionsError_e Enumeration

Nonlinear study option errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsNonLinearStudyOptionsError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsNonLinearStudyOptionsError_e
```

### C#

```csharp
public enum swsNonLinearStudyOptionsError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsNonLinearStudyOptionsError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsNonLinearStudyInvalidArcLengthMaximumDisplacementValue | 17 = Invalid arc-length displacement value |
| swsNonLinearStudyInvalidArcLengthMaximumLoadValue | 18 = Invalid arc-length load value |
| swsNonLinearStudyInvalidArcLengthMultiplierValue | 16 = Value for maximum displacement (for translation DOF) is either <0.1 or >1 |
| swsNonLinearStudyInvalidArcLengthStepsValue | 19 = Invalid arc-length steps value |
| swsNonLinearStudyInvalidDisplaceComponentUnitValue | 15 = Unit value for displacement component unit is <0 or >4 |
| swsNonLinearStudyInvalidDisplaceComponentValue | 14 = Displacement component value is <0 or >5 |
| swsNonLinearStudyInvalidSingularityEliminationfactorValue | 20 = Invalid singularity elimination factor value |
| swsNonLinearStudyOptionsErrorAutoSteppingParameters | 2 = All auto-stepping parameters should be less than end time |
| swsNonLinearStudyOptionsErrorEmptyDispatch | 12 = Empty Dispatch parameter |
| swsNonLinearStudyOptionsErrorSelectArcLengthControlType | 7 = Select the arc-length control type |
| swsNonLinearStudyOptionsErrorSelectDirectSolver | 9 = Select direct solver |
| swsNonLinearStudyOptionsErrorSelectDisplacementControlType | 6 = Select the displacement control type |
| swsNonLinearStudyOptionsErrorSelectForceControl | 10 = Select force control type |
| swsNonLinearStudyOptionsErrorSelectTimeCurve | 8 = Select a time curve |
| swsNonLinearStudyOptionsErrorSelectVerticesOrDatumPoint | 5 = Select a vertex or datum point |
| swsNonLinearStudyOptionsErrorSolutionSteps | 4 = Nonlinear analysis can have up to 15,000 solution steps |
| swsNonLinearStudyOptionsErrorStartEndStepsAndIncrement | 1 = Start time step, end time step, and increment should all be > 0 |
| swsNonLinearStudyOptionsErrorStartTimeLessThanEndTime | 3 = Start time should be < end time |
| swsNonLinearStudyOptionsErrorSuccessful | 0 = Successful |
| swsNonLinearStudyOptionsErrorWrongArcLengthUnit | 11 = Incorrect unit input; must be between 0 and 4 |
| swsNonLinearStudyTimeCurveErrorInvalidStudyType | 13 = Invalid study type |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
