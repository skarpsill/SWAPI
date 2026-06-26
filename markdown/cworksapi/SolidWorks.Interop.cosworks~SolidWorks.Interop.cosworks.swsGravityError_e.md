---
title: "swsGravityError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsGravityError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsGravityError_e.html"
---

# swsGravityError_e Enumeration

Gravity errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsGravityError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsGravityError_e
```

### C#

```csharp
public enum swsGravityError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsGravityError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsGravityErrorEdgeNotStraight | 3 = Selected edge to specify direction is not straight |
| swsGravityErrorFaceNotPlanar | 2 = Selected face to specify direction is not planar |
| swsGravityErrorGravityAlreadyDefined | 4 = Gravity is already defined |
| swsGravityErrorInvalidStudy | 5 = Invalid study type for gravity |
| swsGravityErrorSelectFaceEdgeOrPlane | 1 = Select face, edge, or plane |
| swsGravityErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
