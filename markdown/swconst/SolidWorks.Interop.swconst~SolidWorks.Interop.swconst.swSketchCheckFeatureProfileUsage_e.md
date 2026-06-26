---
title: "swSketchCheckFeatureProfileUsage_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swSketchCheckFeatureProfileUsage_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSketchCheckFeatureProfileUsage_e.html"
---

# swSketchCheckFeatureProfileUsage_e Enumeration

Types of features to check to see if this sketch is valid for use in creating the specified feature.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swSketchCheckFeatureProfileUsage_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swSketchCheckFeatureProfileUsage_e
```

### C#

```csharp
public enum swSketchCheckFeatureProfileUsage_e : System.Enum
```

### C++/CLI

```cpp
public enum class swSketchCheckFeatureProfileUsage_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swSketchCheckFeature_BASEEXTRUDE | 1 |
| swSketchCheckFeature_BASEEXTRUDETHIN | 2 |
| swSketchCheckFeature_BASEREVOLVE | 6 |
| swSketchCheckFeature_BASEREVOLVETHIN | 7 |
| swSketchCheckFeature_BOSSEXTRUDE | 3 |
| swSketchCheckFeature_BOSSEXTRUDETHIN | 4 |
| swSketchCheckFeature_BOSSREVOLVE | 8 |
| swSketchCheckFeature_BOSSREVOLVETHIN | 9 |
| swSketchCheckFeature_CUTEXTRUDE | 11 |
| swSketchCheckFeature_CUTEXTRUDETHIN | 12 |
| swSketchCheckFeature_CUTREVOLVE | 13 |
| swSketchCheckFeature_CUTREVOLVETHIN | 14 |
| swSketchCheckFeature_LOFTGUIDE | 20 |
| swSketchCheckFeature_LOFTSECTION | 18 |
| swSketchCheckFeature_MOLD_PARTINGSURFACES | 23 |
| swSketchCheckFeature_RIBSECTION | 21 |
| swSketchCheckFeature_SHEETMETAL_BASEFLANGE | 22 |
| swSketchCheckFeature_SURFACEEXTRUDE | 5 |
| swSketchCheckFeature_SURFACELOFTSECTION | 19 |
| swSketchCheckFeature_SURFACEREVOLVE | 10 |
| swSketchCheckFeature_SURFACESWEEPSECTION | 16 |
| swSketchCheckFeature_SWEEPPATHORGUIDE | 17 |
| swSketchCheckFeature_SWEEPSECTION | 15 |
| swSketchCheckFeature_UNSET | 0 = Check for things that are wrong in any feature usage |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
