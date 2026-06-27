---
title: "SwDmXmlDataError Enumeration"
project: "SOLIDWORKS Document Manager API Help"
interface: "SwDmXmlDataError"
member: ""
kind: "enum"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmXmlDataError.html"
---

# SwDmXmlDataError Enumeration

XML errors.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum SwDmXmlDataError
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As SwDmXmlDataError
```

### C#

```csharp
public enum SwDmXmlDataError : System.Enum
```

### C++/CLI

```cpp
public enum class SwDmXmlDataError : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDmXmlDataErrorFileCreation | 2 = Failed to create file; reason could be related to permissions |
| swDmXmlDataErrorInvalidStorage | 4 = Invalid storage |
| swDmXmlDataErrorNoData | 1 = File was not saved with XML data |
| swDmXmlDataErrorNone | 0 = Success |
| swDmXmlDataErrorStorageOpenFail | 8 = Storage failed to open |

## See Also

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
