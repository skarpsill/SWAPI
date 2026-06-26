---
title: "swUpdateProgressError_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swUpdateProgressError_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUpdateProgressError_e.html"
---

# swUpdateProgressError_e Enumeration

User progress errors.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swUpdateProgressError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swUpdateProgressError_e
```

### C#

```csharp
public enum swUpdateProgressError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swUpdateProgressError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swUpdateProgressError_NotInitialized | 4 |
| swUpdateProgressError_OutOfBounds | 3 |
| swUpdateProgressError_Success | 1 |
| swUpdateProgressError_UnknownError | 0 |
| swUpdateProgressError_UserCancel | 2 = User pressed the Esc key to cancel the progress indicator |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
