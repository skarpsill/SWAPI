---
title: "swsBearingConnectorErrors_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsBearingConnectorErrors_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsBearingConnectorErrors_e.html"
---

# swsBearingConnectorErrors_e Enumeration

Bearing connector errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsBearingConnectorErrors_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsBearingConnectorErrors_e
```

### C#

```csharp
public enum swsBearingConnectorErrors_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsBearingConnectorErrors_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsBearingConnectorErrCode_FacesOrEdgesSelectedFromSingleComponent | 15 = Select cylindrical faces from 2 different components |
| swsBearingConnectorErrCode_InadequateEntitiesSelection | 12 = Insufficient entities are selected; not enough for valid linkage rod definition |
| swsBearingConnectorErrCode_InvalidConnectionType | 17 = Connection type must be chosen from swsBearingConnectionType_e |
| swsBearingConnectorErrCode_InvalidSelectionForHousing | 4 = Select only single cylindrical face of solid body or an edge of shell or surface body for housing |
| swsBearingConnectorErrCode_InvalidSelectionForShaft | 5 = Select only single cylindrical face of solid body for shaft |
| swsBearingConnectorErrCode_InvalidUnitType | 7 = Unit type must be choosen from swsUnit_e |
| swsBearingConnectorErrCode_LenByDiamRatioGreaterThan2ForShaft | 16 = Length/diameter of shaft > 2 |
| swsBearingConnectorErrCode_MoreThanOneFaceOrEdgeSelectedForHousing | 14 = Select only single cylindrical face of solid body or an edge of shell or surface body for housing |
| swsBearingConnectorErrCode_MoreThanOneFaceSelectedForShaft | 13 = Select only single cylindrical face of solid body for shaft |
| swsBearingConnectorErrCode_NoActiveDoc | 1 = Active document not found |
| swsBearingConnectorErrCode_NoActiveStudy | 2 = Active simulation study not found |
| swsBearingConnectorErrCode_OutOfRangeAxialStiffness | 9 = Set valid value between 0 and 1e+16 for axial stiffness |
| swsBearingConnectorErrCode_OutOfRangeLateralStiffness | 8 = Set valid value between 0 and 1e+16 for lateral stiffness |
| swsBearingConnectorErrCode_OutOfRangeShaftStabilizeStiffness | 11 = Set valid value between 0 and 1e+16 for shaft stabilize stiffness |
| swsBearingConnectorErrCode_OutOfRangeTiltStiffness | 10 = Set valid value between 0 and 1e+16 for tilt stiffness |
| swsBearingConnectorErrCode_SetOperationNotSupported | 3 = Started editing before BeginEdit() was called |
| swsBearingConnectorErrCode_SourceAndTargetSelectionsSwitched | 6 = Switch shaft and housing selections |
| swsBearingConnectorErrCode_Successful | 0 |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
