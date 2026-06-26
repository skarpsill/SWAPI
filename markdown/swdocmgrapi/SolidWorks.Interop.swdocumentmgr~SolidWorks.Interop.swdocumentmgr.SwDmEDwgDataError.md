---
title: "SwDmEDwgDataError Enumeration"
project: "SOLIDWORKS Document Manager API Help"
interface: "SwDmEDwgDataError"
member: ""
kind: "enum"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmEDwgDataError.html"
---

# SwDmEDwgDataError Enumeration

eDrawings data errors.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum SwDmEDwgDataError
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As SwDmEDwgDataError
```

### C#

```csharp
public enum SwDmEDwgDataError : System.Enum
```

### C++/CLI

```cpp
public enum class SwDmEDwgDataError : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDmEDwgDataErrorFileCreation | 2 = Failed to create eDrawings file, possibly because of permissions |
| swDmEDwgDataErrorInvalidStorage | 4 = Invalid storage |
| swDmEDwgDataErrorNoData | 1 = File was not saved with eDrawings data |
| swDmEDwgDataErrorNone | 0 = Success |

## See Also

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
