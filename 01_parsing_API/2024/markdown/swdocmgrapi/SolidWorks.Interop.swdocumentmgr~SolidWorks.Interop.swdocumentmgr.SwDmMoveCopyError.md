---
title: "SwDmMoveCopyError Enumeration"
project: "SOLIDWORKS Document Manager API Help"
interface: "SwDmMoveCopyError"
member: ""
kind: "enum"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmMoveCopyError.html"
---

# SwDmMoveCopyError Enumeration

Move/copy errors.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum SwDmMoveCopyError
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As SwDmMoveCopyError
```

### C#

```csharp
public enum SwDmMoveCopyError : System.Enum
```

### C++/CLI

```cpp
public enum class SwDmMoveCopyError : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDmMoveCopyErrorFail | 2 = Failed to create destination directories or copy operation failed due to problems possibly related to permissions |
| swDmMoveCopyErrorNone | 0 =Success |
| swDmMoveCopyErrorSourceDoesNotExist | 1 = Source file does not exist |

## See Also

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
