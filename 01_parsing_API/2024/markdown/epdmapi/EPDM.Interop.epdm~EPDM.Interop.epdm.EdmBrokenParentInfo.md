---
title: "EdmBrokenParentInfo Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmBrokenParentInfo"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBrokenParentInfo.html"
---

# EdmBrokenParentInfo Structure

Contains broken parent information.

## Syntax

### Visual Basic

```vb
Public Structure EdmBrokenParentInfo
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmBrokenParentInfo : System.ValueType
```

### C++/CLI

```cpp
public value class EdmBrokenParentInfo : public System.ValueType
```

## Examples

struct EdmBrokenParentInfo{ integer mlParentFileID ; integer mlParentFolderID ; string mbsParentName ; integer mlChildFileID ; integer mlChildFolderID ; string mbsChildName ; };

## See Also

[EdmBrokenParentInfo Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBrokenParentInfo_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2013
