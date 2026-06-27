---
title: "swHealActionType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swHealActionType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swHealActionType_e.html"
---

# swHealActionType_e Enumeration

Healing actions.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swHealActionType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swHealActionType_e
```

### C#

```csharp
public enum swHealActionType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swHealActionType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swHealAction_Cap | 2 = Finds a surface where all edges of the wound lie and attaches this to a face and covers the wound; SOLIDWORKS creates a new face to cover the wound |
| swHealAction_GrowParent | 1 = Extends the parent faces around the wound to cover it |
| swHealAction_Shrink | 0 = If extending faces does not yield a solution, then SOLIDWORKS tries to shrink the faces |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
