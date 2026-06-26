---
title: "swsTopologyStudy_StressConstraintErrors_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsTopologyStudy_StressConstraintErrors_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_StressConstraintErrors_e.html"
---

# swsTopologyStudy_StressConstraintErrors_e Enumeration

Topology study stress constraint result codes

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsTopologyStudy_StressConstraintErrors_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsTopologyStudy_StressConstraintErrors_e
```

### C#

```csharp
public enum swsTopologyStudy_StressConstraintErrors_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsTopologyStudy_StressConstraintErrors_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsTopoStressErrCode_ConstraintNotFound | 10 |
| swsTopoStressErrCode_InvalidComparator | 7 = Only swsTopologyStudyConstraintComparator_e .swsTopologyConstraintComparator_IsLessThan is available |
| swsTopoStressErrCode_InvalidComponent | 4 |
| swsTopoStressErrCode_InvalidConstraintValuationOption | 5 |
| swsTopoStressErrCode_InvalidConstraintValue | 2 |
| swsTopoStressErrCode_InvalidUnit | 6 |
| swsTopoStressErrCode_LessThanEqualToZeroConstraintValue | 3 |
| swsTopoStressErrCode_LessThanPermittedValue | 9 = Stress value must be above minimum model stress |
| swsTopoStressErrCode_OutOfRangePercentageValue | 11 = Percentage value for stress must be between 0 and 100 |
| swsTopoStressErrCode_SetOperationNotSupported | 1 = BeginEdit must be called before setting values |
| swsTopoStressErrCode_Success | 0 |
| swsTopoStressErrCode_UnitNotAvailable | 8 = SetUnit is available only when SetValuationPreference sets NValuationOption = swsTopologyStudyConstraintValuationOption_e .swsTopologyConstraintValuationOption_AbsValue |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
