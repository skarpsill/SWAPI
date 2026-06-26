---
title: "swsRemoteLoadType_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsRemoteLoadType_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRemoteLoadType_e.html"
---

# swsRemoteLoadType_e Enumeration

Remote restraint or load types

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsRemoteLoadType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsRemoteLoadType_e
```

### C#

```csharp
public enum swsRemoteLoadType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsRemoteLoadType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsRemoteLoadType_DirectDisplacement | 3 = Connects with rigid bars the remote location, at which translations and rotations are applied, to the center of the selected faces; Available for nonlinear studies only |
| swsRemoteLoadType_DirectLoad | 0 = Transfers the specified remote forces and moments to the selected faces |
| swsRemoteLoadType_RigidDisplacement | 2 = Connects with rigid bars the remote location, at which translations and rotations are applied, to the selected faces, edges, or vertices |
| swsRemoteLoadType_RigidLoadOrMass | 1 = Connects with rigid bars the remote location, at which forces, moments, and/or masses are applied, to the selected faces, edges, or vertices |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
