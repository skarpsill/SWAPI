---
title: "swPartingLineFeatureStatus_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swPartingLineFeatureStatus_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPartingLineFeatureStatus_e.html"
---

# swPartingLineFeatureStatus_e Enumeration

Statuses of parting line features.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swPartingLineFeatureStatus_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swPartingLineFeatureStatus_e
```

### C#

```csharp
public enum swPartingLineFeatureStatus_e : System.Enum
```

### C++/CLI

```cpp
public enum class swPartingLineFeatureStatus_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| STATUS_MOLD_PARTINGLINE_EDGES_OPEN | 2 = Select edges that form a closed loop |
| STATUS_MOLD_PARTINGLINE_NON_SEPARABLE | 4 = The parting line is complete, but the mold cannot be separated into core and cavity; you might need to create shut-off surfaces |
| STATUS_MOLD_PARTINGLINE_SEPARABLE | 3 = The parting line is complete; the mold can be separated into core and cavity |
| STATUS_MOLD_REDUNDANT_EDGES | 1 = There are more than enough edges selected to form a parting line; remove any redundant edges or add edges to close gaps between disjoint edge chains |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
