---
title: "EdmGenItemInfo Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmGenItemInfo"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGenItemInfo.html"
---

# EdmGenItemInfo Structure

Contains information about generated items.

## Syntax

### Visual Basic

```vb
Public Structure EdmGenItemInfo
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmGenItemInfo : System.ValueType
```

### C++/CLI

```cpp
public value class EdmGenItemInfo : public System.ValueType
```

## Examples

struct EdmGenItemInfo{ integer mlFileID ; integer mlFileParentFolderID ; string mbsConfiguration ; integer mlFileVersion ; string mbsFileFolderPath ; string mbsFileName ; integer mlItemID ; integer mlItemParentFolderID ; enum EdmItemLinkType meLinkType ; string mbsItemFolderPath ; string mbsItemName ; string mbsItemAlternativeName ; integer mhResult ; };

## Examples

[Add Items (C#)](Add_Items_Example_CSharp.htm)

[Add Items (VB.NET)](Add_Items_Example_VBNET.htm)

## Remarks

Returned by

[IEdmBatchItemGeneration::GenerateItems](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration~GenerateItems.html)

.

## See Also

[EdmGenItemInfo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGenItemInfo_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2010
