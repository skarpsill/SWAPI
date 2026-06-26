---
title: "swsThermalResultComponentTypes_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsThermalResultComponentTypes_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsThermalResultComponentTypes_e.html"
---

# swsThermalResultComponentTypes_e Enumeration

Component types for thermal study results

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsThermalResultComponentTypes_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsThermalResultComponentTypes_e
```

### C#

```csharp
public enum swsThermalResultComponentTypes_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsThermalResultComponentTypes_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsThermalResultComponentTypes_GRADN | 4 = Resultant temperature gradient |
| swsThermalResultComponentTypes_GRADX | 1 = Temperature gradient in the X direction of the selected reference geometry |
| swsThermalResultComponentTypes_GRADY | 2 = Temperature gradient in the Y direction of the selected reference geometry |
| swsThermalResultComponentTypes_GRADZ | 3 = Temperature gradient in the Z direction of the selected reference geometry |
| swsThermalResultComponentTypes_HFLUXN | 8 = Resultant heat flux |
| swsThermalResultComponentTypes_HFLUXX | 5 = Heat flux in the X direction of the selected reference geometry |
| swsThermalResultComponentTypes_HFLUXY | 6 = Heat flux in the Y direction of the selected reference geometry |
| swsThermalResultComponentTypes_HFLUXZ | 7 = Heat flux in the Z direction of the selected reference geometry |
| swsThermalResultComponentTypes_TEMP | 0 = Nodal temperature |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
