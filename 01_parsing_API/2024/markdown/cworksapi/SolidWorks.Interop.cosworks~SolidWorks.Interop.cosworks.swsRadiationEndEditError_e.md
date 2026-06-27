---
title: "swsRadiationEndEditError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsRadiationEndEditError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRadiationEndEditError_e.html"
---

# swsRadiationEndEditError_e Enumeration

Radiation editing errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsRadiationEndEditError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsRadiationEndEditError_e
```

### C#

```csharp
public enum swsRadiationEndEditError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsRadiationEndEditError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsRadiationEndEditErrorEmissivity | 6 = Emissivity must be between 0 and 1 |
| swsRadiationEndEditErrorEntityAlreadyExists | 2 = At least one entity is specified more than once |
| swsRadiationEndEditErrorNoEntities | 3 = No entities selected |
| swsRadiationEndEditErrorNoEntityAtIndex | 1 = No entity at the specified index |
| swsRadiationEndEditErrorSelectFace | 4 = Select a face |
| swsRadiationEndEditErrorSelectFaceOrEdge | 5 = Select a face or edge |
| swsRadiationEndEditErrorSuccessful | 0 = Successful |
| swsRadiationEndEditErrorViewFactor | 7 = View factor must be between 0 and 1 |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
