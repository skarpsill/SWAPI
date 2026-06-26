---
title: "EdmHistoryItem Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmHistoryItem"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem.html"
---

# EdmHistoryItem Structure

Contains a history item.

## Syntax

### Visual Basic

```vb
Public Structure EdmHistoryItem
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmHistoryItem : System.ValueType
```

### C++/CLI

```cpp
public value class EdmHistoryItem : public System.ValueType
```

## Examples

struct EdmHistoryItem{ enum EdmHistoryType meType ; datetime moDate ; integer mlVersion ; integer mlUserID ; integer mlFileID ; integer mlFolderID ; string mbsItemName ; string mbsUserName ; string mbsComment ; struct EdmCmdData moData ; };

## Examples

[Get Histories of Files (VB.NET)](Get_Histories_of_Files_Example_VBNET.htm)

[Get Histories of Files (C#)](Get_Histories_of_Files_Example_CSharp.htm)

## Remarks

Returned by[IEdmHistory](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmHistory.html).

## See Also

[EdmHistoryItem Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmHistoryItem_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

Version 6.4 of SOLIDWORKS PDM Professional
