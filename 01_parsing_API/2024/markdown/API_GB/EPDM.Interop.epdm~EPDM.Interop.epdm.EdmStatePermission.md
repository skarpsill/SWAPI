---
title: "EdmStatePermission Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmStatePermission"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmStatePermission.html"
---

# EdmStatePermission Structure

Contains state permission information.

## Syntax

### Visual Basic

```vb
Public Structure EdmStatePermission
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmStatePermission : System.ValueType
```

### C++/CLI

```cpp
public value class EdmStatePermission : public System.ValueType
```

## Examples

struct EdmStatePermission { enum EdmObjectType meOwnerType ; integer mlOwnerID ; integer mlStateID ; integer mlEdmRightFlag ; };

## Remarks

Used by

[IEdmUserMgr9::GetStatePermissions](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9~GetStatePermissions.html)

and

[IEdmUserMgr9::SetStatePermissions](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr9~SetStatePermissions.html)

.

## See Also

[EdmStatePermission Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmStatePermission_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2017
