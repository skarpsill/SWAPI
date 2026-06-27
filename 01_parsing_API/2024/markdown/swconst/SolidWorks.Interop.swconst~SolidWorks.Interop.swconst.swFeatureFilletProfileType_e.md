---
title: "swFeatureFilletProfileType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swFeatureFilletProfileType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatureFilletProfileType_e.html"
---

# swFeatureFilletProfileType_e Enumeration

Fillet cross-sectional profile shapes.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swFeatureFilletProfileType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swFeatureFilletProfileType_e
```

### C#

```csharp
public enum swFeatureFilletProfileType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swFeatureFilletProfileType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swFeatureFilletCircular | 0 = Circular for symmetric fillets; elliptical for asymmetric fillets |
| swFeatureFilletConicRadius | 2 = Requires that you set the radius of curvature at the shoulder point along the fillet's cross section |
| swFeatureFilletConicRho | 1 = Requires that you set a ratio in the range [0.5, 0.95] which indicates the weight of the cross-section |
| swFeatureFilletConicRhoZeroChamfer | 3 = Chamfer cross section |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
