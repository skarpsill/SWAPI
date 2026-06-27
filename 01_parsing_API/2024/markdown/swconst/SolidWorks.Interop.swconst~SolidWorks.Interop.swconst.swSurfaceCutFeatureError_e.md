---
title: "swSurfaceCutFeatureError_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swSurfaceCutFeatureError_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSurfaceCutFeatureError_e.html"
---

# swSurfaceCutFeatureError_e Enumeration

Types of surface-cut errors.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swSurfaceCutFeatureError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swSurfaceCutFeatureError_e
```

### C#

```csharp
public enum swSurfaceCutFeatureError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swSurfaceCutFeatureError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swSurfaceCutFeatureError_BodiesNotSpecified | 1 = No bodies specified to cut |
| swSurfaceCutFeatureError_InvalidVariant | 2 = Array passed to IFeatureManager::InsertCutSurface must contain only body objects |
| swSurfaceCutFeatureError_NoError | 0 = No error |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
