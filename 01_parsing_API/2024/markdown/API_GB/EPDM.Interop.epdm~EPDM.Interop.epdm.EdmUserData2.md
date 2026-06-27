---
title: "EdmUserData2 Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmUserData2"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData2.html"
---

# EdmUserData2 Structure

Contains information about a user to be created.

## Syntax

### Visual Basic

```vb
Public Structure EdmUserData2
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmUserData2 : System.ValueType
```

### C++/CLI

```cpp
public value class EdmUserData2 : public System.ValueType
```

## Examples

struct EdmUserData2{ string mbsUserName ; string mbsInitials ; string mbsCompleteName ; string mbsUserData ; string mbsPassword ; string mbsEmail ; integer mlFlags ; EdmSysPerm [] moSysPerms ; string mbsColumnView ; integer mlUserID ; integer mhStatus ; IEdmUser6 * mpoUser ; };

## Examples

[Add Users (C#)](Add_Users_Example_CSharp.htm)

[Add Users (VB.NET)](Add_Users_Example_VBNET.htm)

[Add and Remove User and Group from Folder (C#)](Add_and_Remove_User_and_Group_from_Folder_Example_CSharp.htm)

[Add and Remove User and Group from Folder (VB.NET)](Add_and_Remove_User_and_Group_from_Folder_Example_VBNET.htm)

## See Also

[EdmUserData2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData2_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2010
