---
title: "swsTopologyStudyError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsTopologyStudyError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyError_e.html"
---

# swsTopologyStudyError_e Enumeration

Topology study result codes

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsTopologyStudyError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsTopologyStudyError_e
```

### C#

```csharp
public enum swsTopologyStudyError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsTopologyStudyError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsTopoErrCode_CannotCreatFOSIfStressAlrdyPrsnt | 18 = Factor of Safety constraint cannot be created if a stress constraint is present |
| swsTopoErrCode_CannotCreatStressIfFOSAlrdyPrsnt | 19 = Stress constraint cannot be created if a Factor of Safety constraint is present |
| swsTopoErrCode_ConstraintDefinitionLimitReached | 11 = No more than seven constraints can be defined |
| swsTopoErrCode_ConstraintNotFound | 9 |
| swsTopoErrCode_DefaultConstraintCannotBeRemoved | 10 |
| swsTopoErrCode_InvalidGoalType | 2 |
| swsTopoErrCode_ManufacturingControlNotFound | 12 |
| swsTopoErrCode_MaximizeStiffnessGoalHasNotBeenSet | 5 |
| swsTopoErrCode_MinimizeMassGoalHasNotBeenSet | 4 |
| swsTopoErrCode_MinimizeMaximumDisplacementGoalHasNotBeenSet | 6 |
| swsTopoErrCode_NoGoalHasBeenSet | 3 |
| swsTopoErrCode_OnlyOneDemoldControlCanBeDefined | 14 |
| swsTopoErrCode_OnlyOneDisplacementConstraintWithAutoDefineCanBeDefined | 8 |
| swsTopoErrCode_OnlyOneFOSConstraintCanBeDefined | 21 |
| swsTopoErrCode_OnlyOneFrequencyConstraintCanBeDefined | 16 |
| swsTopoErrCode_OnlyOneMassConstraintCanBeDefined | 7 |
| swsTopoErrCode_OnlyOneStressConstraintCanBeDefined | 20 |
| swsTopoErrCode_OnlyOneSymmetryControlCanBeDefined | 15 |
| swsTopoErrCode_OnlyOneThicknessControlCanBeDefined | 13 |
| swsTopoErrCode_SetOperationNotSupported | 17 = BeginEdit must be called before setting any values |
| swsTopoErrCode_Success | 0 |
| swsTopoErrCode_TopologyStudyManagerIsNotInitialized | 1 |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
