---
title: "swsProbePostResultOption_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsProbePostResultOption_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsProbePostResultOption_e.html"
---

# swsProbePostResultOption_e Enumeration

Results probe options

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsProbePostResultOption_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsProbePostResultOption_e
```

### C#

```csharp
public enum swsProbePostResultOption_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsProbePostResultOption_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsProbePostResultOption_AtDistance | 3 = Measure the distance between two nodes; available for mesh and displacement plots only |
| swsProbePostResultOption_AtLocation | 0 = Probe results for individual nodes or elements selected in the graphics area |
| swsProbePostResultOption_AtNodeElemNumber | 4 = Probe results at a specified node or element |
| swsProbePostResultOption_FromSensors | 1 = Probe results at locations stored in sensor lists; you must define Workflow Sensors to create a sensor list |
| swsProbePostResultOption_OnSelectedEntities | 2 = Probe results for all nodes or elements on selected faces, edges, or vertices |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
