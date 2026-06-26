---
title: "EdmCheckRef Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmCheckRef"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCheckRef.html"
---

# EdmCheckRef Structure

Contains information about a file reference.

## Syntax

### Visual Basic

```vb
Public Structure EdmCheckRef
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmCheckRef : System.ValueType
```

### C++/CLI

```cpp
public value class EdmCheckRef : public System.ValueType
```

## Examples

struct EdmCheckRef{ integer mlParentFileID ; integer mlRefFileID ; string mbsParentPath ; string mbsRefPath ; integer mlRefVersion ; integer mlRefLatestVersion ; integer mlRefFolderID ; };

## Remarks

Returned by

[IEdmRevisionMgr3::VerUpgrade_ReferenceCheck](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr3~VerUpgrade_ReferenceCheck.html)

.

## See Also

[EdmCheckRef Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCheckRef_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2009
