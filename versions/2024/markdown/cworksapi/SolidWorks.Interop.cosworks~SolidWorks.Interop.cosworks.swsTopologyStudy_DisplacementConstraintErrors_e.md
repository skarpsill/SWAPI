---
title: "swsTopologyStudy_DisplacementConstraintErrors_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsTopologyStudy_DisplacementConstraintErrors_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_DisplacementConstraintErrors_e.html"
---

# swsTopologyStudy_DisplacementConstraintErrors_e Enumeration

Topology study displacement constraint result codes

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsTopologyStudy_DisplacementConstraintErrors_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsTopologyStudy_DisplacementConstraintErrors_e
```

### C#

```csharp
public enum swsTopologyStudy_DisplacementConstraintErrors_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsTopologyStudy_DisplacementConstraintErrors_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsTopoDispErrCode_CannotSetVertex | 10 = SetVertex is available only when LocationOption = swsTopologyStudyDisplacementConstraintLocationOption_e .swsTopologyDisplacementConstraintLocationOption_UserDefine |
| swsTopoDispErrCode_ConstraintNotFound | 17 = Constraint does not exist |
| swsTopoDispErrCode_CoordinateSysInvalidOption | 14 = Option must be in swsTopologyStudyDisplacementCoordinateSysOption_e |
| swsTopoDispErrCode_CoordinateSysInvalidSelection | 15 = Wrong coordinate system dispatch was passed |
| swsTopoDispErrCode_CoordinateSysNAError | 13 = SetCoordinateSystem is available only when SetCoordinateSystemPreference sets NCSPreference = swsTopologyStudyDisplacementCoordinateSysOption_e .swsTopologyDisplacementCoordinateSysOption_UserDefine |
| swsTopoDispErrCode_CoordinateSysNotSelected | 16 = Coordinate system has not been set |
| swsTopoDispErrCode_InvalidArray | 18 = Invalid input array |
| swsTopoDispErrCode_InvalidComparator | 7 = Input comparator must be in swsTopologyStudyConstraintComparator_e |
| swsTopoDispErrCode_InvalidComponent | 4 = Component type must be in swsTopologyStudyDisplacementComponentType_e |
| swsTopoDispErrCode_InvalidConstraintValuationOption | 5 = Valuation option must be in swsTopologyStudyConstraintValuationOption_e |
| swsTopoDispErrCode_InvalidConstraintValue | 2 = Input value contains invalid characters |
| swsTopoDispErrCode_InvalidLocationOption | 11 = Location option must be in swsTopologyDisplacementConstraintLocationOption_e |
| swsTopoDispErrCode_InvalidSelectionForVertex | 9 = Wrong vertex dispatch has been passed |
| swsTopoDispErrCode_InvalidUnit | 6 = Input unit must be in swsLinearUnit_e |
| swsTopoDispErrCode_InvalidVertexCount | 12 = You cannot define this displacement constraint when SetLocationPreference sets NLocationPreference = swsTopologyStudyDisplacementConstraintLocationOption_e.swsTopologyDisplacementConstraintLocationOption_UserDefine and vertex count != 1 |
| swsTopoDispErrCode_LessThanEqualToZeroConstraintValue | 3 = Less than or equal to zero value is invalid |
| swsTopoDispErrCode_SetOperationNotSupported | 1 = BeginEdit must be called before setting values |
| swsTopoDispErrCode_Success | 0 |
| swsTopoDispErrCode_UnitNotAvailable | 8 = SetUnit is available only when SetValuationPreference sets NValuationOption = swsTopologyStudyConstraintValuationOption_e .swsTopologyConstraintValuationOption_AbsValue |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
