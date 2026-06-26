---
title: "swsBeamStressType_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsBeamStressType_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsBeamStressType_e.html"
---

# swsBeamStressType_e Enumeration

Beam stress types

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsBeamStressType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsBeamStressType_e
```

### C#

```csharp
public enum swsBeamStressType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsBeamStressType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsBeamStressAxial | 0 = Uniform axial stress |
| swsBeamStressBendingDirection1 | 1 = Bending stress in Dir 1 |
| swsBeamStressBendingDirection2 | 2 = Bending stress in Dir 2 |
| swsBeamStressTorsional | 3 = Torsional stress |
| swsBeamStressWorstCase | 4 = Axial and bending stresses at the extreme fibers of the cross-section |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
