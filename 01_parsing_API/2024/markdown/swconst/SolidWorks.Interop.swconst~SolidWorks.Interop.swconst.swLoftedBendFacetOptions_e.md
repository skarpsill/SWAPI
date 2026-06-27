---
title: "swLoftedBendFacetOptions_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swLoftedBendFacetOptions_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLoftedBendFacetOptions_e.html"
---

# swLoftedBendFacetOptions_e Enumeration

Faceting options for lofted bend facet features.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swLoftedBendFacetOptions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swLoftedBendFacetOptions_e
```

### C#

```csharp
public enum swLoftedBendFacetOptions_e : System.Enum
```

### C++/CLI

```cpp
public enum class swLoftedBendFacetOptions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAngleBetweenSegments | 3 = Facet by maximum angle between adjacent linear segments |
| swBendsPerTransitionSegment | 1 = Facet by maximum number of bends per transition segment |
| swChordTolerance | 0 = Facet by maximum distance between the arc and linear segment of a chord on the lofted bend |
| swMaxSegmentLength | 2 = Facet by maximum length of a linear segment |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
