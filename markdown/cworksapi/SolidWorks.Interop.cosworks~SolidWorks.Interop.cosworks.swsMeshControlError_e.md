---
title: "swsMeshControlError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsMeshControlError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMeshControlError_e.html"
---

# swsMeshControlError_e Enumeration

Mesh control errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsMeshControlError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsMeshControlError_e
```

### C#

```csharp
public enum swsMeshControlError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsMeshControlError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsMeshControlErrorElementSize | 6 = Specify a number between 0.0000001 and 1000000 for element size |
| swsMeshControlErrorEntityAlreadyExists | 2 = Entity already exists in this mesh control |
| swsMeshControlErrorNoEntities | 3 = No entities selected |
| swsMeshControlErrorNoEntityAtIndex | 1 = No entity is passed at index |
| swsMeshControlErrorNumberOfLayers | 7 = Number of layers must be an integer larger than 0 and less than or equal to 80 |
| swsMeshControlErrorSelectFaceEdgeOrVertex | 5 = Select face, edge, or vertex |
| swsMeshControlErrorSelectVerticesEdgesFacesBodiesOrComponents | 4 = Select vertices, edges, faces, bodies, or components |
| swsMeshControlErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
