---
title: "swsThermalComponent_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsThermalComponent_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsThermalComponent_e.html"
---

# swsThermalComponent_e Enumeration

Thermal components

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsThermalComponent_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsThermalComponent_e
```

### C#

```csharp
public enum swsThermalComponent_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsThermalComponent_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsThermalComponentGRADN | 4 = Resultant temperature gradient |
| swsThermalComponentGRADX | 1 = Temperature gradient in the X direction of the selected reference geometry |
| swsThermalComponentGRADY | 2 = Temperature gradient in the Y direction of the selected reference geometry |
| swsThermalComponentGRADZ | 3 = Temperature gradient in the Z direction of the selected reference geometry |
| swsThermalComponentHFLUXN | 8 = Resultant heat flux |
| swsThermalComponentHFLUXX | 5 = Heat flux in the X direction of the selected reference geometry |
| swsThermalComponentHFLUXY | 6 = Heat flux in the Y direction of the selected reference geometry |
| swsThermalComponentHFLUXZ | 7 = Heat flux in the Z direction of the selected reference geometry |
| swsThermalComponentTEMP | 0 = Nodal temperature |

## Remarks

X, Y, Z directions correspond to the reference geometry. The first plane that appears in the FeatureManager tree is used as the default reference geometry.

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
