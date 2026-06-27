---
title: "swsTopologyStudy_MinMaxDisplacementGoalErrors_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsTopologyStudy_MinMaxDisplacementGoalErrors_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_MinMaxDisplacementGoalErrors_e.html"
---

# swsTopologyStudy_MinMaxDisplacementGoalErrors_e Enumeration

Topology study minimize maximum displacement goal result codes

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsTopologyStudy_MinMaxDisplacementGoalErrors_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsTopologyStudy_MinMaxDisplacementGoalErrors_e
```

### C#

```csharp
public enum swsTopologyStudy_MinMaxDisplacementGoalErrors_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsTopologyStudy_MinMaxDisplacementGoalErrors_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsTopoDGErrCode_CoordinateSysInvalidOption | 4 |
| swsTopoDGErrCode_CoordinateSysInvalidSelection | 5 |
| swsTopoDGErrCode_CoordinateSysNAError | 3 = SetCoordinateSystem is available only when SetCoordinateSystemPreference sets NCSPreference = swsTopologyStudyDisplacementCoordinateSysOption_e .swsTopologyDisplacementCoordinateSysOption_UserDefine |
| swsTopoDGErrCode_CoordinateSysNotSelected | 6 |
| swsTopoDGErrCode_InvalidArray | 8 |
| swsTopoDGErrCode_InvalidComponent | 2 |
| swsTopoDGErrCode_InvalidEntities | 9 |
| swsTopoDGErrCode_InvalidVertexCount | 7 = You must specify at least one vertex for this goal |
| swsTopoDGErrCode_SetOperationNotSupported | 1 = BeginEdit must be called before setting values |
| swsTopoDGErrCode_Success | 0 |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
