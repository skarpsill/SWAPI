---
title: "swEditPartCommandStatus_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swEditPartCommandStatus_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEditPartCommandStatus_e.html"
---

# swEditPartCommandStatus_e Enumeration

Return values during the activation of a part.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swEditPartCommandStatus_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swEditPartCommandStatus_e
```

### C#

```csharp
public enum swEditPartCommandStatus_e : System.Enum
```

### C++/CLI

```cpp
public enum class swEditPartCommandStatus_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swEditPartAsmMustBeSaved | -2 |
| swEditPartCompMustBeResolved | -4 |
| swEditPartCompMustBeSelected | -3 |
| swEditPartCompMustHaveWriteAccess | -5 |
| swEditPartCompNotPositioned | 1 or 0x1 |
| swEditPartFailure | -1 |
| swEditPartSuccessful | 0 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
