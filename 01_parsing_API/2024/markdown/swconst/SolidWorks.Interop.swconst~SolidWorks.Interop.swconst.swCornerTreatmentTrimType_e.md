---
title: "swCornerTreatmentTrimType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCornerTreatmentTrimType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerTreatmentTrimType_e.html"
---

# swCornerTreatmentTrimType_e Enumeration

Structure system corner treatment trim types.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCornerTreatmentTrimType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCornerTreatmentTrimType_e
```

### C#

```csharp
public enum swCornerTreatmentTrimType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCornerTreatmentTrimType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCornerTreatmentTrim_BodyTrim | 1 = Conforms the intersecting member to the shape of adjacent faces by adding or removing material according to trim order |
| swCornerTreatmentTrim_MiterTrim | 2 = Trims the members at a 45 degree angle; valid only for two member corner treatments |
| swCornerTreatmentTrim_PlanarTrim | 0 = Cuts the intersecting member with a plane using first contact or full contact trim |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
