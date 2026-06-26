---
title: "swRotationAxisIndex_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swRotationAxisIndex_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRotationAxisIndex_e.html"
---

# swRotationAxisIndex_e Enumeration

Rotation ring manipulator options when creating or editing an explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swRotationAxisIndex_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swRotationAxisIndex_e
```

### C#

```csharp
public enum swRotationAxisIndex_e : System.Enum
```

### C++/CLI

```cpp
public enum class swRotationAxisIndex_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swRotationAxisIndex_Unknown | -1 = Use in IExplodeStep::SetRotationAxis to continue using the current enumerator value |
| swRotationAxisIndex_XYRing | 0 |
| swRotationAxisIndex_YZRing | 1 |
| swRotationAxisIndex_ZXRing | 2 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
