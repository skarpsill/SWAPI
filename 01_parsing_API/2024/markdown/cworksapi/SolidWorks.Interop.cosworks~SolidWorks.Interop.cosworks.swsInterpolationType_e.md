---
title: "swsInterpolationType_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsInterpolationType_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsInterpolationType_e.html"
---

# swsInterpolationType_e Enumeration

Types of harmonic frequency interpolations

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsInterpolationType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsInterpolationType_e
```

### C#

```csharp
public enum swsInterpolationType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsInterpolationType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsInterpolationType_Linear | 1 = Linear; solution frequency points are distributed uniformly on the bandwidth |
| swsInterpolationType_Logarithmic | 0 = Logarithmic; solution frequency points are clustered logarithmically around each natural frequency to capture the response accurately at natural frequencies |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
