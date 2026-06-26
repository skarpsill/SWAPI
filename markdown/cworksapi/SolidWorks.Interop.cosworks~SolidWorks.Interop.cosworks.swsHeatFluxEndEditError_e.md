---
title: "swsHeatFluxEndEditError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsHeatFluxEndEditError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsHeatFluxEndEditError_e.html"
---

# swsHeatFluxEndEditError_e Enumeration

Heat flux editing errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsHeatFluxEndEditError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsHeatFluxEndEditError_e
```

### C#

```csharp
public enum swsHeatFluxEndEditError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsHeatFluxEndEditError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsHeatFluxEndEditErrorEntityAlreadyExists | 2 = At least one entity is specified more than once |
| swsHeatFluxEndEditErrorLowerboundTemperatureHigherThanUpperbound | 7 = Lower-bound temperature must be lower than upper-bound temperature |
| swsHeatFluxEndEditErrorNoEntities | 3 = No entities specified |
| swsHeatFluxEndEditErrorNoEntityAtIndex | 1 = No entity passed at index |
| swsHeatFluxEndEditErrorSelectFace | 4 = Select a face |
| swsHeatFluxEndEditErrorSelectFacesOrShellEdge | 5 = Select a fade or shell edge |
| swsHeatFluxEndEditErrorSelectrVertexForSensorLocation | 6 = Select a vertex for the location of the sensor |
| swsHeatFluxEndEditErrorSuccessful | 0 = Successful |
| swsHeatFluxEndEditErrorThermostatForTransientStudiesOnly | 8 = Thermostat is allowed for transient studies only (not allowed for steady-state thermal studies) |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
