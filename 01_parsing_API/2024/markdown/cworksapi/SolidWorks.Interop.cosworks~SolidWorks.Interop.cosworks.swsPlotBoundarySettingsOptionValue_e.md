---
title: "swsPlotBoundarySettingsOptionValue_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsPlotBoundarySettingsOptionValue_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsPlotBoundarySettingsOptionValue_e.html"
---

# swsPlotBoundarySettingsOptionValue_e Enumeration

Model boundary plot display options

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsPlotBoundarySettingsOptionValue_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsPlotBoundarySettingsOptionValue_e
```

### C#

```csharp
public enum swsPlotBoundarySettingsOptionValue_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsPlotBoundarySettingsOptionValue_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsPlotBoundaryMesh | 2 = Superimpose the selected result plot on the mesh plot |
| swsPlotBoundaryModel | 1 = Display the boundary edges of the model |
| swsPlotBoundaryNone | 0 = Do not display the boundary edges of the model |
| swsPlotBoundaryTranslucentPartColor | 4 = Display all hidden or excluded parts in their shaded mode colors; valid only when hidden or excluded bodies exist |
| swsPlotBoundaryTranslucentSingleColor | 3 = Display all hidden or excluded parts in a single color; valid only when hidden or excluded bodies exist |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
