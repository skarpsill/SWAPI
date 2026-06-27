---
title: "swCollisionGroupApplyTransformErrors_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCollisionGroupApplyTransformErrors_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCollisionGroupApplyTransformErrors_e.html"
---

# swCollisionGroupApplyTransformErrors_e Enumeration

Errors when applying transforms to collision groups.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCollisionGroupApplyTransformErrors_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCollisionGroupApplyTransformErrors_e
```

### C#

```csharp
public enum swCollisionGroupApplyTransformErrors_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCollisionGroupApplyTransformErrors_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCollisionGroupApplyTransformErrors_GroupRemoved | 3 = The specified collision group is no longer available |
| swCollisionGroupApplyTransformErrors_InvalidTransforms | 2 = Array of transforms contains a null pointer for one or more elements or a pointer to an object other than an IMathTransform |
| swCollisionGroupApplyTransformErrors_None | 0 |
| swCollisionGroupApplyTransformErrors_SizeMismatch | 1 = Array of transforms does not contain one IMathTransform for each component in the collision group |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
