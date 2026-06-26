---
title: "swsThermalOption_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsThermalOption_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsThermalOption_e.html"
---

# swsThermalOption_e Enumeration

Thermal options for studies

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsThermalOption_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsThermalOption_e
```

### C#

```csharp
public enum swsThermalOption_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsThermalOption_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsThermalOption_InputTemperature | 0 = Considers the prescribed temperatures that are defined for the model |
| swsThermalOption_TemperatureFromFlow | 2 = Reads the temperature values from a SOLIDWORKS Flow Simulation results file (not available for 2D simplification studies) |
| swsThermalOption_TemperatureFromThermalStudy | 1 = Reads the temperature values from a thermal study |

## Remarks

This enumerator corresponds to the Thermal options radio buttons on the Flow/Thermal Effects tab of a study's properties dialog box.

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
