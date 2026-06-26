---
title: "swsForceEndEditError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsForceEndEditError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsForceEndEditError_e.html"
---

# swsForceEndEditError_e Enumeration

Force editing errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsForceEndEditError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsForceEndEditError_e
```

### C#

```csharp
public enum swsForceEndEditError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsForceEndEditError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsForceEndEditErrorEntityAlreadyExists | 2 = Entity already exists in this object |
| swsForceEndEditErrorMagnitudeForceMustBeLargerZero | 11 = The magnitude of force must be larger than 0 |
| swsForceEndEditErrorNoEntitiesSelected | 3 = No entities selected |
| swsForceEndEditErrorNoEntityAtIndex | 1 = No entity passed at index |
| swsForceEndEditErrorReferenceGeometryEntityNotSelected | 5 = Entity for reference geometry may not be in the list of selected entities |
| swsForceEndEditErrorSelectCoordinateSystem | 8 = Select a coordinate system |
| swsForceEndEditErrorSelectFace | 7 = Select only face for entity |
| swsForceEndEditErrorSelectFaceEdgeOrVertex | 4 = Select face, edge, or vertex for entity |
| swsForceEndEditErrorSelectFaceEdgePlaneOrAxisForReferenceGeometry | 6 = Select face, edge, plane, or axis for reference geometry |
| swsForceEndEditErrorSelectReferenceAxisOrCylindricalFaceForTorque | 10 = Select a reference axis or cylindrical face to apply torque |
| swsForceEndEditErrorSuccessful | 0 = Successful |
| swsForceEndEditErrorVariableForceCannotBeAppliedToVertices | 12 = Variable force cannot be applied to vertices |
| swsForceEndEditErrorVariableForceCannotBeAppliedToVerticesOrEdges | 9 = Variable force cannot be applied to vertices or edges |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
