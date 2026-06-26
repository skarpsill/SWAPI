---
title: "swFlangeDimTypes_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swFlangeDimTypes_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFlangeDimTypes_e.html"
---

# swFlangeDimTypes_e Enumeration

Origins for dimensioning Blind or Up To Edge And Merge flange length end conditions in edge flanges.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swFlangeDimTypes_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swFlangeDimTypes_e
```

### C#

```csharp
public enum swFlangeDimTypes_e : System.Enum
```

### C++/CLI

```cpp
public enum class swFlangeDimTypes_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swFlangeDimTypeBendTangentArc | 3 = Flange length is measured from the edge flange face to a line that is tangent to the bend; not valid for the Up To Edge And Merge length end condition |
| swFlangeDimTypeInnerVirtualSharp | 2 = Flange length is measured from the edge flange face to an inner virtual sharp (sketch point at the virtual intersection point of two sketch entities) |
| swFlangeDimTypeOuterVirtualSharp | 1 = Flange length is measured from the edge flange face to an outer virtual sharp (sketch point at the virtual intersection point of two sketch entities) |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
