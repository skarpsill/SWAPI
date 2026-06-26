---
title: "swsPinConnectorError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsPinConnectorError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsPinConnectorError_e.html"
---

# swsPinConnectorError_e Enumeration

Pin connector errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsPinConnectorError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsPinConnectorError_e
```

### C#

```csharp
public enum swsPinConnectorError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsPinConnectorError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsPinConnectorErrorArrayEmtpy | 16 = Array has an empty dispatch |
| swsPinConnectorErrorArrayHasBeamBody | 17 = Array has a beam body |
| swsPinConnectorErrorBodyExcludedFromAnalysis | 20 = Selected entity is on a body excluded from analysis |
| swsPinConnectorErrorComponentConcentricFacesRadiiNotEqual | 8 = Radii of cylindrical faces of component are not equal |
| swsPinConnectorErrorEntitySameForComponents | 14 = Entity is same in first and second components |
| swsPinConnectorErrorFaceNotCylindrical | 6 = Select faces does not have a cylindrical surface |
| swsPinConnectorErrorInvalidArray | 9 = Invalid array |
| swsPinConnectorErrorInvalidMesh | 1 = Invalid mesh type |
| swsPinConnectorErrorInvalidStudy | 3 = Invalid study type |
| swsPinConnectorErrorNonlinearStudyPartDocument | 2 = Study type equals nonlinear and document type equals part |
| swsPinConnectorErrorNoObject | 4 = No object in array |
| swsPinConnectorErrorNullOrEmptyArray | 13 = Array of either entities is NULL or empty |
| swsPinConnectorErrorSelectAssemblyDocument | 10 = Select an assembly document |
| swsPinConnectorErrorSelectCircularEdgesOnShells | 19 = Select circular edges on shells |
| swsPinConnectorErrorSelectConcentricCylindricalFacesForConnection | 18 = Select two concentric cylindrical faces from two bodies for pin connection |
| swsPinConnectorErrorSelectConcentricCylindricalFacesForConnector | 7 = Select two concentric cylindrical faces from two bodies for pin connector |
| swsPinConnectorErrorSelectDifferentBody | 15 = Select different body |
| swsPinConnectorErrorSelectFace | 5 = Select a face |
| swsPinConnectorErrorSelectFaceFromSameHoleForTarget | 12 = Select the face that belongs to the same hole for the target |
| swsPinConnectorErrorSelectFacesFromSameHoleForSource | 11 = Select the faces that belong to the same hole for the source |
| swsPinConnectorErrorSuccesful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
