---
title: "swsSpringConnectorEndEditError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsSpringConnectorEndEditError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSpringConnectorEndEditError_e.html"
---

# swsSpringConnectorEndEditError_e Enumeration

Spring connector editing errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsSpringConnectorEndEditError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsSpringConnectorEndEditError_e
```

### C#

```csharp
public enum swsSpringConnectorEndEditError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsSpringConnectorEndEditError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsSpringConnectorEndEditErrorBodyExcludedFromAnalysis | 18 = Select entity is on a body excluded from analysis |
| swsSpringConnectorEndEditErrorEntityAlreadyExists | 11 = Entity already exists |
| swsSpringConnectorEndEditErrorHasBeamBody | 14 = Connector has beam body |
| swsSpringConnectorEndEditErrorHasMassElement | 15 = Connector has mass element |
| swsSpringConnectorEndEditErrorIndexInvalidForRemovalOfEntity | 13 = Specified index is invalid for removal of entity in the first location |
| swsSpringConnectorEndEditErrorNoEntity | 1 = No entity selected |
| swsSpringConnectorEndEditErrorNoEntityAtIndex | 12 = No entity at specified index |
| swsSpringConnectorEndEditErrorNormalTangentialOrRotationalStiffness | 8 = Select anon-negative value for normal or tangential or rotational stiffness |
| swsSpringConnectorEndEditErrorNullEntity | 17 = Entity is NULL |
| swsSpringConnectorEndEditErrorRadiiNotEqual | 7 = Radii of cylindrical faces of components are not equal |
| swsSpringConnectorEndEditErrorSelectConcentricCylindricalFaces | 6 = Select two concentric faces from two bodies |
| swsSpringConnectorEndEditErrorSelectDatumPointOrVertex | 10 = Select datum point or vertex |
| swsSpringConnectorEndEditErrorSelectFace | 2 = Select a face |
| swsSpringConnectorEndEditErrorSelectFaceWithCylindricalSurface | 5 = Select a face with a cylindrical surface |
| swsSpringConnectorEndEditErrorSelectionsBelongToSameBody | 16 = Selections belong to the same body |
| swsSpringConnectorEndEditErrorSelectPlanarFace | 3 = Select a planar face |
| swsSpringConnectorEndEditErrorSelectTwoParallelPlanarFaces | 4 = Select two parallel planar faces from two bodies |
| swsSpringConnectorEndEditErrorStiffness | 9 = Specify a non-0 value for stiffness |
| swsSpringConnectorEndEditErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
