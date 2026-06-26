---
title: "swCornerType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCornerType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerType_e.html"
---

# swCornerType_e Enumeration

Structure system corner types.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCornerType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCornerType_e
```

### C#

```csharp
public enum swCornerType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCornerType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCorner_Complex | 2 = Three or more members intersect with several trim options |
| swCorner_Simple | 0 = Two members intersect with two trim options |
| swCorner_TwoMember | 1 = Two members intersect with three trim options |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
