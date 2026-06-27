---
title: "swsHeatPowerError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsHeatPowerError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsHeatPowerError_e.html"
---

# swsHeatPowerError_e Enumeration

Heat power errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsHeatPowerError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsHeatPowerError_e
```

### C#

```csharp
public enum swsHeatPowerError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsHeatPowerError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsHeatPowerErrorInvalidArray | 4 = Invalid array |
| swsHeatPowerErrorInvalidStudy | 3 = Invalid study type; heat power is valid for thermal studies only |
| swsHeatPowerErrorNoEntities | 5 = No entities selected (empty array) |
| swsHeatPowerErrorSelectFaceEdgeVertexComponentOrBody | 1 = Select face, edge, vertex, component, or body |
| swsHeatPowerErrorSelectFacesEdgesOrVertices | 2 = Select faces, edges, or vertices |
| swsHeatPowerErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
