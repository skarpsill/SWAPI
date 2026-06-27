---
title: "swParameterizationPropertyType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swParameterizationPropertyType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swParameterizationPropertyType_e.html"
---

# swParameterizationPropertyType_e Enumeration

Properties of U and V parameters.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swParameterizationPropertyType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swParameterizationPropertyType_e
```

### C#

```csharp
public enum swParameterizationPropertyType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swParameterizationPropertyType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swParameterizationPropertyType_AllDerivativesContinuous | 13737 |
| swParameterizationPropertyType_AllDerivativesNotContinuous | 13738 |
| swParameterizationPropertyType_BoundsCoincident | 13746 = Bounds at the ends of the parameter range are coincident |
| swParameterizationPropertyType_Circular | 13740 = The parameter represents an angle around a circle; A circle indicates that the other parameter is a constant |
| swParameterizationPropertyType_Linear | 13739 = The parameter is proportional to the distance along a straight line; A straight line indicates that the other parameter is a constant |
| swParameterizationPropertyType_Periodic | 13701 = Periodic parameterization |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
