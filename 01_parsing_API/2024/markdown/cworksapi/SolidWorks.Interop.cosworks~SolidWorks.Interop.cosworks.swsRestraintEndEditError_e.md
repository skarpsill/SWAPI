---
title: "swsRestraintEndEditError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsRestraintEndEditError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRestraintEndEditError_e.html"
---

# swsRestraintEndEditError_e Enumeration

Restraint editing errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsRestraintEndEditError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsRestraintEndEditError_e
```

### C#

```csharp
public enum swsRestraintEndEditError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsRestraintEndEditError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsRestraintEndEditErrorCannotRestrainRefGeometryEntity | 14 = Entity for reference geometry cannot be in list of entities to be restrained |
| swsRestraintEndEditErrorCyclicSymmetryRestraint | 10 = Cyclic symmetry restraint is valid only for solid meshes |
| swsRestraintEndEditErrorDefineDisplacementComponent | 13 = Define at least one displacement component |
| swsRestraintEndEditErrorEntityExists | 2 = Entity already exists in this restraint |
| swsRestraintEndEditErrorNoEntity | 3 = No entity specified |
| swsRestraintEndEditErrorNoIndex | 1 = No entity at specified index |
| swsRestraintEndEditErrorSelectAxis | 12 = Select axis as reference geometry |
| swsRestraintEndEditErrorSelectCylindricalFaces | 6 = Select cylindrical faces |
| swsRestraintEndEditErrorSelectFaceEdgeOrVertices | 4 = Select face, edge or vertices |
| swsRestraintEndEditErrorSelectFaceEdgeVertexOrFaces | 8 = Select face, edge, vertex, or faces |
| swsRestraintEndEditErrorSelectFaces | 5 = Select faces |
| swsRestraintEndEditErrorSelectPlaneAxisEdgeFaceOrCylinder | 9 = Select reference plane, axis, edge, planar face, or cylinder for reference |
| swsRestraintEndEditErrorSelectSphericalFaces | 7 = Select spherical faces |
| swsRestraintEndEditErrorSelectTwoFaces | 11 = Select only two faces for cyclic symmetry |
| swsRestraintEndEditErrorSuccess | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
