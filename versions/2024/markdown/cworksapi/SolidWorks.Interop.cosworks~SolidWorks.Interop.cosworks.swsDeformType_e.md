---
title: "swsDeformType_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsDeformType_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDeformType_e.html"
---

# swsDeformType_e Enumeration

Deform types

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsDeformType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsDeformType_e
```

### C#

```csharp
public enum swsDeformType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsDeformType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsAutomatic | 0 = Displays the deformed shape of the model using the default scale factor that the program uses to scale the largest deformation to 10% of the largest dimension of the smallest box that surrounds the model |
| swsTrueScale | 1 = Displays the actual deformed shape of the model; scale factor is 1.0 |
| swsUserDefined | 2 = Allows you to specify a custom scale factor |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
