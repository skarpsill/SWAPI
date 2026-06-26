---
title: "swCornerReliefSuitCaseType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCornerReliefSuitCaseType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefSuitCaseType_e.html"
---

# swCornerReliefSuitCaseType_e Enumeration

Sheet metal corner relief suitcase types.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCornerReliefSuitCaseType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCornerReliefSuitCaseType_e
```

### C#

```csharp
public enum swCornerReliefSuitCaseType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCornerReliefSuitCaseType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCornerReliefSuitCase_Default | 0 = Leaves the gap unchanged |
| swCornerReliefSuitCase_ExtendGapInBendArea | 1 = Cut the corner relief with the gap |
| swCornerReliefSuitCase_FillInSomeGap | 2 = Extends the corner relief material into the gap |

## Remarks

A suitcase is a closed spherical corner without any cutouts.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
