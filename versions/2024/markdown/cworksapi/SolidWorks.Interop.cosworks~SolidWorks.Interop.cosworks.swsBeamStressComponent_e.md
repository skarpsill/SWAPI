---
title: "swsBeamStressComponent_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsBeamStressComponent_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsBeamStressComponent_e.html"
---

# swsBeamStressComponent_e Enumeration

Beam stresses

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsBeamStressComponent_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsBeamStressComponent_e
```

### C#

```csharp
public enum swsBeamStressComponent_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsBeamStressComponent_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsBeamStressComponentAxial | 0 = Uniform axial stress |
| swsBeamStressComponentBendingLocalDir1 | 1 = Upper bound bending stress due to moment M1 |
| swsBeamStressComponentBendingLocalDir2 | 2 = Upper bound bending stress due to moment M2 |
| swsBeamStressComponentWorstCase | 3 = Upper bound axial and bending stresses at the extreme fibers of the cross-section |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
