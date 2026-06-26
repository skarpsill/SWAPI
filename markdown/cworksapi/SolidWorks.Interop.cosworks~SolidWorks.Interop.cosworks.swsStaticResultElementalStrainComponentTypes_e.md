---
title: "swsStaticResultElementalStrainComponentTypes_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsStaticResultElementalStrainComponentTypes_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsStaticResultElementalStrainComponentTypes_e.html"
---

# swsStaticResultElementalStrainComponentTypes_e Enumeration

Elemental strain component types for static study results

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsStaticResultElementalStrainComponentTypes_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsStaticResultElementalStrainComponentTypes_e
```

### C#

```csharp
public enum swsStaticResultElementalStrainComponentTypes_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsStaticResultElementalStrainComponentTypes_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsStaticElementalStrain_E1 | 9 = Normal strain in the first principal direction |
| swsStaticElementalStrain_E2 | 10 = Normal strain in the second principal direction |
| swsStaticElementalStrain_E3 | 11 = Normal strain in the third principal direction |
| swsStaticElementalStrain_ENERGY | 8 = Total strain energy |
| swsStaticElementalStrain_EPSX | 0 = Normal strain in the X direction of the selected reference geometry |
| swsStaticElementalStrain_EPSY | 1 = Normal strain in the Y direction of the selected reference geometry |
| swsStaticElementalStrain_EPSZ | 2 = Normal strain in the Z direction of the selected reference geometry |
| swsStaticElementalStrain_ESTRN | 6 = Equivalent strain |
| swsStaticElementalStrain_GMXY | 3 = Shear strain in the Y direction on the YZ plane of the selected reference geometry |
| swsStaticElementalStrain_GMXZ | 4 = Shear strain in the Z direction on the YZ plane of the selected reference geometry |
| swsStaticElementalStrain_GMYZ | 5 = Shear strain in the Z direction on the XZ plane of the selected reference geometry |
| swsStaticElementalStrain_SEDENS | 7 = Strain energy density |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
