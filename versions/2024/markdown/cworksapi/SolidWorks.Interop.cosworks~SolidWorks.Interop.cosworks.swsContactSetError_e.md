---
title: "swsContactSetError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsContactSetError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetError_e.html"
---

# swsContactSetError_e Enumeration

Contact set errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsContactSetError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsContactSetError_e
```

### C#

```csharp
public enum swsContactSetError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsContactSetError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsContactSetErrorBondedContactForTouchingFaces | 10 = Bonded contact for drop test studies is only allowed for touching faces |
| swsContactSetErrorCannotCreateContactPair | 12 = Contact pair cannot be created for this study type |
| swsContactSetErrorFaceForSourceAndTarget | 7 = At least one face is specified for both source and target |
| swsContactSetErrorInvalidArray | 1 = Invalid array |
| swsContactSetErrorInvalidType | 3 = Invalid contact set type |
| swsContactSetErrorNoEntities | 2 = No entities specified (empty array) |
| swsContactSetErrorSelectOneTargetPlane | 5 = Specify faces, edges, or vertices for source |
| swsContactSetErrorSelectOnlyFaces | 6 = Only faces can be selected for target |
| swsContactSetErrorShrinkFitNeedsIntereference | 11 = Shrink fit requires that source and target bodies interfere |
| swsContactSetErrorSourceTargetFacesMustTouch | 9 = Node to node contact requires that source and target faces touch |
| swsContactSetErrorSpecifyFacesEdgesOrVertices | 4 = Specify faces, edges, or vertices for source |
| swsContactSetErrorSuccess | 0 = Successful |
| swsContactSetErrorVerticesEdgesForBondingSurfaceContacts | 8 = Vertices and edges are allowed in source entities only for bonding and surface contact conditions |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
