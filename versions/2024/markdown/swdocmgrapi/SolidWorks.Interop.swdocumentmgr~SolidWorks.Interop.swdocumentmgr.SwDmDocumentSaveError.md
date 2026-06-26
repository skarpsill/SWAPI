---
title: "SwDmDocumentSaveError Enumeration"
project: "SOLIDWORKS Document Manager API Help"
interface: "SwDmDocumentSaveError"
member: ""
kind: "enum"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmDocumentSaveError.html"
---

# SwDmDocumentSaveError Enumeration

Document save errors.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum SwDmDocumentSaveError
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As SwDmDocumentSaveError
```

### C#

```csharp
public enum SwDmDocumentSaveError : System.Enum
```

### C++/CLI

```cpp
public enum class SwDmDocumentSaveError : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDmDocumentSaveErrorFail | 2 = Failed; reason could be related to permissions |
| swDmDocumentSaveErrorNone | 0 = Saved successfully |
| swDmDocumentSaveErrorReadOnly | 1 = Failed; file was opened as read-only |

## See Also

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
