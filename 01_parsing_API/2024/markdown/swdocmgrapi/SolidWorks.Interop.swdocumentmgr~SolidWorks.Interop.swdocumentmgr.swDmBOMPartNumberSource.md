---
title: "swDmBOMPartNumberSource Enumeration"
project: "SOLIDWORKS Document Manager API Help"
interface: "swDmBOMPartNumberSource"
member: ""
kind: "enum"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmBOMPartNumberSource.html"
---

# swDmBOMPartNumberSource Enumeration

Sources of bill of materials (BOM) part numbers.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swDmBOMPartNumberSource
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swDmBOMPartNumberSource
```

### C#

```csharp
public enum swDmBOMPartNumberSource : System.Enum
```

### C++/CLI

```cpp
public enum class swDmBOMPartNumberSource : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDmBOMPartNumber_ConfigurationName | 1 |
| swDmBOMPartNumber_DocumentName | 0 |
| swDmBOMPartNumber_NotDefined | -1 = Document was saved in older version of SOLIDWORKS; you must save the document in SOLIDWORKS 2009 or later |
| swDmBOMPartNumber_ParentName | 2 |
| swDmBOMPartNumber_UserSpecified | 3 |

## See Also

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
