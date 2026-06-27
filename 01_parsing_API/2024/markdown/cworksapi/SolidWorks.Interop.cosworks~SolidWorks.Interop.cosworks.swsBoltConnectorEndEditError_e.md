---
title: "swsBoltConnectorEndEditError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsBoltConnectorEndEditError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsBoltConnectorEndEditError_e.html"
---

# swsBoltConnectorEndEditError_e Enumeration

Bolt connector editing errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsBoltConnectorEndEditError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsBoltConnectorEndEditError_e
```

### C#

```csharp
public enum swsBoltConnectorEndEditError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsBoltConnectorEndEditError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsBoltConnectorEndEditErrorBodyExcludedFromAnalysis | 40 = Entity is on a body excluded from analysis |
| swsBoltConnectorEndEditErrorBodyHasBeamElement | 42 = Body has a beam element |
| swsBoltConnectorEndEditErrorBodyHasMassElement | 39 = Body has a mass element |
| swsBoltConnectorEndEditErrorBoltDiameterBiggerShankContactFaceDiameter | 25 = Bolt diameter cannot be greater than the minimum shank contact face diameter |
| swsBoltConnectorEndEditErrorDefineMaterial | 13 = Define a material |
| swsBoltConnectorEndEditErrorDocumentIsPart | 30 = Document type is part |
| swsBoltConnectorEndEditErrorEntityAlreadyExits | 27 = Entity already exists |
| swsBoltConnectorEndEditErrorEntitySelectionBoxesEmpty | 34 = Both entity selection boxes are empty |
| swsBoltConnectorEndEditErrorIncorrectHeadDiameter | 3 = Head diameter is either <= 0 or > the maximum value |
| swsBoltConnectorEndEditErrorIncorrectNutDiameter | 29 = Nut diameter is either < 0 or > maximum value |
| swsBoltConnectorEndEditErrorIncorrectShankDiameter | 7 = Shank diameter is <= 0 or > the maximum value |
| swsBoltConnectorEndEditErrorInvalidConnectionType | 44 |
| swsBoltConnectorEndEditErrorInvalidForAnalysis | 43 |
| swsBoltConnectorEndEditErrorNoEntity | 28 = No entity specified |
| swsBoltConnectorEndEditErrorNoMultiBoltSelected | 38 = Entity cannot be inserted because multi-bolt not selected |
| swsBoltConnectorEndEditErrorNoObjectAtIndex | 33 = No object at specified index |
| swsBoltConnectorEndEditErrorNoShearEffectSelected | 37 = Entity cannot be inserted because shear effect not selected |
| swsBoltConnectorEndEditErrorNullEntity | 41 = Entity is NULL |
| swsBoltConnectorEndEditErrorSelectBoltHeadAndNut | 17 = Select a bolt head and bolt nut from different bodies |
| swsBoltConnectorEndEditErrorSelectBoltNut | 26 = Select a bolt nut |
| swsBoltConnectorEndEditErrorSelectCircularEdge | 5 = Select a circular edge |
| swsBoltConnectorEndEditErrorSelectCoaxialCylindricalSurfaces | 23 = Select co-axial cylindrical surfaces from different components |
| swsBoltConnectorEndEditErrorSelectConcentricCylindricalFaces | 24 = Select concentric cylindrical faces from two bodies |
| swsBoltConnectorEndEditErrorSelectConcentricEntities | 9 = Select concentric entities |
| swsBoltConnectorEndEditErrorSelectConicalFaceAndBoltNut | 19 = Select conical face and bolt nut from different bodies |
| swsBoltConnectorEndEditErrorSelectConicalFaceAndFaceForThread | 20 = Select conical face and face for thread from different bodies |
| swsBoltConnectorEndEditErrorSelectConicalSurface | 2 = Select a conical surface |
| swsBoltConnectorEndEditErrorSelectCylindricalThreadFace | 6 = Select cylindrical thread face from a different body |
| swsBoltConnectorEndEditErrorSelectEdge | 4 = Select an edge |
| swsBoltConnectorEndEditErrorSelectEdgesOnShells | 32 = Select edges on shells |
| swsBoltConnectorEndEditErrorSelectFace | 1 = Select a face |
| swsBoltConnectorEndEditErrorSelectFaceForHeadNutFaceForThread | 18 = Select face for the head nut and face for the thread from different bodies |
| swsBoltConnectorEndEditErrorSelectFacesFromMultilayerBolt | 22 = Select faces from multi-layer bolt |
| swsBoltConnectorEndEditErrorSelectMass | 8 = Select a mass > 0 |
| swsBoltConnectorEndEditErrorSelectNutOrHead | 31 = Select a nut or head |
| swsBoltConnectorEndEditErrorSelectOneEntity | 35 = Can only select one entity per selection box |
| swsBoltConnectorEndEditErrorSelectPlanarFace | 16 = Select a planar face |
| swsBoltConnectorEndEditErrorSelectReferencePlane | 21 = Sleect a reference plane |
| swsBoltConnectorEndEditErrorSpecifyFrictionValue | 15 = Specify a friction value >= 0 and <= 1 |
| swsBoltConnectorEndEditErrorSpecifyPoissonsRatio | 12 = Specify a Poissons ratio >= 0 but <= 1 |
| swsBoltConnectorEndEditErrorSpecifyPreloadValue | 14 = Specify a preload value >= 0 |
| swsBoltConnectorEndEditErrorSpecifyTemperatureCoefficient | 11 = Specify a temperature coefficient >= 0 |
| swsBoltConnectorEndEditErrorSpecifyYoungModulus | 10 = Specify a young Modulus > 0 |
| swsBoltConnectorEndEditErrorSuccessful | 0 = Successful |
| swsBoltConnectorEndEditErrorTooManyEntities | 36 = Number of entities specified is greater than the number of entities in the selection box |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
