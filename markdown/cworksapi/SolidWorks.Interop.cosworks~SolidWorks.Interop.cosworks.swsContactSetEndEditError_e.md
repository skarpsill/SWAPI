---
title: "swsContactSetEndEditError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsContactSetEndEditError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactSetEndEditError_e.html"
---

# swsContactSetEndEditError_e Enumeration

Contact set editing errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsContactSetEndEditError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsContactSetEndEditError_e
```

### C#

```csharp
public enum swsContactSetEndEditError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsContactSetEndEditError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsContactSetEndEditErrorBondTouchingFacesInDropTestStudies | 15 = In drop test studies, you can only bond touching faces |
| swsContactSetEndEditErrorContactSetsMustBeUnique | 13 = For thermal resistance, contact sets must be unique; use the split-line features to split common faces; you may need to redefine existing contact sets |
| swsContactSetEndEditErrorEntityAlreadySpecified | 2 = At least one entity is specified more than once |
| swsContactSetEndEditErrorIncorrectCoefficientFriction | 10 = Coefficient of friction must be >= 0 and <= 1.0 |
| swsContactSetEndEditErrorInvalidContactSetType | 3 = Invalid contact set type |
| swsContactSetEndEditErrorInvalidOption | 4 = Invalid option |
| swsContactSetEndEditErrorNodeToNodeContactAndSourceTargetFaces | 14 = Node to node contact requires that source and target faces touch |
| swsContactSetEndEditErrorNoEntityAtIndex | 1 = No entity is passed at index |
| swsContactSetEndEditErrorOnlyFacesAllowedForTarget | 7 = Only faces are allowed for target |
| swsContactSetEndEditErrorShrinkFitAndnterferingSourceTargetBodies | 16 = Shrink fit requires that source and target bodies interfere |
| swsContactSetEndEditErrorSpecifyFacesEdgesOrVerticesForSource | 5 = Specify faces, edges, or vertices for source |
| swsContactSetEndEditErrorSpecifyOneTargetPlaneForVirtualWall | 6 = Specify only one target plane for virtual wall |
| swsContactSetEndEditErrorStiffnessCannotBeNegative | 8 = Stiffness cannot be negative |
| swsContactSetEndEditErrorStiffnessMustBePositive | 9 = Specify a positive value for at least one of the stiffness parameters |
| swsContactSetEndEditErrorSuccessful | 0 = Successful |
| swsContactSetEndEditErrorThermalResistanceMustBePositive | 12 = Thermal resistance must have a positive value |
| swsContactSetEndEditErrorVerticesAndEdgesForBondingAndSurfaceContacts | 11 = Vertices and edges are allowed as source entities only for bonding and surface contact conditions |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
