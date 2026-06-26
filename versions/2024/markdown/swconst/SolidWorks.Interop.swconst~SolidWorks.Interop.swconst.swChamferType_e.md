---
title: "swChamferType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swChamferType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swChamferType_e.html"
---

# swChamferType_e Enumeration

Chamfer types.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swChamferType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swChamferType_e
```

### C#

```csharp
public enum swChamferType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swChamferType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swChamferAngleDistance | 1 |
| swChamferDistanceDistance | 2 |
| swChamferEqualDistance | 16 |
| swChamferVertex | 3 |

## Remarks

These values can be bitwise OR'd to get the desired chamfer type.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
