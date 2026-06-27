---
title: "swsTemperatureError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsTemperatureError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTemperatureError_e.html"
---

# swsTemperatureError_e Enumeration

Temperature errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsTemperatureError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsTemperatureError_e
```

### C#

```csharp
public enum swsTemperatureError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsTemperatureError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsTemperatureErrorEmptyArray | 4 = No entities specified (empty array) |
| swsTemperatureErrorInvalidArray | 3 = Invalid array |
| swsTemperatureErrorInvalidStudy | 2 = Invalid study type for temperature (used for thermal studies only) |
| swsTemperatureErrorSelectVerticesEdgesFacesBodiesOrComponents | 1 = Select vertices, edges, faces, bodies, or components |
| swsTemperatureErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
