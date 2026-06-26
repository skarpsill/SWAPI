---
title: "swSensorType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swSensorType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSensorType_e.html"
---

# swSensorType_e Enumeration

Types of sensor.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swSensorType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swSensorType_e
```

### C#

```csharp
public enum swSensorType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swSensorType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swSensorDimension | 2 = Measurement (dimension) sensor |
| swSensorInterfaceDetection | 3 = Interference detection sensor; Obsolete |
| swSensorMassProperty | 1 = Obsolete |
| swSensorProximity | 5 = Obsolete |
| swSensorSimulation | 0 = Obsolete |

## Remarks

As of SOLIDWORKS 2009 SP02, only sensors of type swSensorDimension are supported. Non-dimension measurement sensors (=4) and all of the other sensor types are no longer supported.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
