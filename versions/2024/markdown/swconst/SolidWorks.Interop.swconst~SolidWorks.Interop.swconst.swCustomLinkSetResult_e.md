---
title: "swCustomLinkSetResult_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCustomLinkSetResult_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCustomLinkSetResult_e.html"
---

# swCustomLinkSetResult_e Enumeration

Error codes when linking and unlinking custom properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCustomLinkSetResult_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCustomLinkSetResult_e
```

### C#

```csharp
public enum swCustomLinkSetResult_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCustomLinkSetResult_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCustomLinkSetResult_Legacy | 2 = Legacy custom properties cannot be linked or unlinked |
| swCustomLinkSetResult_NotPresent | 1 = Custom property does not exist |
| swCustomLinkSetResult_OK | 0 = Success |
| swCustomLinkSetResult_UserProp | 3 = User-defined custom properties cannot be linked or unlinked |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
