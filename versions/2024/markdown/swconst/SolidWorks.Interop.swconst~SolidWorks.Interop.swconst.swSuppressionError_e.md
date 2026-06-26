---
title: "swSuppressionError_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swSuppressionError_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSuppressionError_e.html"
---

# swSuppressionError_e Enumeration

Suppression errors.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swSuppressionError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swSuppressionError_e
```

### C#

```csharp
public enum swSuppressionError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swSuppressionError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swSuppressionBadComponent | 0 = Component object is no longer valid; for example, if a configuration changed |
| swSuppressionBadState | 1 = Invalid state was specified |
| swSuppressionChangeFailed | 3 = Change failed, even though the arguments were okay |
| swSuppressionChangeOk | 2 = State was changed |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
