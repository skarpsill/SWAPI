---
title: "swsContactType_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsContactType_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactType_e.html"
---

# swsContactType_e Enumeration

Contact types

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsContactType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsContactType_e
```

### C#

```csharp
public enum swsContactType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsContactType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsContactTypeAllowPenetration | 1 = Allow penetration for static, nonlinear, buckling, and frequency studies |
| swsContactTypeBonded | 0 = Bonded (no clearance) for static, nonlinear, buckling, thermal, and frequency studies |
| swsContactTypeFreeOrInsulated | 1 = Free (no interaction) for static, nonlinear, buckling, and frequency studies; insulated for thermal studies |
| swsContactTypeStaticNoPenetration | 2 = No penetration for static and nonlinear studies |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
