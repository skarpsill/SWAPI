---
title: "swsRigidConnectorError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsRigidConnectorError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRigidConnectorError_e.html"
---

# swsRigidConnectorError_e Enumeration

Rigid connector errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsRigidConnectorError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsRigidConnectorError_e
```

### C#

```csharp
public enum swsRigidConnectorError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsRigidConnectorError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsRigidConnectorErrorBodyExcludedFromAnalysis | 14 = Selected entity is on a body excluded from analysis |
| swsRigidConnectorErrorBodyHasRemoteMass | 11 = Select body has a remote mass |
| swsRigidConnectorErrorFacesFromSameComponent | 13 = Faces are from the same component |
| swsRigidConnectorErrorInvalidMesh | 1 = Invalid mesh |
| swsRigidConnectorErrorInvalidSourceArray | 5 = Invalid array for the source |
| swsRigidConnectorErrorInvalidStudy | 3 = Invalid study type |
| swsRigidConnectorErrorInvalidTargetArray | 7 = Invalid array for the target |
| swsRigidConnectorErrorNonlinearStudyPartDocument | 2 = Study type equals nonlinear and document type equals part |
| swsRigidConnectorErrorNoObjectForFace | 6 = No object for the face |
| swsRigidConnectorErrorNoObjectForTarget | 8 = No object for target |
| swsRigidConnectorErrorNullOrEmptyArray | 12 = Array of either entities are NULL or empty |
| swsRigidConnectorErrorSameEntityAtFaceAndTargetArray | 10 = Entity is the same at face and target array |
| swsRigidConnectorErrorSelectAssemblyDocument | 4 = Select assembly document |
| swsRigidConnectorErrorSelectFace | 9 = Select a face |
| swsRigidConnectorErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
