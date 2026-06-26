---
title: "swBodyType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swBodyType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBodyType_e.html"
---

# swBodyType_e Enumeration

Valid body types.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swBodyType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swBodyType_e
```

### C#

```csharp
public enum swBodyType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swBodyType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAllBodies | -1 = All solid and sheet bodies |
| swEmptyBody | 5 = NULL body |
| swGeneralBody | 4 = General, nonmanifold body |
| swGraphicsBody | 7 = Graphics body |
| swMeshBody | 6 = Mesh body |
| swMinimumBody | 3 = Point body |
| swSheetBody | 1 = Sheet body |
| swSolidBody | 0 = Solid body |
| swWireBody | 2 = Wire body |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
