---
title: "swsRemoteLoadEndEditError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsRemoteLoadEndEditError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRemoteLoadEndEditError_e.html"
---

# swsRemoteLoadEndEditError_e Enumeration

Remote load editing errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsRemoteLoadEndEditError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsRemoteLoadEndEditError_e
```

### C#

```csharp
public enum swsRemoteLoadEndEditError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsRemoteLoadEndEditError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsRemoteLoadEndEditError_CheckAtleastOneComp | 11 = Select at least one load component |
| swsRemoteLoadEndEditError_DisplacementMustBe0ForTopology | 15 = Displacement components in remote loads in topology studies must be zero |
| swsRemoteLoadEndEditError_EmptyArray | 6 = Empty array |
| swsRemoteLoadEndEditError_EntityAlreadyAdded | 7 = Entity already exists |
| swsRemoteLoadEndEditError_InvalidArray | 5 = Invalid array |
| swsRemoteLoadEndEditError_InvalidConnectionType | 16 = Connection type should be 0 or 1 |
| swsRemoteLoadEndEditError_InvalidForAnalysis | 12 = Only linear static and nonlinear static studies support remote loads with distributed connection types |
| swsRemoteLoadEndEditError_InvalidForNonSolid | 13 = You must select entities on solid bodies for remote loads with distributed connection types |
| swsRemoteLoadEndEditError_InvalidForRigid | 14 = The selections are invalid for a remote load with a rigid connection type |
| swsRemoteLoadEndEditError_InvalidLoadType | 3 = Remote load type is invalid |
| swsRemoteLoadEndEditError_InvalidMass | 10 = Mass should be greater than 0 |
| swsRemoteLoadEndEditError_InvalidMassArray | 9 = Invalid mass array |
| swsRemoteLoadEndEditError_InvalidStudyType | 4 = Study type is invalid for the remote load type |
| swsRemoteLoadEndEditError_InvalidUnits | 8 = Incorrect units |
| swsRemoteLoadEndEditError_NoError | 0 = Success |
| swsRemoteLoadEndEditError_SelectCoordinateSystem | 2 = Select a coordinate system |
| swsRemoteLoadEndEditError_SelectFaceEdgeOrVertex | 1 = Select a face, edge, or vertex |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
