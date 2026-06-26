---
title: "swsBoltConnectorError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsBoltConnectorError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsBoltConnectorError_e.html"
---

# swsBoltConnectorError_e Enumeration

Bolt connector errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsBoltConnectorError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsBoltConnectorError_e
```

### C#

```csharp
public enum swsBoltConnectorError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsBoltConnectorError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsBoltConnectorErrorArrayEmpty | 17 = Array has an empty dispatch |
| swsBoltConnectorErrorBodyExcludedFromAnalysis | 20 = Selected entity is on a body excluded from analysis |
| swsBoltConnectorErrorBoltDiameterTooLarge | 19 = Bolt diameter may be too large |
| swsBoltConnectorErrorEdgeFromSameFace | 21 = Selected edge belongs to a conical face of the same bolt |
| swsBoltConnectorErrorInvalidMesh | 1 = Invalid mesh type |
| swsBoltConnectorErrorInvalidStudy | 3 = Invalid study |
| swsBoltConnectorErrorNonLinearStudyAndPartDocument | 2 = Study type equals nonlinear and document type equals part |
| swsBoltConnectorErrorNoObjectForNutOrHead | 15 = No object for either the nut or head |
| swsBoltConnectorErrorSameEntityHeadAndNut | 13 = Entity is the same for the head and nut |
| swsBoltConnectorErrorSelectAssemblyDocument | 14 = Document type is part; select an assembly document |
| swsBoltConnectorErrorSelectCircularEdgeOnShells | 18 = Select circular edge on shells |
| swsBoltConnectorErrorSelectConcentricEntities | 9 = Select concentric entities |
| swsBoltConnectorErrorSelectCylindricalThreadFace | 8 = Select cylindrical thread face from a different body |
| swsBoltConnectorErrorSelectDatumPlane | 10 = Select datum plane |
| swsBoltConnectorErrorSelectEdge | 11 = Select an edge |
| swsBoltConnectorErrorSelectEdgeWithCircularLine | 6 = Select an edge with circular line |
| swsBoltConnectorErrorSelectEntity | 4 = Select an entity |
| swsBoltConnectorErrorSelectFace | 12 = Select a face |
| swsBoltConnectorErrorSelectFaceWithConicalSurface | 5 = Select a face with conical surface |
| swsBoltConnectorErrorSelectFaceWithCylindricalSurface | 7 = Select a face with cylindrical surface |
| swsBoltConnectorErrorSelectNutOrHead | 16 = Number of entities selected for the nut or head is < 1 |
| swsBoltConnectorErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
