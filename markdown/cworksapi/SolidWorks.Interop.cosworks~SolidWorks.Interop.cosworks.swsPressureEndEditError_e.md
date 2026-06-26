---
title: "swsPressureEndEditError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsPressureEndEditError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsPressureEndEditError_e.html"
---

# swsPressureEndEditError_e Enumeration

Pressure editing errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsPressureEndEditError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsPressureEndEditError_e
```

### C#

```csharp
public enum swsPressureEndEditError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsPressureEndEditError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsPressureEndEditErrorEntityAlreadyAdded | 2 = Entity already added to pressure |
| swsPressureEndEditErrorNoEntities | 3 = No entities selected |
| swsPressureEndEditErrorNoEntityAtIndex | 1 = No entity passed at index |
| swsPressureEndEditErrorRefGeomPreExist | 6 = Reference geometry already select in list of selected entities |
| swsPressureEndEditErrorSelectCoordinateSystem | 8 = Select a coordinate system |
| swsPressureEndEditErrorSelectFaceEdgePlaneOrAxis | 7 = Select a face, edge, plane, or axis for reference geometry |
| swsPressureEndEditErrorSelectFaceOrShellEdge | 5 = Select face or shell edge |
| swsPressureEndEditErrorSelectFacesOrShellEdges | 4 = Select faces or shell edges |
| swsPressureEndEditErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
