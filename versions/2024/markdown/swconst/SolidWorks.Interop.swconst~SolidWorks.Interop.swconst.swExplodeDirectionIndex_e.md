---
title: "swExplodeDirectionIndex_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swExplodeDirectionIndex_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swExplodeDirectionIndex_e.html"
---

# swExplodeDirectionIndex_e Enumeration

Explode direction manipulator options when creating or editing an explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swExplodeDirectionIndex_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swExplodeDirectionIndex_e
```

### C#

```csharp
public enum swExplodeDirectionIndex_e : System.Enum
```

### C++/CLI

```cpp
public enum class swExplodeDirectionIndex_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swExplodeDirectionIndex_Unknown | -1 = Use in IExplodeStep::SetExplodeDirection to continue using the current enumerator value |
| swExplodeDirectionIndex_XAxis | 0 |
| swExplodeDirectionIndex_YAxis | 1 |
| swExplodeDirectionIndex_ZAxis | 2 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
