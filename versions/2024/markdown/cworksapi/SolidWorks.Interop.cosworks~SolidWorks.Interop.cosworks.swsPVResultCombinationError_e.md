---
title: "swsPVResultCombinationError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsPVResultCombinationError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsPVResultCombinationError_e.html"
---

# swsPVResultCombinationError_e Enumeration

Errors when combining results of Pressure Vessel Design studies

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsPVResultCombinationError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsPVResultCombinationError_e
```

### C#

```csharp
public enum swsPVResultCombinationError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsPVResultCombinationError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsPVResultCombinationError_AtleastTwoItemsNeeded | 2 = You need to specify at least two studies and multiplication factors |
| swsPVResultCombinationError_CombineAnalysisNotDone | 7 = The analysis was not done |
| swsPVResultCombinationError_CombineIncompatibleConfiguration | 10 = Incompatible configurations |
| swsPVResultCombinationError_CombineIncompatibleConnectors | 15 = Incompatible connectors |
| swsPVResultCombinationError_CombineIncompatibleContact | 14 = Incompatible contacts |
| swsPVResultCombinationError_CombineIncompatibleMesh | 9 = Incompatible meshes |
| swsPVResultCombinationError_CombineIncompatiblePlanarType | 16 = Incompatible planar types |
| swsPVResultCombinationError_CombineIncompatibleRestraints | 11 = Incompatible restraints |
| swsPVResultCombinationError_CombineIncompatibleResults | 8 = Incompatible results |
| swsPVResultCombinationError_CombineIncompatibleShellsMaterials | 13 = Incompatible shell materials |
| swsPVResultCombinationError_CombineIncompatibleSolidsMaterials | 12 = Incompatible solid materials |
| swsPVResultCombinationError_InvalidFactors | 5 = One or more multiplication factors are invalid |
| swsPVResultCombinationError_InvalidStudy | 6 = One or more studies are invalid |
| swsPVResultCombinationError_ItemsNotSameInNumber | 4 = Number of elements in the multiplication factors and study names arrays are not the same |
| swsPVResultCombinationError_NoError | 0 = Successful |
| swsPVResultCombinationError_NotAvailable | 1 = Result combination is not available for this study |
| swsPVResultCombinationError_StudyNamesNotProper | 3 = Study names are not valid |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
