---
title: "swTesselationMatchType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swTesselationMatchType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTesselationMatchType_e.html"
---

# swTesselationMatchType_e Enumeration

Tessellation match types.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swTesselationMatchType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swTesselationMatchType_e
```

### C#

```csharp
public enum swTesselationMatchType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swTesselationMatchType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swTesselationMatchEdgeCurve | 2 = Clipping facet boundaries to model edge curves |
| swTesselationMatchFacetGeometry | 1 = Clipping facet boundaries to a common edge |
| swTesselationMatchFacetTopology | 0 = Matching facet vertices across a common edge |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
