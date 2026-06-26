---
title: "swsTopologyStudy_FOSConstraintErrors_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsTopologyStudy_FOSConstraintErrors_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_FOSConstraintErrors_e.html"
---

# swsTopologyStudy_FOSConstraintErrors_e Enumeration

Topology study Factor of Safety constraint result codes

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsTopologyStudy_FOSConstraintErrors_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsTopologyStudy_FOSConstraintErrors_e
```

### C#

```csharp
public enum swsTopologyStudy_FOSConstraintErrors_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsTopologyStudy_FOSConstraintErrors_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsTopoFOSErrCode_ConstraintNotFound | 7 |
| swsTopoFOSErrCode_InvalidComparator | 6 |
| swsTopoFOSErrCode_InvalidComponent | 4 |
| swsTopoFOSErrCode_InvalidConstraintValue | 2 |
| swsTopoFOSErrCode_LessThanEqualToZeroConstraintValue | 3 |
| swsTopoFOSErrCode_MaterialWithInvalidYieldStrength | 8 = Cannot define FOS for model with material which has invalid yield strength; apply material with valid yield strength |
| swsTopoFOSErrCode_OutOfRangeValue | 5 = Value must be between 1.0 and 10000.0, inclusive |
| swsTopoFOSErrCode_SetOperationNotSupported | 1 = BeginEdit must be called before setting values |
| swsTopoFOSErrCode_Success | 0 |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
