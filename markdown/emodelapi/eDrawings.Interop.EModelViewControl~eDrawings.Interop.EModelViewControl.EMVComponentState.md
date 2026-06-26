---
title: "EMVComponentState Enumeration"
project: "eDrawings API Help"
interface: "EMVComponentState"
member: ""
kind: "enum"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.EMVComponentState.html"
---

# EMVComponentState Enumeration

Component states. Bitmask.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum EMVComponentState
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As EMVComponentState
```

### C#

```csharp
public enum EMVComponentState : System.Enum
```

### C++/CLI

```cpp
public enum class EMVComponentState : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| eMVHidden | 1 = Hidden mode |
| eMVHighlight | 2 = Highlight mode. Setting a component to its highlight state is not the same as selecting it in the user interface even though both actions turn the component green. |

## See Also

[eDrawings.Interop.EModelViewControl Namespace](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl_namespace.html)
