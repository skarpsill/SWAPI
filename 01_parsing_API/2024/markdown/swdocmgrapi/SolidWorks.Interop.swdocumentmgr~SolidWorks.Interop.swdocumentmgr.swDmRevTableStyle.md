---
title: "swDmRevTableStyle Enumeration"
project: "SOLIDWORKS Document Manager API Help"
interface: "swDmRevTableStyle"
member: ""
kind: "enum"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmRevTableStyle.html"
---

# swDmRevTableStyle Enumeration

Multiple drawing sheet styles for revision tables.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swDmRevTableStyle
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swDmRevTableStyle
```

### C#

```csharp
public enum swDmRevTableStyle : System.Enum
```

### C++/CLI

```cpp
public enum class swDmRevTableStyle : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDmRevCopyOfSheet1 | 1 = Linked; copies the revision table on sheet 1 to all sheets, updating all revision tables when revisions are made |
| swDmRevIndependent | 2 = Independent; makes the revision table on each sheet independent of the other revision tables in the drawing; updates to one revision table do not affect other revision tables |
| swDmRevSeeSheet1 | 0 = See Sheet 1; makes the revision table on the first sheet the active table, labeling the revision tables on all other drawing sheets, See Sheet 1 |
| swDmRevStyleUnknown | -1 |

## See Also

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
