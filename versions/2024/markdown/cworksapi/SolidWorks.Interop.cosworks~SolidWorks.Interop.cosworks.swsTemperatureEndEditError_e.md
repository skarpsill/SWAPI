---
title: "swsTemperatureEndEditError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsTemperatureEndEditError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTemperatureEndEditError_e.html"
---

# swsTemperatureEndEditError_e Enumeration

Temperature editing errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsTemperatureEndEditError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsTemperatureEndEditError_e
```

### C#

```csharp
public enum swsTemperatureEndEditError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsTemperatureEndEditError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsTemperatureEndEditErrorCannotSetInitialTemperatureType | 5 = Cannot set initial temperature type; invalid study type |
| swsTemperatureEndEditErrorEntityAlreadyExists | 2 = At least one entity is specified more than once |
| swsTemperatureEndEditErrorNoEntities | 3 = No entities selected |
| swsTemperatureEndEditErrorNoEntityAtIndex | 1 = No entity passed at index |
| swsTemperatureEndEditErrorSelectVerticesEdgesFacesComponentsOrBodies | 4 = Select vertices, edges, faces, components, or bodies |
| swsTemperatureEndEditErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
