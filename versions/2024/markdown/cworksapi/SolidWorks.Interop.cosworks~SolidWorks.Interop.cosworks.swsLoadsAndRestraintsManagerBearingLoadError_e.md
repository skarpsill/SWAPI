---
title: "swsLoadsAndRestraintsManagerBearingLoadError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsLoadsAndRestraintsManagerBearingLoadError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLoadsAndRestraintsManagerBearingLoadError_e.html"
---

# swsLoadsAndRestraintsManagerBearingLoadError_e Enumeration

Bearing load errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsLoadsAndRestraintsManagerBearingLoadError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsLoadsAndRestraintsManagerBearingLoadError_e
```

### C#

```csharp
public enum swsLoadsAndRestraintsManagerBearingLoadError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsLoadsAndRestraintsManagerBearingLoadError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsLoadsAndRestraintsManagerBearingLoadErrorBodyExcludedFromAnalysis | 9 = Selected entity is on a body excluded from analysis |
| swsLoadsAndRestraintsManagerBearingLoadErrorCoordinateSystemAndCylindricalFaces | 6 = Coordinate system and set of cylindrical faces must be the same radii and z axis of coordinate system must be coincident with the axis of the cylindrical faces |
| swsLoadsAndRestraintsManagerBearingLoadErrorCoordinateSystemEmpty | 3 = Coordinate system is empty |
| swsLoadsAndRestraintsManagerBearingLoadErrorInvalidArray | 1 = Invalid array |
| swsLoadsAndRestraintsManagerBearingLoadErrorInvalidMesh | 7 = Invalid mesh type |
| swsLoadsAndRestraintsManagerBearingLoadErrorInvalidStudy | 8 = Invalid study type |
| swsLoadsAndRestraintsManagerBearingLoadErrorNoObjectForFace | 2 = No object for the face |
| swsLoadsAndRestraintsManagerBearingLoadErrorSelectCoordinateSystem | 5 = Select a coordinate system |
| swsLoadsAndRestraintsManagerBearingLoadErrorSelectFace | 4 = Select a face |
| swsLoadsAndRestraintsManagerBearingLoadErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
