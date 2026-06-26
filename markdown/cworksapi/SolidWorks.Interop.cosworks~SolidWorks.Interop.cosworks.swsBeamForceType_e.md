---
title: "swsBeamForceType_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsBeamForceType_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsBeamForceType_e.html"
---

# swsBeamForceType_e Enumeration

Beam force types

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsBeamForceType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsBeamForceType_e
```

### C#

```csharp
public enum swsBeamForceType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsBeamForceType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsBeamForceAxial | 0 = Axial force; for trusses, this is the only valid option |
| swsBeamForceMomentDirection1 | 3 = Moment in Dir 1 |
| swsBeamForceMomentDirection2 | 4 = Moment in Dir 2 |
| swsBeamForceShearDirection1 | 1 = Shear force in Dir 1 |
| swsBeamForceShearDirection2 | 2 = Shear force in Dir 2 |
| swsBeamForceTorque | 5 = Torque |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
