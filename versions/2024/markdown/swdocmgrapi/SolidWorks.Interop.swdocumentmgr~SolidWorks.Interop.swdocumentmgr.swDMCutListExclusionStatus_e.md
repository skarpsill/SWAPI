---
title: "swDMCutListExclusionStatus_e Enumeration"
project: "SOLIDWORKS Document Manager API Help"
interface: "swDMCutListExclusionStatus_e"
member: ""
kind: "enum"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDMCutListExclusionStatus_e.html"
---

# swDMCutListExclusionStatus_e Enumeration

Exclusion statuses of a cut list item.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swDMCutListExclusionStatus_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swDMCutListExclusionStatus_e
```

### C#

```csharp
public enum swDMCutListExclusionStatus_e : System.Enum
```

### C++/CLI

```cpp
public enum class swDMCutListExclusionStatus_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDMCutListStatus_Excluded | 1 |
| swDMCutListStatus_Included | 0 |
| swDMCutListStatus_Unknown | -1 = Data is missing or document was saved in a SOLIDWORKS version earlier than 2021 |

## See Also

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
