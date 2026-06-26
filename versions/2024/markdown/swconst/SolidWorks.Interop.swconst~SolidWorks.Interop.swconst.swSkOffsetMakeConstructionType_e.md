---
title: "swSkOffsetMakeConstructionType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swSkOffsetMakeConstructionType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSkOffsetMakeConstructionType_e.html"
---

# swSkOffsetMakeConstructionType_e Enumeration

Convert original and offset sketch entities to construction sketch entities.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swSkOffsetMakeConstructionType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swSkOffsetMakeConstructionType_e
```

### C#

```csharp
public enum swSkOffsetMakeConstructionType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swSkOffsetMakeConstructionType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swSkOffsetDontMakeConstruction | 0 = Do not the convert original or offset sketch entities to construction sketch entities |
| swSkOffsetMakeBothConstruction | 3 = Convert the original and offset sketch entities to construction sketch entities |
| swSkOffsetMakeOffsConstruction | 2 = Convert only the offset sketch entities to construction sketch entities |
| swSkOffsetMakeOrigConstruction | 1 = Convert only the original sketch entities to construction sketch entities |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
