---
title: "swGtolTolType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swGtolTolType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGtolTolType_e.html"
---

# swGtolTolType_e Enumeration

Tolerance zone types in Gtol frame boxes.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swGtolTolType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swGtolTolType_e
```

### C#

```csharp
public enum swGtolTolType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swGtolTolType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swGtolTolType_MAX | 5 = Specifies a maximum value for a material condition that has already been specified as a modifier of the tolerance in the Gtol; this maximum upper tolerance is typically specified in the Tolerance 2 box with "MAX" |
| swGtolTolType_None | 0 |
| swGtolTolType_ProjectedTolerance | 2 = Applies to holes in which a pin, stud, or screw is to be inserted; controls the perpendicularity of the hole to the extent of the projection from the hole; specified with a circle-P symbol; typically a height is also specified in a separate field |
| swGtolTolType_Square | 3 |
| swGtolTolType_UnequallyDisposedProfile | 4 = Indicates that the profile of a surface tolerance is not symmetrical about the true profile; the value following the circle-U symbol is the amount of the tolerance that is in a direction that would allow additional material to be added to the true profile |
| swGtolTolType_Unknown | 1 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
