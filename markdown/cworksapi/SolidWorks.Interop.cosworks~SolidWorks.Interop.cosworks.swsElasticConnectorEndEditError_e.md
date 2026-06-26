---
title: "swsElasticConnectorEndEditError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsElasticConnectorEndEditError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsElasticConnectorEndEditError_e.html"
---

# swsElasticConnectorEndEditError_e Enumeration

Elastic connector editing errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsElasticConnectorEndEditError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsElasticConnectorEndEditError_e
```

### C#

```csharp
public enum swsElasticConnectorEndEditError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsElasticConnectorEndEditError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsElasticConnectorEndEditErrorBodyExcludedFromAnalysis | 10 = Selected entity is on a body excluded from analysis |
| swsElasticConnectorEndEditErrorEntityAlreadyAdded | 2 = Entity already added to the elastic connector |
| swsElasticConnectorEndEditErrorHasBeamBody | 8 = Connector has a beam body |
| swsElasticConnectorEndEditErrorHasMassElement | 9 = Connector has mass element |
| swsElasticConnectorEndEditErrorNoEntityAtIndex | 1 = No entity at the specified index |
| swsElasticConnectorEndEditErrorNullEntity | 11 = Entity is NULL |
| swsElasticConnectorEndEditErrorSelectEntity | 7 = Select an entity |
| swsElasticConnectorEndEditErrorSelectFace | 3 = Select a face |
| swsElasticConnectorEndEditErrorSelectNonNegativeValueForNormalOrShearStiffness | 5= Select a non-negative value for normal or shear stiffness |
| swsElasticConnectorEndEditErrorSelectNonZeroValueForNormalOrShearStiffness | 6 = Select a non-0 value for normal or shear stiffness |
| swsElasticConnectorEndEditErrorSelectPlanarFace | 4 = Select a planar face |
| swsElasticConnectorEndEditErrorSuccessful | 0 = Successful |

## Remarks

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
