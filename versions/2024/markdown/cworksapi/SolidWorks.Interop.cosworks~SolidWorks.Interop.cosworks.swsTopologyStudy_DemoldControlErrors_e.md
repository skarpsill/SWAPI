---
title: "swsTopologyStudy_DemoldControlErrors_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsTopologyStudy_DemoldControlErrors_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_DemoldControlErrors_e.html"
---

# swsTopologyStudy_DemoldControlErrors_e Enumeration

Topology study de-mold manufacturing control result codes

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsTopologyStudy_DemoldControlErrors_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsTopologyStudy_DemoldControlErrors_e
```

### C#

```csharp
public enum swsTopologyStudy_DemoldControlErrors_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsTopologyStudy_DemoldControlErrors_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsTopoDCErrCode_EdgeSelectionNotAvailable | 8 = Edge selection is not available for swsTopologyStudyDemoldDirectionOption_e .swsTopologyDemoldDirection_TwoDirectionMidPlane de-mold direction option when SetAutoDetermineCentralMidPlane sets BFlag = 0 |
| swsTopoDCErrCode_EdgeSelectionRequired | 9 = Edge selection is required for all de-mold direction options except swsTopologyStudyDemoldDirectionOption_e.swsTopologyDemoldDirection_TwoDirectionMidPlane when SetAutoDetermineCentralMidPlane sets BFlag = 0 |
| swsTopoDCErrCode_InvalidDirectionOptionSelected | 3 |
| swsTopoDCErrCode_InvalidEntitySelectedAsEdge | 2 |
| swsTopoDCErrCode_InvalidEntitySelectedAsPlane | 4 |
| swsTopoDCErrCode_NotAvailableForCurrentDirectionOption | 5 |
| swsTopoDCErrCode_PlaneSelectionNotAvailable | 6 = Plane selection is available only for swsTopologyStudyDemoldDirectionOption_e.swsTopologyDemoldDirection_TwoDirectionMidPlane de-mold direction option when SetAutoDetermineCentralMidPlane sets BFlag = 0 |
| swsTopoDCErrCode_PlaneSelectionRequired | 7 = Plane selection is required for swsTopologyStudyDemoldDirectionOption_e.swsTopologyDemoldDirection_TwoDirectionMidPlane de-mold direction option when SetAutoDetermineCentralMidPlane sets BFlag = 0 |
| swsTopoDCErrCode_SetOperationNotSupported | 1 = BeginEdit must be called before setting values |
| swsTopoDCErrCode_Success | 0 |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
