---
title: "swsCentrifugalForceError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsCentrifugalForceError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCentrifugalForceError_e.html"
---

# swsCentrifugalForceError_e Enumeration

Centrifugal force errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsCentrifugalForceError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsCentrifugalForceError_e
```

### C#

```csharp
public enum swsCentrifugalForceError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsCentrifugalForceError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsCentrifugalForceErrorAlreadyDefined | 4 = Centrifugal force is already defined |
| swsCentrifugalForceErrorEdgeNotLinear | 3 = Edge is not linear |
| swsCentrifugalForceErrorFaceNotCylindrical | 2 = Face is not cylindrical |
| swsCentrifugalForceErrorInvalidStudyType | 5 = Study type is invalid for centrifugal force |
| swsCentrifugalForceErrorSelectAxisEdgeOrCylindricalFace | 1 = Select an axis, edge, or cylindrical face for the direction |
| swsCentrifugalForceErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
