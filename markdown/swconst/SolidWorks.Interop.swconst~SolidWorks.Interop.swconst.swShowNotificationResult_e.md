---
title: "swShowNotificationResult_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swShowNotificationResult_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swShowNotificationResult_e.html"
---

# swShowNotificationResult_e Enumeration

User notification display return values.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swShowNotificationResult_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swShowNotificationResult_e
```

### C#

```csharp
public enum swShowNotificationResult_e : System.Enum
```

### C++/CLI

```cpp
public enum class swShowNotificationResult_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swShowNotificationResult_DontShowAgain | 1 = The user notification is not shown when "Don't show again" is selected |
| swShowNotificationResult_FailedInvalidDefinition | 2 = The user notification could not be displayed due to an invalid definition (e.g., empty title/description) |
| swShowNotificationResult_FailedInvalidHandler | 3 = The user notification could not be desiplayed because the Handler argument is NULL or does not support the expected interface |
| swShowNotificationResult_Shown | 0 = The user notification is shown |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
