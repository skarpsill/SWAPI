---
title: "swMoveCopyError_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swMoveCopyError_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMoveCopyError_e.html"
---

# swMoveCopyError_e Enumeration

Move/copy errors.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swMoveCopyError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swMoveCopyError_e
```

### C#

```csharp
public enum swMoveCopyError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swMoveCopyError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swMoveCopyErrorFail | 2 = Failed to create destination directories or copy operation failed possibly because you do not have proper permissions |
| swMoveCopyErrorNone | 0 = Successful |
| swMoveCopyErrorSourceDoesNotExist | 1 = Source file does not exist |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
