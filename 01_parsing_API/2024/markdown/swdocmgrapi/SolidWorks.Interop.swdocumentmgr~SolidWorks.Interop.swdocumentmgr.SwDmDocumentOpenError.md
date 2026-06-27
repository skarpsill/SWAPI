---
title: "SwDmDocumentOpenError Enumeration"
project: "SOLIDWORKS Document Manager API Help"
interface: "SwDmDocumentOpenError"
member: ""
kind: "enum"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmDocumentOpenError.html"
---

# SwDmDocumentOpenError Enumeration

Document open errors.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum SwDmDocumentOpenError
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As SwDmDocumentOpenError
```

### C#

```csharp
public enum SwDmDocumentOpenError : System.Enum
```

### C++/CLI

```cpp
public enum class SwDmDocumentOpenError : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDmDocumentOpenErrorFail | 1 = File failed to open; reasons could be related to permissions or the file is in use by some other application or the file does not exist |
| swDmDocumentOpenErrorFileNotFound | 3 = File not found |
| swDmDocumentOpenErrorFileReadOnly | 4 = File is read only |
| swDmDocumentOpenErrorFutureVersion | 6 = File was created in a version of SOLIDWORKS more recent than the SOLIDWORKS Document Manager version attempting to open the file; you need to install a later version of SOLIDWORKS Document Manager; see ISwDMApplication::GetLatestSupportedFileVersion |
| swDmDocumentOpenErrorNoLicense | 5 = No valid SOLIDWORKS Document Manager API license; the file may have been saved in a later version of SOLIDWORKS to which your license key does not allow access; see License Key section of Getting Started |
| swDmDocumentOpenErrorNone | 0 = File successfully opened |
| swDmDocumentOpenErrorNonSW | 2 = Non-SOLIDWORKS file was opened |

## See Also

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
