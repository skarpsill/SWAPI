---
title: "SwDmDesignTableDataError Enumeration"
project: "SOLIDWORKS Document Manager API Help"
interface: "SwDmDesignTableDataError"
member: ""
kind: "enum"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmDesignTableDataError.html"
---

# SwDmDesignTableDataError Enumeration

Design table data errors.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum SwDmDesignTableDataError
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As SwDmDesignTableDataError
```

### C#

```csharp
public enum SwDmDesignTableDataError : System.Enum
```

### C++/CLI

```cpp
public enum class SwDmDesignTableDataError : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDmDesignTableDataError_ExternalTableFound | 0 = The SOLIDWORKS document has an external design table, which is linked to and has been found on disk |
| swDmDesignTableDataError_Fail | 5 = Unknown failure |
| swDmDesignTableDataError_InternalTable | 1 = The SOLIDWORKS document has an internal design table, so there is no external filename |
| swDmDesignTableDataError_NoData | 4 = The SOLIDWORKS document was saved before in a version of SOLIDWORKS earlier than SOLIDWORKS 2009 SP0, so no data is available |
| swDmDesignTableDataError_NoTable | 2 = The SOLIDWORKS document does not have a design table |
| swDMDesigTableDataError_ExternalTableNotFound | 3 = The SOLIDWORKS document has an external design table, but it cannot be found on disk |

## See Also

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
