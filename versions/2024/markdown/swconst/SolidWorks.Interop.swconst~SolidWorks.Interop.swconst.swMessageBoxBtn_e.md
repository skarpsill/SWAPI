---
title: "swMessageBoxBtn_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swMessageBoxBtn_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMessageBoxBtn_e.html"
---

# swMessageBoxBtn_e Enumeration

Message box control buttons.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swMessageBoxBtn_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swMessageBoxBtn_e
```

### C#

```csharp
public enum swMessageBoxBtn_e : System.Enum
```

### C++/CLI

```cpp
public enum class swMessageBoxBtn_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swMbAbortRetryIgnore | 1 = The message box contains three push buttons: Abort, Retry, and Ignore |
| swMbOk | 2 = The message box contains one button, OK |
| swMbOkCancel | 3 = The message box contains two push buttons: OK and Cancel |
| swMbRetryCancel | 4 = The message box contains two push buttons: Retry and Cancel |
| swMbYesNo | 5 = The message box contains two push buttons: Yes and No |
| swMbYesNoCancel | 6 = The message box contains three push buttons: Yes, No, and Cancel |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
