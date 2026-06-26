---
title: "swRebuildOnActivation_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swRebuildOnActivation_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRebuildOnActivation_e.html"
---

# swRebuildOnActivation_e Enumeration

Rebuild options during document activation.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swRebuildOnActivation_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swRebuildOnActivation_e
```

### C#

```csharp
public enum swRebuildOnActivation_e : System.Enum
```

### C++/CLI

```cpp
public enum class swRebuildOnActivation_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDontRebuildActiveDoc | 1 = do not rebuild the activated document |
| swRebuildActiveDoc | 2 = rebuild the activated document |
| swUserDecision | 0 = prompt the user whether to rebuild the activated document |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
