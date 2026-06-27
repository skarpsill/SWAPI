---
title: "swsStrainComponent_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsStrainComponent_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsStrainComponent_e.html"
---

# swsStrainComponent_e Enumeration

Strain components

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsStrainComponent_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsStrainComponent_e
```

### C#

```csharp
public enum swsStrainComponent_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsStrainComponent_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsStrainComponentE1 | 9 = Normal strain in the first principal direction |
| swsStrainComponentE2 | 10 = Normal strain in the second principal direction |
| swsStrainComponentE3 | 11 = Normal strain in the third principal direction |
| swsStrainComponentENERGY | 8 = Total strain energy |
| swsStrainComponentEPSX | 0 = Normal strain in the X direction of the selected reference geometry |
| swsStrainComponentEPSY | 1 = Normal strain in the Y direction of the selected reference geometry |
| swsStrainComponentEPSZ | 2 = Normal strain in the Z direction of the selected reference geometry |
| swsStrainComponentESTRN | 6 = Equivalent strain |
| swsStrainComponentGMXY | 3 = Shear strain in the Y direction in the YZ plane of the selected reference geometry |
| swsStrainComponentGMXZ | 4 = Shear strain in the Z direction in the YZ plane of the selected reference geometry |
| swsStrainComponentGMYZ | 5 = Shear strain in the Z direction in the XZ plane of the selected reference geometry |
| swsStrainComponentSEDENS | 7 = Strain energy density |

## Remarks

X, Y, Z directions correspond to the reference geometry. The first plane that appears in the FeatureManager design tree is used as the default reference geometry.

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
