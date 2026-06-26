---
title: "swAnimationPlayMode_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swAnimationPlayMode_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAnimationPlayMode_e.html"
---

# swAnimationPlayMode_e Enumeration

Modes to play animations.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swAnimationPlayMode_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swAnimationPlayMode_e
```

### C#

```csharp
public enum swAnimationPlayMode_e : System.Enum
```

### C++/CLI

```cpp
public enum class swAnimationPlayMode_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAnimationPlayModeLoop | 2 = Play from beginning to end, from beginning to end, etc. |
| swAnimationPlayModeNormal | 1 = Play from beginning to end once. |
| swAnimationPlayModeReciprocate | 3 = Play from beginning to end, from end to beginning, beginning to end, etc. |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
