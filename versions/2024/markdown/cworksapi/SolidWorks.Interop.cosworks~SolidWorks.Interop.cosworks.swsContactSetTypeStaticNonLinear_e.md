---
title: "swsContactSetTypeStaticNonLinear_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsContactSetTypeStaticNonLinear_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetTypeStaticNonLinear_e.html"
---

# swsContactSetTypeStaticNonLinear_e Enumeration

Contact set types for static and nonlinear studies

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsContactSetTypeStaticNonLinear_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsContactSetTypeStaticNonLinear_e
```

### C#

```csharp
public enum swsContactSetTypeStaticNonLinear_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsContactSetTypeStaticNonLinear_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsContactSetTypeStaticNonLinearBonded | 1 = Bonded |
| swsContactSetTypeStaticNonLinearFree | 3 = Free (no interaction) |
| swsContactSetTypeStaticNonLinearNoPenetration | 0 = No penetration |
| swsContactSetTypeStaticNonLinearShrinkFit | 2 = Shrink fit |
| swsContactSetTypeStaticNonLinearVirtualWall | 4 = Virtual wall (for static studies only) |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
