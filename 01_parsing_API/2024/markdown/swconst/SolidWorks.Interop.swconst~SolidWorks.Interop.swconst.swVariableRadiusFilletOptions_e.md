---
title: "swVariableRadiusFilletOptions_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swVariableRadiusFilletOptions_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swVariableRadiusFilletOptions_e.html"
---

# swVariableRadiusFilletOptions_e Enumeration

Variable radius fillet transition options.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swVariableRadiusFilletOptions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swVariableRadiusFilletOptions_e
```

### C#

```csharp
public enum swVariableRadiusFilletOptions_e : System.Enum
```

### C++/CLI

```cpp
public enum class swVariableRadiusFilletOptions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swSmoothTransition | 0 = Fillet changes smoothly from one radius to another when matching a fillet edge to an adjacent face |
| swStraightTransition | 1 = Fillet changes from one radius to another linearly without matching edge tangency with an adjacent fillet |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
