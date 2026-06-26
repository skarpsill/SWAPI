---
title: "swsSpringConnectorError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsSpringConnectorError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSpringConnectorError_e.html"
---

# swsSpringConnectorError_e Enumeration

Spring connector errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsSpringConnectorError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsSpringConnectorError_e
```

### C#

```csharp
public enum swsSpringConnectorError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsSpringConnectorError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsSpringConnectorErrorBodyExcludedFromAnalysis | 22 = Selected entity is on a body excluded from analysis |
| swsSpringConnectorErrorCylindricalFacesRadiiNotEqual | 8 = Radii of cylindrical faces of components are not equal |
| swsSpringConnectorErrorEmptyArray | 20 = Array has an empty dispatch |
| swsSpringConnectorErrorHasRemoteMass | 19 = Entity has a remote mass |
| swsSpringConnectorErrorInvalidArray | 13 = Invalid array |
| swsSpringConnectorErrorInvalidMesh | 1 = Invalid mesh |
| swsSpringConnectorErrorInvalidStudy | 3 = Invalid study |
| swsSpringConnectorErrorNonlinearStudyPartDocument | 2 = Study type equals nonlinear and document type equals part |
| swsSpringConnectorErrorNoObjectForSourceOrTarget | 15 = No object for source or target |
| swsSpringConnectorErrorNumberPlanarFacesLessThanTwo | 14 = Number of planar faces < 2 |
| swsSpringConnectorErrorSelectDatumPoint | 16 = Select a datum point |
| swsSpringConnectorErrorSelectEntities | 4 = Select entities |
| swsSpringConnectorErrorSelectFace | 5 = Select a face |
| swsSpringConnectorErrorSelectFaceWithCylindricalSurface | 6 = Select a face with a cylindrical surface |
| swsSpringConnectorErrorSelectionsOnToSameComponent | 18 = Selections belong to same component |
| swsSpringConnectorErrorSelectPlanarFace | 9 = Select a planar face |
| swsSpringConnectorErrorSelectTwoConcentricCylindricalFaces | 7 = Select two concentric cylindrical faces from two bodies |
| swsSpringConnectorErrorSelectTwoPlanarFaces | 10 = Select two planar faces from two bodies |
| swsSpringConnectorErrorSourceTargetEntitiesSame | 11 = Source and target entities are the same |
| swsSpringConnectorErrorSpringSubtypeInvalidForShellMesh | 21 = Spring subtype is invalid for shell mesh |
| swsSpringConnectorErrorStudyNonlinearAndSpringSubtypeValue | 12 = Study type is nonlinear and spring subtype is either 0 or 1 |
| swsSpringConnectorErrorSuccessful | 0 = Successful |
| swsSpringConnectorErrorTooManyEntitiesForSpringType | 17 = Number of entities is >1 for spring type = 2 |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
