---
title: "swsRunAnalysisError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsRunAnalysisError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRunAnalysisError_e.html"
---

# swsRunAnalysisError_e Enumeration

Run analysis errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsRunAnalysisError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsRunAnalysisError_e
```

### C#

```csharp
public enum swsRunAnalysisError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsRunAnalysisError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsRunAnalysisDefineInitialTemperature | 3 = Define initial temperatures to perform transient thermal analysis |
| swsRunAnalysisErrorAnalysisFailed | 24 = Analysis failed |
| swsRunAnalysisErrorAuthorizationFailed | 22 = Authorization failed for this analysis type |
| swsRunAnalysisErrorDefineRigidVirtualWallContact | 2 = Rigid virtual wall contact must be defined for grounded bolts |
| swsRunAnalysisErrorEXMaterialPropertyNotDefined | 13 = Elastic modulus (EX) material property not defined |
| swsRunAnalysisErrorEXValue | 14 = Elastic modulus (EX) should be > 0.0 |
| swsRunAnalysisErrorInvalidLBC | 30 = Invalid load boundary conditions |
| swsRunAnalysisErrorMaterialNotDefined | 19 = Material is not defined |
| swsRunAnalysisErrorMaterialNotDefinedForComponents | 20 = Material is not defined for one or more components |
| swsRunAnalysisErrorMaterialNotDefinedForShells | 18 = Material is not defined for one or more shells |
| swsRunAnalysisErrorMeshNotFound | 23 = Mesh not found; create mesh first |
| swsRunAnalysisErrorMeshNotIdentical | 11 = The mesh is not identical for static studies used in different events |
| swsRunAnalysisErrorMultipleLoadsUseSameTimeCurve | 4 = Multiple loads on an entity should use the same time curve |
| swsRunAnalysisErrorNeedOneOrMoreStaticStudies | 6 = One or more static, nonlinear, or linear dynamic studies needed to perform fatigue analysis; studies containing beams only are excluded |
| swsRunAnalysisErrorNoFatigueEvent | 7 = No fatigue event defined |
| swsRunAnalysisErrorNoSNCurve | 9 = No SN curve available |
| swsRunAnalysisErrorNoSolidBody | 21 = No solid body to process |
| swsRunAnalysisErrorNoValidShell | 12 = No valid shell defined |
| swsRunAnalysisErrorPadaptiveNotSupportCyclicSymmetry | 27 = Cyclic symmetry is incompatible with p-adaptive method |
| swsRunAnalysisErrorPadaptiveNotSupportLargeDisplacement | 26 = Large displacement is incompatible with p-adaptive method |
| swsRunAnalysisErrorPadaptiveNotSupportNoPenetration | 28 = No Penetration contact is incompatible with p-adaptive method |
| swsRunAnalysisErrorPadaptiveNotSupportRemoteLoadMassGapContactConnector | 29 = P-adaptive method does not support: remove load/mass gap contact connectors |
| swsRunAnalysisErrorPoissonsRatio | 15 = Poisson's Ratio should be less than 0.5 |
| swsRunAnalysisErrorRemoveOrChangeCreep | 17 = Creep option for material works only with force control method; remove creep or change the control method in the Advanced page of study's properties |
| swsRunAnalysisErrorSetUpDropTestStudy | 5 = Drop test study is not set up |
| swsRunAnalysisErrorStudyNotExist | 25 = Study does not exist |
| swsRunAnalysisErrorSuccessful | 0 = Successful |
| swsRunAnalysisErrorThermalConductivityNotDefined | 16 = Thermal conductivity not defined |
| swsRunAnalysisErrorTimeDependentOrAmplitideOnlyLoads | 8 = All loads should be either time dependent or amplitude only |
| swsRunAnalysisErrorUseHighQualityMesh | 1 = Draft mesh is incompatible with p-adaptive method; use high quality mesh |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
