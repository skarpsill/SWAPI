---
title: "swsForceError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsForceError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsForceError_e.html"
---

# swsForceError_e Enumeration

Force errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsForceError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsForceError_e
```

### C#

```csharp
public enum swsForceError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsForceError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsForceErrorApplyNormalForceToFacesAndShellEdges | 3 = You can only apply normal force to faces and shell edges |
| swsForceErrorCannotApplyForce | 10 = Cannot apply the force to the entity used for reference geometry |
| swsForceErrorCannotApplyNonuniformForce | 9 = Nonuniform force cannot be applied to vertices or edges |
| swsForceErrorCannotApplyNonuniformLoadOnMultipleBeam | 18 = Cannot apply nonuniform load on multiple beams |
| swsForceErrorCannotApplyZeroLoading | 19 = Cannot apply zero loading |
| swsForceErrorInvalidArray | 6 = Invalid array |
| swsForceErrorInvalidForceType | 7 = Invalid force type; valid types are 0, 1, and 2 |
| swsForceErrorInvalidSelectionType | 20 = Invalid selection |
| swsForceErrorInvalidStudyType | 5 = Force cannot be applied for this study type |
| swsForceErrorNoEntities | 8 = No entities specified (empty array) |
| swsForceErrorNonUniformBeamLoadInvalidTableData | 21 = Invalid table-driven data for nonuniform loading of a beam |
| swsForceErrorNonUniformBeamLoadInvalidTableDistData | 22 = Invalid table-driven distribution data for nonuniform loading of a beam |
| swsForceErrorSelectFaceEdgePlaneOrAxis | 2 = Select a face, straight edge, plane, or axis for reference geometry |
| swsForceErrorSelectFacesEdgesVerticesOrPoints | 1 = No faces, edges, vertices, or points selected |
| swsForceErrorSelectReferenceAxisOrCylindricalFace | 4 = Select a reference axis or cylindrical face for reference geometry to apply torque |
| swsForceErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
