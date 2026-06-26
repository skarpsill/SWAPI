---
title: "swsStaticResultNodalStressComponentTypes_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsStaticResultNodalStressComponentTypes_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsStaticResultNodalStressComponentTypes_e.html"
---

# swsStaticResultNodalStressComponentTypes_e Enumeration

Nodal stress component types for static study results

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsStaticResultNodalStressComponentTypes_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsStaticResultNodalStressComponentTypes_e
```

### C#

```csharp
public enum swsStaticResultNodalStressComponentTypes_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsStaticResultNodalStressComponentTypes_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsStaticNodalStress_INT | 10 = Stress intensity (P1-P3) |
| swsStaticNodalStress_P1 | 6 = Normal stress in the first principal direction |
| swsStaticNodalStress_P2 | 7 = Normal stress in the second principal direction |
| swsStaticNodalStress_P3 | 8 = Normal stress in the third principal direction |
| swsStaticNodalStress_SX | 0 = Normal stress in the X direction of the selected reference geometry |
| swsStaticNodalStress_SY | 1 = Normal stress in the Y direction of the selected reference geometry |
| swsStaticNodalStress_SZ | 2 = Normal stress in the Z direction of the selected reference geometry |
| swsStaticNodalStress_TRI | 11 = Triaxial stress (P1+P2+P3) |
| swsStaticNodalStress_TXY | 3 = Shear stress in the Y direction on the YZ plane of the selected reference geometry |
| swsStaticNodalStress_TXZ | 4 = Shear stress in the Z direction on the YZ plane of the selected reference geometry |
| swsStaticNodalStress_TYZ | 5 = Shear stress in the Z direction on the XZ plane of the selected reference geometry |
| swsStaticNodalStress_VON | 9 = von Mises stress |

## Remarks

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
