---
title: "swsTopologyStudy_MassConstraintErrors_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsTopologyStudy_MassConstraintErrors_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_MassConstraintErrors_e.html"
---

# swsTopologyStudy_MassConstraintErrors_e Enumeration

Topology study mass constraint result codes

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsTopologyStudy_MassConstraintErrors_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsTopologyStudy_MassConstraintErrors_e
```

### C#

```csharp
public enum swsTopologyStudy_MassConstraintErrors_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsTopologyStudy_MassConstraintErrors_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsTopoMassErrCode_ConstraintNotFound | 8 |
| swsTopoMassErrCode_GreaterThan100PercentApplied | 4 = You must specify a percentage of mass to remove that is less than or equal to 100 |
| swsTopoMassErrCode_GreaterThanTotalMassOfModel | 5 = You must specify a quantity of mass to remove that is less than or equal to the total mass of the model |
| swsTopoMassErrCode_InvalidConstraintValue | 2 |
| swsTopoMassErrCode_InvalidPreferenceOption | 7 |
| swsTopoMassErrCode_InvalidUnit | 6 |
| swsTopoMassErrCode_LessThanEqualToZeroConstraintValue | 3 |
| swsTopoMassErrCode_SetOperationNotSupported | 1 = BeginEdit must be called before setting values |
| swsTopoMassErrCode_Success | 0 |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
