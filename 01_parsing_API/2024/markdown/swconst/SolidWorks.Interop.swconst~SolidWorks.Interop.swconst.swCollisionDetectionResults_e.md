---
title: "swCollisionDetectionResults_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCollisionDetectionResults_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCollisionDetectionResults_e.html"
---

# swCollisionDetectionResults_e Enumeration

Collision detection results.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCollisionDetectionResults_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCollisionDetectionResults_e
```

### C#

```csharp
public enum swCollisionDetectionResults_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCollisionDetectionResults_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCollisionDetectionResult_CollisionDetected | 1 |
| swCollisionDetectionResult_FailedNotEnoughGroups | -1 = You must define more than one collision group containing two or more unsuppressed components in different collision groups |
| swCollisionDetectionResult_NoCollision | 0 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
