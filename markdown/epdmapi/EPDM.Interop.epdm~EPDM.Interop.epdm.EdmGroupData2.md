---
title: "EdmGroupData2 Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmGroupData2"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2.html"
---

# EdmGroupData2 Structure

Contains information about a user group.

## Syntax

### Visual Basic

```vb
Public Structure EdmGroupData2
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmGroupData2 : System.ValueType
```

### C++/CLI

```cpp
public value class EdmGroupData2 : public System.ValueType
```

## Examples

struct EdmGroupData2{ string mbsName ; string mbsDescription ; integer mlFlags ; array( enum EdmSysPerm ) moSysPerms ; short mbAutoAdd ; array(integer) moMembers ; integer mlGroupID ; integer mhStatus ; IEdmUserGroup5 * mpoGroup ; };

## Examples

[Vault Utilities (VB.NET)](Vault_Utilities_Example_VBNET.htm)

[Vault Utilities (C#)](Vault_Utilities_Example_CSharp.htm)

## Remarks

This structure extends

[EdmGroupData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData.html)

and is used in

[IEdmUserMgr7::AddGroups2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr7~AddGroups2.html)

to add user groups to the vault.

## See Also

[EdmGroupData2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2010
