---
title: "swsStaticResultElementalStressComponentTypes_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsStaticResultElementalStressComponentTypes_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsStaticResultElementalStressComponentTypes_e.html"
---

# swsStaticResultElementalStressComponentTypes_e Enumeration

Elemental stress component types for static study results

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsStaticResultElementalStressComponentTypes_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsStaticResultElementalStressComponentTypes_e
```

### C#

```csharp
public enum swsStaticResultElementalStressComponentTypes_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsStaticResultElementalStressComponentTypes_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsStaticElementalStress_CONTACTPRESS | 12 = Contact Pressure |
| swsStaticElementalStress_ERR | 11 = Energy Norm Error |
| swsStaticElementalStress_INT | 10 = Stress intensity (P1-P3) |
| swsStaticElementalStress_P1 | 6 = Normal stress in the first principal direction |
| swsStaticElementalStress_P2 | 7 = Normal stress in the second principal direction |
| swsStaticElementalStress_P3 | 8 = Normal stress in the third principal direction |
| swsStaticElementalStress_SX | 0 = Normal stress in the X direction of the selected reference geometry |
| swsStaticElementalStress_SY | 1 = Normal stress in the Y direction of the selected reference geometry |
| swsStaticElementalStress_SZ | 2 = Normal stress in the Z direction of the selected reference geometry |
| swsStaticElementalStress_TRI | 11 = Triaxial stress (P1+P2+P3) |
| swsStaticElementalStress_TXY | 3 = Shear stress in the Y direction on the YZ plane of the selected reference geometry |
| swsStaticElementalStress_TXZ | 4 = Shear stress in the Z direction on the YZ plane of the selected reference geometry |
| swsStaticElementalStress_TYZ | 5 = Shear stress in the Z direction on the XZ plane of the selected reference geometry |
| swsStaticElementalStress_VON | 9 = von Mises stress |

## Remarks

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
