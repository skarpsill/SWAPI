---
title: "swCollisionGroupSetComponentsErrors_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCollisionGroupSetComponentsErrors_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCollisionGroupSetComponentsErrors_e.html"
---

# swCollisionGroupSetComponentsErrors_e Enumeration

Errors when setting components in collision groups.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCollisionGroupSetComponentsErrors_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCollisionGroupSetComponentsErrors_e
```

### C#

```csharp
public enum swCollisionGroupSetComponentsErrors_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCollisionGroupSetComponentsErrors_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCollisionGroupSetComponentsErrors_ComponentsAddedElsewhere | 2 = One or more components have already been added to a different collision group |
| swCollisionGroupSetComponentsErrors_GroupRemoved | 3 = The specified collision group is no longer available |
| swCollisionGroupSetComponentsErrors_InvalidComponents | 1 = Components from a different assembly cannot be included in this collision detection |
| swCollisionGroupSetComponentsErrors_None | 0 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
