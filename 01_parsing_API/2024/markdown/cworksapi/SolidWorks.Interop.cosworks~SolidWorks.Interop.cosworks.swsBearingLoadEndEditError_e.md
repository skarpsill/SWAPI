---
title: "swsBearingLoadEndEditError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsBearingLoadEndEditError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsBearingLoadEndEditError_e.html"
---

# swsBearingLoadEndEditError_e Enumeration

Bearing load editing errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsBearingLoadEndEditError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsBearingLoadEndEditError_e
```

### C#

```csharp
public enum swsBearingLoadEndEditError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsBearingLoadEndEditError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsBearingLoadEndEditErrorBodyExcludedFromAnalysis | 17 = Selected entity is on a body excluded from analysis |
| swsBearingLoadEndEditErrorCoordinateSystemCylindricalFaces | 1 = Coordinate system and set of cylindrical faces must be the same radii and z axis of coordinate system must be coincident with the axis of the cylindrical faces |
| swsBearingLoadEndEditErrorEntityExists | 3 = Entity already exists |
| swsBearingLoadEndEditErrorHasBeamBody | 9 = Bearing load has a beam body |
| swsBearingLoadEndEditErrorHasMassElement | 8 = Bearing load has a mass element |
| swsBearingLoadEndEditErrorIncorrectOrNullEntity | 2 = Incorrect or NULL entity |
| swsBearingLoadEndEditErrorIndexExceedsNumberOfEntities | 10 = Specified index exceeds the number of entities |
| swsBearingLoadEndEditErrorNoEntity | 11 = No entity |
| swsBearingLoadEndEditErrorNoEntityAtIndex | 5 = No entity at specified index |
| swsBearingLoadEndEditErrorNullEntity | 16 = Entity is NULL |
| swsBearingLoadEndEditErrorSelectFace | 4 = Select a face |
| swsBearingLoadEndEditErrorSelectFaceWithCylindricalSurface | 7 = Select a face with cylindrical surface |
| swsBearingLoadEndEditErrorSelectForceDirection | 13 = Select one force direction |
| swsBearingLoadEndEditErrorSelectOneForceDirection | 12 = Select one force direction, not both force directions |
| swsBearingLoadEndEditErrorSetXDirection | 14 = Set X direction to 0 or 1 |
| swsBearingLoadEndEditErrorSetYDirection | 15 = Set Y direction to 0 or 1 |
| swsBearingLoadEndEditErrorSpecifyValue | 6 = Specify a value > 0 |
| swsBearingLoadEndEditErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
