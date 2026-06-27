---
title: "swsStaticResultNodalStrainComponentTypes_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsStaticResultNodalStrainComponentTypes_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsStaticResultNodalStrainComponentTypes_e.html"
---

# swsStaticResultNodalStrainComponentTypes_e Enumeration

Nodal strain component types for static study results

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsStaticResultNodalStrainComponentTypes_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsStaticResultNodalStrainComponentTypes_e
```

### C#

```csharp
public enum swsStaticResultNodalStrainComponentTypes_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsStaticResultNodalStrainComponentTypes_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsStaticNodalStrain_E1 | 7 = Normal strain in the first principal direction |
| swsStaticNodalStrain_E2 | 8 = Normal strain in the second principal direction |
| swsStaticNodalStrain_E3 | 9 = Normal strain in the third principal direction |
| swsStaticNodalStrain_EPSX | 0 = Normal strain in the X direction of the selected reference geometry |
| swsStaticNodalStrain_EPSY | 1 = Normal strain in the Y direction of the selected reference geometry |
| swsStaticNodalStrain_EPSZ | 2 = Normal strain in the Z direction of the selected reference geometry |
| swsStaticNodalStrain_ESTRN | 6 = Equivalent strain |
| swsStaticNodalStrain_GMXY | 3 = Shear strain in the Y direction on the YZ plane of the selected reference geometry |
| swsStaticNodalStrain_GMXZ | 4 = Shear strain in the Z direction on the YZ plane of the selected reference geometry |
| swsStaticNodalStrain_GMYZ | 5 = Shear strain in the Z direction on the XZ plane of the selected reference geometry |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
