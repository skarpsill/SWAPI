---
title: "swsRigidConnectorEndEditError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsRigidConnectorEndEditError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRigidConnectorEndEditError_e.html"
---

# swsRigidConnectorEndEditError_e Enumeration

Rigid connector editing errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsRigidConnectorEndEditError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsRigidConnectorEndEditError_e
```

### C#

```csharp
public enum swsRigidConnectorEndEditError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsRigidConnectorEndEditError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsRigidConnectorEndEditErrorBodyExcludedFromAnalysis | 9 = Selected entity is on a body excluded from analysis |
| swsRigidConnectorEndEditErrorEntityAlreadyAdded | 2 = Entity already added |
| swsRigidConnectorEndEditErrorFacesOnSameComponent | 8 = Faces are on the same component |
| swsRigidConnectorEndEditErrorHasBeamBody | 6 = Connector has a beam body |
| swsRigidConnectorEndEditErrorHasMassBody | 7 = Connector has a mass body |
| swsRigidConnectorEndEditErrorIndexTooBig | 5 = Specified index > total number of entities |
| swsRigidConnectorEndEditErrorNoEntityAtIndex | 1 = No entity at the specified index |
| swsRigidConnectorEndEditErrorNullEntity | 10 = Entity is NULL |
| swsRigidConnectorEndEditErrorSelectFace | 4 = Select a face |
| swsRigidConnectorEndEditErrorSelectTargetEntityOrFaces | 3 = Either the target entity or the faces has not been selected |
| swsRigidConnectorEndEditErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
