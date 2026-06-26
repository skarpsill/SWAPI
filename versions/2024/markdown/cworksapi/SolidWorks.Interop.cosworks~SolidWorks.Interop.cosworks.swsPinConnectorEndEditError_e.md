---
title: "swsPinConnectorEndEditError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsPinConnectorEndEditError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsPinConnectorEndEditError_e.html"
---

# swsPinConnectorEndEditError_e Enumeration

Pin connector editing errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsPinConnectorEndEditError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsPinConnectorEndEditError_e
```

### C#

```csharp
public enum swsPinConnectorEndEditError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsPinConnectorEndEditError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsPinConnectorEndEditErrorBodyExcludedFromAnalysis | 23 = Selected entity is on a body excluded from analysis |
| swsPinConnectorEndEditErrorEntityAlreadyAdded | 2 = Entity already added |
| swsPinConnectorEndEditErrorHasBeamBody | 11 = Connector has a beam body |
| swsPinConnectorEndEditErrorHasMassElement | 12 = Connection has a mass element |
| swsPinConnectorEndEditErrorIncludeStrengthData | 25 = Select to include strength data |
| swsPinConnectorEndEditErrorIndexTooBig | 10 = Specified index > number of entities |
| swsPinConnectorEndEditErrorInvalidConnectionType | 27 |
| swsPinConnectorEndEditErrorInvalidForAnalysis | 26 |
| swsPinConnectorEndEditErrorNoEntityAtIndex | 1 = No entity at specified index |
| swsPinConnectorEndEditErrorNullEntity | 24 = Entity is null |
| swsPinConnectorEndEditErrorPinBoltStrength | 20 = Specify a positive value for the pin or bolt yield |
| swsPinConnectorEndEditErrorPinMass | 17 = Specify a positive value for the pin mass |
| swsPinConnectorEndEditErrorRadiiNotEqual | 7 = Radii of cylindrical faces of components are not equal |
| swsPinConnectorEndEditErrorSafetyFactor | 21 = Specify a positive value for safety factor |
| swsPinConnectorEndEditErrorSelectAssemblyDocument | 8 = Select assembly document |
| swsPinConnectorEndEditErrorSelectCircularEdge | 22 = Select a circular edge |
| swsPinConnectorEndEditErrorSelectCircularEdges | 13 = Select circular edges on shells |
| swsPinConnectorEndEditErrorSelectConcentricCylindricalFacesConnection | 9 = Select two concentric cylindrical faces from two bodies for pin connector |
| swsPinConnectorEndEditErrorSelectConcentricCylindricalFacesConnector | 6 = Select two concentric cylindrical faces from two bodies for pin connector |
| swsPinConnectorEndEditErrorSelectDifferentBody | 14 = Select a different body for either entity |
| swsPinConnectorEndEditErrorSelectEntity | 3 = Select an entity |
| swsPinConnectorEndEditErrorSelectFace | 4 = Select a face |
| swsPinConnectorEndEditErrorSelectFaceCylindricalSurface | 5 = Select a face with cylindrical surface |
| swsPinConnectorEndEditErrorSelectFacesFromSameHole | 15 = Select the faces that belong to the same hole for the source |
| swsPinConnectorEndEditErrorSpecifyPositiveValue | 16 = Specify a positive value |
| swsPinConnectorEndEditErrorSuccessful | 0 = Successful |
| swsPinConnectorEndEditErrorTensileStressArea | 18 = Specify a positive value for tensile stress area |
| swsPinConnectorEndEditErrorTesileStressAreaLarge | 19 = Tensile stress area is too large |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
