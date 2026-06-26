---
title: "swsIncompatibleBondingOption_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsIncompatibleBondingOption_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsIncompatibleBondingOption_e.html"
---

# swsIncompatibleBondingOption_e Enumeration

Bonding contact methods for analyzing models that contain contacting surfaces with incompatible meshes

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsIncompatibleBondingOption_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsIncompatibleBondingOption_e
```

### C#

```csharp
public enum swsIncompatibleBondingOption_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsIncompatibleBondingOption_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsIncompatibleBondingOption_Automatic | 0 = Automatic; let solver automatically switch from surface-based bonding contact to node-based bonding contact, if surface-based bonding contact slows down solution convergence |
| swsIncompatibleBondingOption_MoreAccurate | 2 = More accurate (slower); use surface-based bonding contact method to produce continuous and more accurate stresses in contact regions |
| swsIncompatibleBondingOption_Simplified | 1 = Simplified; use node-based bonding contact method on models with extensive contact surfaces to quickly reach solution convergence |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
