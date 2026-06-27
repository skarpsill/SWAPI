---
title: "swsStressComponent_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsStressComponent_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsStressComponent_e.html"
---

# swsStressComponent_e Enumeration

Stress components

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsStressComponent_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsStressComponent_e
```

### C#

```csharp
public enum swsStressComponent_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsStressComponent_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsStressComponentCP | 12 = Contact Pressure |
| swsStressComponentERR | 11 = Energy Norm Error |
| swsStressComponentINT | 10 = Stress intensity (P1-P3) |
| swsStressComponentP1 | 6 = Normal stress in the first principal direction |
| swsStressComponentP2 | 7 = Normal stress in the second principal direction |
| swsStressComponentP3 | 8 = Normal stress in the third principal direction |
| swsStressComponentSX | 0 = Normal stress in the X direction of the selected reference geometry |
| swsStressComponentSY | 1 = Normal stress in the Y direction of the selected reference geometry |
| swsStressComponentSZ | 2 = Normal stress in the Z direction of the selected reference geometry |
| swsStressComponentTRI | 13 = Triaxial stress (P1+P2+P3) |
| swsStressComponentTXY | 3 = Shear stress in the Y direction acting in the YZ plane of the selected reference geometry |
| swsStressComponentTXZ | 4 = Shear stress in the Z direction acting in the YZ plane of the selected reference geometry |
| swsStressComponentTYZ | 5 = Shear stress in the Z direction acting in the XZ plane of the selected reference geometry |
| swsStressComponentVON | 9 = von Mises stress |
| swsStressComponentVONDC | 100 = Directional von Mises stress; valid only for NComponent of ICWResults::GetMinMaxStressForHarmonic |

## Remarks

X, Y, Z directions correspond to the reference geometry. The first plane that appears in the FeatureManager design tree is used as the default reference geometry.

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
