---
title: "EdmUserDataEx Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmUserDataEx"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserDataEx.html"
---

# EdmUserDataEx Structure

Contains information about a user.

## Syntax

### Visual Basic

```vb
Public Structure EdmUserDataEx
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmUserDataEx : System.ValueType
```

### C++/CLI

```cpp
public value class EdmUserDataEx : public System.ValueType
```

## Examples

struct EdmUserDataEx{ integer mlUserID ; integer mlEdmUserDataExFlags ; string mbsInitials ; string mbsCompleteName ; string mbsUserData ; string mbsEmail ; string mbsPhone ; string mbsCellPhone ; string mbsPicturePath ; string mbsWebSite1 ; string mbsWebSite2 ; string mbsWebSite3 ; string mbsWebSite4 ; string mbsPresenceNote ; };

## Examples

[Find Users (VB.NET)](Find_Users_Example_VBNET.htm)

[Find Users (C#)](Find_Users_Example_CSharp.htm)

## Remarks

Used to read/write user properties via[IEdmUser10::GetUserDataEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser10~GetUserDataEx.html)and[IEdmUser10::SetUserDataEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser10~SetUserDataEx.html).

The following image shows where the EdmUserDataEx struct fields are used in the user popup window when[IEdmUserMgr8::ShowUserPopup](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr8~ShowUserPopup.html)is called after updating the properties with[IEdmUser10::GetUserDataEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser10~GetUserDataEx.html).

## See Also

[EdmUserDataEx Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserDataEx_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2013
