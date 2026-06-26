---
title: "swDmShowChildComponentsInBOMResult Enumeration"
project: "SOLIDWORKS Document Manager API Help"
interface: "swDmShowChildComponentsInBOMResult"
member: ""
kind: "enum"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmShowChildComponentsInBOMResult.html"
---

# swDmShowChildComponentsInBOMResult Enumeration

How components are displayed in the bill of materials (BOM).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swDmShowChildComponentsInBOMResult
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swDmShowChildComponentsInBOMResult
```

### C#

```csharp
public enum swDmShowChildComponentsInBOMResult : System.Enum
```

### C++/CLI

```cpp
public enum class swDmShowChildComponentsInBOMResult : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDmShowChildComponentsInBOM_FALSE | 0 = Do not display child components in the BOM; the subassembly appears as a single item |
| swDmShowChildComponentsInBOM_NotDefined | -1 = Document was saved in an older version of SOLIDWORKS; you must save document in SOLIDWORKS 2009 or later |
| swDmShowChildComponentsInBOM_Promote | 2 = All of the child components are promoted one level; the configuration dissolves when it appears in a BOM |
| swDmShowChildComponentsInBOM_TRUE | 1 = List child components individually in the BOM |

## See Also

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
