---
title: "swAlignViewTypes_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swAlignViewTypes_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAlignViewTypes_e.html"
---

# swAlignViewTypes_e Enumeration

View alignments.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swAlignViewTypes_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swAlignViewTypes_e
```

### C#

```csharp
public enum swAlignViewTypes_e : System.Enum
```

### C++/CLI

```cpp
public enum class swAlignViewTypes_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAlignViewHorizontalCenter | 2 = Align this view horizontally with the center of BaseView |
| swAlignViewHorizontalOrigin | 4 = Align this view horizontally with the origin of BaseView |
| swAlignViewVerticalCenter | 3 = Align this view vertically with BaseView |
| swAlignViewVerticalOrigin | 5 = Align this view vertically with the origin of BaseView |
| swDefaultViewAlignment | 1 = Set the alignment of this view to its default |
| swNoViewAlignment | 0 = Remove the alignment restriction on this view |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
