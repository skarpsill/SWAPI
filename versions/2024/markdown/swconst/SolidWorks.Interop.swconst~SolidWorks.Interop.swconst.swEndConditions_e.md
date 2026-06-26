---
title: "swEndConditions_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swEndConditions_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndConditions_e.html"
---

# swEndConditions_e Enumeration

End conditions for creation of a variety of features.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swEndConditions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swEndConditions_e
```

### C#

```csharp
public enum swEndConditions_e : System.Enum
```

### C++/CLI

```cpp
public enum class swEndConditions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swEndCondBlind | 0 |
| swEndCondMidPlane | 6 |
| swEndCondOffsetFromSurface | 5 |
| swEndCondThroughAll | 1 |
| swEndCondThroughAllBoth | 9 |
| swEndCondThroughNext | 2 |
| swEndCondUpToBody | 7 |
| swEndCondUpToNext | 11 |
| swEndCondUpToSelection | 10 |
| swEndCondUpToSurface | 4 = Do not use; superseded by swEndCondUpToSelection |
| swEndCondUpToVertex | 3 = Do not use; superseded by swEndCondUpToSelection |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
