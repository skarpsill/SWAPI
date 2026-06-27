---
title: "swFlangePositionTypes_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swFlangePositionTypes_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFlangePositionTypes_e.html"
---

# swFlangePositionTypes_e Enumeration

Position types for sheet metal edge flanges.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swFlangePositionTypes_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swFlangePositionTypes_e
```

### C#

```csharp
public enum swFlangePositionTypes_e : System.Enum
```

### C++/CLI

```cpp
public enum class swFlangePositionTypes_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swFlangePositionTypeBendCenterLine | 4 |
| swFlangePositionTypeBendOutside | 3 |
| swFlangePositionTypeBendSharp | 5 = Bend from virtual sharp |
| swFlangePositionTypeBendTangent | 6 = The flange position will always be tangent to the side face attached to the selected edge, and the flange length will always maintain the exact length; not valid for the Up To Edge And Merge length end condition |
| swFlangePositionTypeMaterialInside | 1 |
| swFlangePositionTypeMaterialOutside | 2 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
