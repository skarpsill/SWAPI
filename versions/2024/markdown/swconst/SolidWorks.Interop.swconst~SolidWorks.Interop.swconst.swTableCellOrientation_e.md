---
title: "swTableCellOrientation_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swTableCellOrientation_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTableCellOrientation_e.html"
---

# swTableCellOrientation_e Enumeration

Orientations of text in table cells.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swTableCellOrientation_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swTableCellOrientation_e
```

### C#

```csharp
public enum swTableCellOrientation_e : System.Enum
```

### C++/CLI

```cpp
public enum class swTableCellOrientation_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swTableCellOrientation_Down | 3 |
| swTableCellOrientation_Left | 1 |
| swTableCellOrientation_Right | 0 |
| swTableCellOrientation_Rotate90CCW | 6 = Rotate text 90 degrees counter clockwise from the current orientation |
| swTableCellOrientation_Rotate90CW | 5 = Rotate text 90 degrees clockwise from the current orientation |
| swTableCellOrientation_Up | 2 |
| swTableCellOrientation_Varies | 4 = Orientation varies in several table cells; not valid when calling ITableAnnotation::SetCellTextOrientation |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
