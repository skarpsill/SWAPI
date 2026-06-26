---
title: "swsHeatPowerEndEditError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsHeatPowerEndEditError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsHeatPowerEndEditError_e.html"
---

# swsHeatPowerEndEditError_e Enumeration

Heat power editing errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsHeatPowerEndEditError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsHeatPowerEndEditError_e
```

### C#

```csharp
public enum swsHeatPowerEndEditError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsHeatPowerEndEditError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsHeatPowerEndEditErrorEntityAlreadyExists | 2 = At least one entity is specified more than once |
| swsHeatPowerEndEditErrorLowerboundTemperatureHigherThanUpperbound | 7 = Lower-bound temperature cannot be higher than the upper-bound temperature |
| swsHeatPowerEndEditErrorNoEntitiesSelected | 3 = No entities specified |
| swsHeatPowerEndEditErrorNoEntityAtIndex | 1 = No entity passed at index |
| swsHeatPowerEndEditErrorNotValidForSteadyStateAnalysis | 8 = Not valid for steady-state analysis; solution type must be transient |
| swsHeatPowerEndEditErrorSelectFaceEdgeOrVertex | 5 = Select a face, edge, or vertex |
| swsHeatPowerEndEditErrorSelectVertexForThermostatLocation | 6 = Specify a vertex for the location of the thermostat |
| swsHeatPowerEndEditErrorSelectVerticesEdgesFacesComponentsOrBodies | 4 = Select vertices, edges, faces, components, or bodies |
| swsHeatPowerEndEditErrorSuccessful | 0 = Successful |
| swsHeatPowerEndEditErrorVertexCannotBeUsedForSensorLocation | 9 = A vertex in the selected entities cannot be used for the location of the sensor |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
