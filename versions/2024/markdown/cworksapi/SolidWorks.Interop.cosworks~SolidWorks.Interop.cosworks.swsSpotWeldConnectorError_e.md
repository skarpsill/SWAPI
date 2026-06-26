---
title: "swsSpotWeldConnectorError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsSpotWeldConnectorError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSpotWeldConnectorError_e.html"
---

# swsSpotWeldConnectorError_e Enumeration

Spot weld connector errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsSpotWeldConnectorError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsSpotWeldConnectorError_e
```

### C#

```csharp
public enum swsSpotWeldConnectorError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsSpotWeldConnectorError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| SpotWeldConnectorErrorSelectVerticesOrDatumPoint | 7 = Select vertices or a datum point |
| swsSpotWeldConnectorErrorBodyExcludedFromAnalysis | 16 = Selected entity is on a body excluded from analysis |
| swsSpotWeldConnectorErrorEmptyArray | 14 = Array for spot-weld entity is empty |
| swsSpotWeldConnectorErrorGapTooBig | 10 = Current gap between the spot-weld faces is greater than the recommended 3 mm |
| swsSpotWeldConnectorErrorHasRemoteMass | 15 = Spot-weld connector has a remote mass |
| swsSpotWeldConnectorErrorInvalidArray | 13 = Invalid array |
| swsSpotWeldConnectorErrorInvalidMesh | 1 = Invalid mesh |
| swsSpotWeldConnectorErrorInvalidStudy | 3 = Invalid study |
| swsSpotWeldConnectorErrorNonlinearStudyPartDocument | 2 = Study type equals nonlinear and document type equals part |
| swsSpotWeldConnectorErrorNullDispatch | 4 = NULL dispatch passed as argument |
| swsSpotWeldConnectorErrorPlanesNotParallel | 8 = Planes are not parallel |
| swsSpotWeldConnectorErrorPlanesTouching | 9 = Planes touching |
| swsSpotWeldConnectorErrorPostWeldInvalidPoints | 12 = Post weld invalid points |
| swsSpotWeldConnectorErrorSelectAssemblyDocument | 5 = Select an assembly document |
| swsSpotWeldConnectorErrorSelectDatumPoints | 11 = Select datum points for spot weld |
| swsSpotWeldConnectorErrorSelectFace | 6 = Select a face |
| swsSpotWeldConnectorErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
