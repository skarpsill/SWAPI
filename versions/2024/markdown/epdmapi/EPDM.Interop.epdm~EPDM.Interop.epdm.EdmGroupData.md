---
title: "EdmGroupData Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmGroupData"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData.html"
---

# EdmGroupData Structure

Contains information about a user group.

## Syntax

### Visual Basic

```vb
Public Structure EdmGroupData
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmGroupData : System.ValueType
```

### C++/CLI

```cpp
public value class EdmGroupData : public System.ValueType
```

## Examples

struct EdmGroupData

{ string mbsName ;

string mbsDescription ;

integer mlFlags ;

integer mlSysRights ;

short mbAutoAdd ;

array moMembers ;

integer mlGroupID ;

integer mhStatus ;

[IEdmUserGroup5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5.html)

*

[mpoGroup](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData~mpoGroup.html)

;

};

## Remarks

Used in[IEdmUserMgr6::AddGroups](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr6~AddGroups.html). This structure is extended by[EdmGroupData2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2.html), which should be used instead of this structure in version 2010 and later.

## See Also

[EdmGroupData Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2007
