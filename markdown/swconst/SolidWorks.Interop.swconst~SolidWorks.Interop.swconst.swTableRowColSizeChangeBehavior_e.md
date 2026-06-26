---
title: "swTableRowColSizeChangeBehavior_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swTableRowColSizeChangeBehavior_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTableRowColSizeChangeBehavior_e.html"
---

# swTableRowColSizeChangeBehavior_e Enumeration

Values indicate how the size of the rest of the table should behave when a height of a row or width of a column changes.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swTableRowColSizeChangeBehavior_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swTableRowColSizeChangeBehavior_e
```

### C#

```csharp
public enum swTableRowColSizeChangeBehavior_e : System.Enum
```

### C++/CLI

```cpp
public enum class swTableRowColSizeChangeBehavior_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swTableRowColChange_AbsorbedByNext | 1 = The next row or column must absorb the change in size so that the entire table size remains the same |
| swTableRowColChange_AbsorbedByPrevious | 2 = The next row or column must absorb the change in size so that the entire table size remains the same |
| swTableRowColChange_TableSizeCanChange | 0 = The remaining rows or columns can shift, so that the entire table width or height changes |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
