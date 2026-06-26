---
title: "swShowMessageBarResult_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swShowMessageBarResult_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swShowMessageBarResult_e.html"
---

# swShowMessageBarResult_e Enumeration

Message bar display result codes.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swShowMessageBarResult_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swShowMessageBarResult_e
```

### C#

```csharp
public enum swShowMessageBarResult_e : System.Enum
```

### C++/CLI

```cpp
public enum class swShowMessageBarResult_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swShowMessageBarResult_DontShowAgain | 1 = The message bar is not shown when "Don't show again" is selected |
| swShowMessageBarResult_FailedInvalidDefinition | 2 = The message bar could not be displayed due to an invalid definition (e.g., empty title/description) |
| swShowMessageBarResult_FailedInvalidHandler | 3 = The message bar could not be desiplayed because the Handler argument is NULL or does not support the expected interface |
| swShowMessageBarResult_Shown | 0 = The modeless message bar is shown |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
