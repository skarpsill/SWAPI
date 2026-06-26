---
title: "swsHeatFluxError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsHeatFluxError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsHeatFluxError_e.html"
---

# swsHeatFluxError_e Enumeration

Heat flux errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsHeatFluxError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsHeatFluxError_e
```

### C#

```csharp
public enum swsHeatFluxError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsHeatFluxError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsHeatFluxErrorInvalidArray | 4 = Invalid array |
| swsHeatFluxErrorInvalidStudy | 3 = Invalid study type for heat flux (valid for thermal studies only) |
| swsHeatFluxErrorNoEntities | 5 = No entities specified (empty array) |
| swsHeatFluxErrorNoFaces | 1 = No faces selected |
| swsHeatFluxErrorNoFacesOrShellEdges | 2 = No faces or shell edges selected |
| swsHeatFluxErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
