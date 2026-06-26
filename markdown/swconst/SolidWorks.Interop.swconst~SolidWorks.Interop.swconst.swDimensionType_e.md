---
title: "swDimensionType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swDimensionType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDimensionType_e.html"
---

# swDimensionType_e Enumeration

Types of dimensions.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swDimensionType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swDimensionType_e
```

### C#

```csharp
public enum swDimensionType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swDimensionType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAngularDimension | 3 = Angular dimension type |
| swAngularOrdinateDimension | 16 = Angular ordinate dimension |
| swArcLengthDimension | 4 = Arc length dimension type |
| swChamferDimension | 10 |
| swDiameterDimension | 6 = Diameter dimension |
| swDiametricLinearDimension | 15 = Doubled distance linear dimension |
| swDimensionTypeUnknown | 0 = Dimension type could not be determined |
| swHorLinearDimension | 11 = Horizontal linear dimension |
| swHorOrdinateDimension | 7 = Horizontal ordinate dimension |
| swLinearDimension | 2 = Linear dimension type |
| swOrdinateDimension | 1 = Base ordinate and its subordinates are of this type |
| swRadialDimension | 5 = Radial dimension |
| swRadialLinearDimension | 14 = Doubled distance radial dimension |
| swScalarDimension | 13 |
| swVertLinearDimension | 12 = Vertical linear dimension |
| swVertOrdinateDimension | 8 = Vertical ordinate dimension |
| swZAxisDimension | 9 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
