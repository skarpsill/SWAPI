---
title: "swDmExcludeFromBOMResult Enumeration"
project: "SOLIDWORKS Document Manager API Help"
interface: "swDmExcludeFromBOMResult"
member: ""
kind: "enum"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmExcludeFromBOMResult.html"
---

# swDmExcludeFromBOMResult Enumeration

Bill of materials (BOM) components exclusion options.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swDmExcludeFromBOMResult
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swDmExcludeFromBOMResult
```

### C#

```csharp
public enum swDmExcludeFromBOMResult : System.Enum
```

### C++/CLI

```cpp
public enum class swDmExcludeFromBOMResult : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDmExcludeFromBOM_FALSE | 0 = Do not exclude components from BOM. |
| swDmExcludeFromBOM_NotDefined | - 1 = Indicates that the document was created or saved in SOLIDWORKS 2008 SP01 or earlier. Open and save the document in SOLIDWORKS 2008 SP02 or later. |
| swDmExcludeFromBOM_TRUE | 1 = Exclude components from BOM. |

## See Also

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
