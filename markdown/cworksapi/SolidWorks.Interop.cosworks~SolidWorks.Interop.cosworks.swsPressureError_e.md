---
title: "swsPressureError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsPressureError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsPressureError_e.html"
---

# swsPressureError_e Enumeration

Pressure errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsPressureError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsPressureError_e
```

### C#

```csharp
public enum swsPressureError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsPressureError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsPressureErrorCannotApplyPressure | 7 = You cannot apply the pressure to the entity used for reference geometry |
| swsPressureErrorInvalidArray | 6 = Invalid entity array |
| swsPressureErrorInvalidStudy | 5 = Invalid study type for pressure |
| swsPressureErrorPressureType | 4 = Selected pressure type must be 0 or 1 |
| swsPressureErrorSelectFaceEdgePlaneOrAxis | 3 = Select face, edge, plane, or axis for reference geometry |
| swsPressureErrorSelectFaceOrFaces | 1 = Select one or more faces |
| swsPressureErrorSelectFacesOrShellEdges | 2 = Select faces or shell edges |
| swsPressureErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
