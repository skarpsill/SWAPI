---
title: "swHingeMateEntityType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swHingeMateEntityType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swHingeMateEntityType_e.html"
---

# swHingeMateEntityType_e Enumeration

Hinge mate entity types.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swHingeMateEntityType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swHingeMateEntityType_e
```

### C#

```csharp
public enum swHingeMateEntityType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swHingeMateEntityType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swHingeMateEntityType_Angle | 2 = Select two faces to define the extent of angular rotation |
| swHingeMateEntityType_Coincident | 1 = Select two coincident entities: a plane or planar face another plane, planar face, edge, or point |
| swHingeMateEntityType_Concentric | 0 = Select two concentric entities; valid selections are the same as for concentric mates |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
