---
title: "EdmCardViewParams Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmCardViewParams"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardViewParams.html"
---

# EdmCardViewParams Structure

Contains card view parameters.

## Syntax

### Visual Basic

```vb
Public Structure EdmCardViewParams
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmCardViewParams : System.ValueType
```

### C++/CLI

```cpp
public value class EdmCardViewParams : public System.ValueType
```

## Examples

struct EdmCardViewParams{ integer mlFileID ; integer mlFolderID ; integer mlCardID ; integer mlX ; integer mlY ; integer mhParentWindow ; integer mlEdmCardViewFlags ; };

## Examples

[Create Custom Card View (VB.NET)](Create_Custom_Card_View_Example_VBNET.htm)

[Create Custom Card View (C#)](Create_Custom_Card_View_Example_CSharp.htm)

## Remarks

Used by

[IEdmVault10::CreateCardViewEx2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault10~CreateCardViewEx2.html)

to create a card view.

## See Also

[EdmCardViewParams Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardViewParams_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2009
