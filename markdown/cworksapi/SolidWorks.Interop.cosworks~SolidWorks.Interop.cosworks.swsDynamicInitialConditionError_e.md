---
title: "swsDynamicInitialConditionError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsDynamicInitialConditionError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDynamicInitialConditionError_e.html"
---

# swsDynamicInitialConditionError_e Enumeration

Errors for dynamic initial conditions

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsDynamicInitialConditionError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsDynamicInitialConditionError_e
```

### C#

```csharp
public enum swsDynamicInitialConditionError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsDynamicInitialConditionError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsDynamicInitialConditionError_AllValuesZero | 13 = Values are zeros |
| swsDynamicInitialConditionError_CheckAtleastOneComp | 12 = Select at least one component for the inital condition |
| swsDynamicInitialConditionError_CheckOnlyThirdComp | 14 = Select only the third direction for a reference edge, and specify a non-zero third value |
| swsDynamicInitialConditionError_InvalidEntityArray | 2 = Unable to read data in the entity array, or the entity array is NULL |
| swsDynamicInitialConditionError_InvalidRefGeom | 7 = The reference geometry is NULL |
| swsDynamicInitialConditionError_InvalidType | 11 = The dynamic initial condition type must be specified using an option from swsDynamicInitialConditionType_e |
| swsDynamicInitialConditionError_NoError | 0 = Successful |
| swsDynamicInitialConditionError_NoFacesOnBeamsAllowed | 5 = Do not select faces on beams |
| swsDynamicInitialConditionError_NotAvailable | 1 = Dynamic initial condition is not available for this study type |
| swsDynamicInitialConditionError_OnlyEdgePlaneOrFaceForReference | 9 = Select only an edge, plane, or face for the reference entity |
| swsDynamicInitialConditionError_OnlyFlatFaceOrStraightEdge | 10 = Select only a flat face, straight edge, or plane as the reference entity |
| swsDynamicInitialConditionError_RefGeomAlreadySelected | 8 = The reference geometry is already selected |
| swsDynamicInitialConditionError_SelectOnlyBeams | 4 = Select only beam bodies |
| swsDynamicInitialConditionError_SelectOnlyFaceBodyOrComps | 6 = Select only faces, bodies, or components |
| swsDynamicInitialConditionError_SelectOnlyJoints | 3 = Select only joints |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
