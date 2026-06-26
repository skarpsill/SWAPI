---
title: "swFlangeOffsetTypes_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swFlangeOffsetTypes_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFlangeOffsetTypes_e.html"
---

# swFlangeOffsetTypes_e Enumeration

End conditions for both flange length and flange position offset for sheet metal edge and base flanges.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swFlangeOffsetTypes_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swFlangeOffsetTypes_e
```

### C#

```csharp
public enum swFlangeOffsetTypes_e : System.Enum
```

### C++/CLI

```cpp
public enum class swFlangeOffsetTypes_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swFlangeOffsetBlind | 1 = Positions the edge flange based on the length and direction you specify |
| swFlangeOffsetFromSurface | 4 |
| swFlangeOffsetMidPlane | 5 |
| swFlangeOffsetUptoEdgeAndMerge | 6 = Creates the edge flange in a multibody part by merging a selected edge on one body with an Up To reference edge on the second body |
| swFlangeOffsetUpToSurface | 3 |
| swFlangeOffsetUpToVertex | 2 = Positions the edge flange up to a specified vertex; for flange length, the selected vertex may be either on a plane that is normal to the end face of the edge flange or on a plane that is parallel to the face of the base flange |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
