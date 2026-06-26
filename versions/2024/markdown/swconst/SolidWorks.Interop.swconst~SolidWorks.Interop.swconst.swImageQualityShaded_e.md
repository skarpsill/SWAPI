---
title: "swImageQualityShaded_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swImageQualityShaded_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swImageQualityShaded_e.html"
---

# swImageQualityShaded_e Enumeration

Quality of tessellation of cylindrical surfaces for shaded rendering output.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swImageQualityShaded_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swImageQualityShaded_e
```

### C#

```csharp
public enum swImageQualityShaded_e : System.Enum
```

### C++/CLI

```cpp
public enum class swImageQualityShaded_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swShadedImageQualityCoarse | 1 |
| swShadedImageQualityCustom | 3 = Use swUserPreferenceDoubleValue_e.swImageQualityShadedDeviation to set a value for the custom shaded image quality. |
| swShadedImageQualityFine | 2 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
