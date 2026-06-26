---
title: "swIntersectionType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swIntersectionType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swIntersectionType_e.html"
---

# swIntersectionType_e Enumeration

Curve intersections types.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swIntersectionType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swIntersectionType_e
```

### C#

```csharp
public enum swIntersectionType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swIntersectionType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swIntersectionCOINCIDENCE_END | 4 = An intersection at the end of a region of coincidence |
| swIntersectionCOINCIDENCE_START | 3 = An intersection at the start of a region of coincidence |
| swIntersectionSIMPLE | 1 = An intersection not adjoining a region of coincidence |
| swIntersectionTANGENT | 2 = A tangent intersection |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
