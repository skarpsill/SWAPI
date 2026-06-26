---
title: "swsTopologyStudy_FrequencyConstraintErrors_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsTopologyStudy_FrequencyConstraintErrors_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_FrequencyConstraintErrors_e.html"
---

# swsTopologyStudy_FrequencyConstraintErrors_e Enumeration

Topology study frequency constraint result codes

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsTopologyStudy_FrequencyConstraintErrors_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsTopologyStudy_FrequencyConstraintErrors_e
```

### C#

```csharp
public enum swsTopologyStudy_FrequencyConstraintErrors_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsTopologyStudy_FrequencyConstraintErrors_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsTopoFreqErrCode_ComparatorDataIsNotSet | 12 |
| swsTopoFreqErrCode_ConstraintNotFound | 15 |
| swsTopoFreqErrCode_EnterRangeOfValues | 6 = If SetFrequencyData sets an element of the VarComparators array with swsTopologyStudyConstraintComparator_e .swsTopologyConstraintComparator_IsInBetween, then the corresponding value in the VarFrequencyValues array must be specified with a range of values, e.g., "200-400". In-between comparator requires a range of values (e.g., 200-400) |
| swsTopoFreqErrCode_FreqValuesDataIsNotSet | 13 |
| swsTopoFreqErrCode_HMSFreqLessThanLMSFreq | 4 = You must set the arrays in SetFrequencyData such that higher mode shapes have frequency values greater than those of lower mode shapes, i.e., VarModeShapes and VarFrequencyValues arrays must both be in increasing order |
| swsTopoFreqErrCode_InvalidArray | 14 |
| swsTopoFreqErrCode_InvalidComparatorData | 9 |
| swsTopoFreqErrCode_InvalidConstraintValue | 2 |
| swsTopoFreqErrCode_InvalidFreqValuesData | 10 |
| swsTopoFreqErrCode_InvalidModeShapeData | 8 |
| swsTopoFreqErrCode_LessThanEqualToZeroConstraintValue | 3 |
| swsTopoFreqErrCode_ModeShapeDataIsNotSet | 11 |
| swsTopoFreqErrCode_ModeShapesNotInAscendingOrder | 5 |
| swsTopoFreqErrCode_SetOperationNotSupported | 1 = BeginEdit must be called before setting values |
| swsTopoFreqErrCode_Success | 0 |
| swsTopoFreqErrCode_UnequalSizedArrays | 7 |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
