---
title: "swViewAlignment_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swViewAlignment_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swViewAlignment_e.html"
---

# swViewAlignment_e Enumeration

Values for alignment of views.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swViewAlignment_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swViewAlignment_e
```

### C#

```csharp
public enum swViewAlignment_e : System.Enum
```

### C++/CLI

```cpp
public enum class swViewAlignment_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swViewAlignBoth | 3 = View is aligned and has aligned children |
| swViewAligned | 2 = View is aligned with a parent view |
| swViewAlignedChildren | 1 = View has children aligned with it |
| swViewAlignNone | 0 = View has no alignment restrictions |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
