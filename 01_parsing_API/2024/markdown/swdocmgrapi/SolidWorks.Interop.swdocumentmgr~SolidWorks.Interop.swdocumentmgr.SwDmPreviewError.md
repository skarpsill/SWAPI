---
title: "SwDmPreviewError Enumeration"
project: "SOLIDWORKS Document Manager API Help"
interface: "SwDmPreviewError"
member: ""
kind: "enum"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmPreviewError.html"
---

# SwDmPreviewError Enumeration

Preview errors.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum SwDmPreviewError
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As SwDmPreviewError
```

### C#

```csharp
public enum SwDmPreviewError : System.Enum
```

### C++/CLI

```cpp
public enum class SwDmPreviewError : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDmPreviewErrorFileOpen | 1 = Failed to open the document |
| swDmPreviewErrorMakeBmpFail | 4 = Failed to make the bitmap |
| swDmPreviewErrorNone | 0 = Success |
| swDmPreviewErrorNoPreview | 2 = No preview data stored in document |

## See Also

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
