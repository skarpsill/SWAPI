---
title: "swCommandFlyoutStyle_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCommandFlyoutStyle_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCommandFlyoutStyle_e.html"
---

# swCommandFlyoutStyle_e Enumeration

Types of FlyoutGroup.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCommandFlyoutStyle_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCommandFlyoutStyle_e
```

### C#

```csharp
public enum swCommandFlyoutStyle_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCommandFlyoutStyle_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCommandFlyoutStyle_Favorite | 1 = the first command in the menu list is the immediate action for the main button |
| swCommandFlyoutStyle_LastUsed | 2 = the last used command in the menu list is the immediate action for the main button |
| swCommandFlyoutStyle_Simple | 0 = no immediate action is available for the main button |

## Remarks

Context-sensitive menus support only the swCommandFlyoutStyle_Simple flyout style.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
