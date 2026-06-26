---
title: "EdmUserData Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmUserData"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData.html"
---

# EdmUserData Structure

Obsolete. Superseded by

[EdmUserData2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData2.html)

in SOLIDWORKS PDM Professional 2010 and later.

## Syntax

### Visual Basic

```vb
Public Structure EdmUserData
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmUserData : System.ValueType
```

### C++/CLI

```cpp
public value class EdmUserData : public System.ValueType
```

## Examples

struct EdmUserData{ string mbsUserName ; string mbsInitials ; string mbsCompleteName ; string mbsUserData ; string mbsPassword ; string mbsEmail ; integer mlFlags ; integer mlSysRights ; string mbsColumnView ; integer mlUserID ; integer mhStatus ; IEdmUser6 * mpoUser ; };

## Remarks

Holds information about a user. This struct is used as argument to

[IEdmUserMgr6::AddUsers](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr6~AddUsers.html)

.

## See Also

[EdmUserData Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2007
