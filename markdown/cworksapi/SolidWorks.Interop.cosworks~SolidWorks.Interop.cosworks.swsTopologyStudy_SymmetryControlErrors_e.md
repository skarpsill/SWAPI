---
title: "swsTopologyStudy_SymmetryControlErrors_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsTopologyStudy_SymmetryControlErrors_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_SymmetryControlErrors_e.html"
---

# swsTopologyStudy_SymmetryControlErrors_e Enumeration

Topology study symmetry manufacturing control result codes

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsTopologyStudy_SymmetryControlErrors_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsTopologyStudy_SymmetryControlErrors_e
```

### C#

```csharp
public enum swsTopologyStudy_SymmetryControlErrors_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsTopologyStudy_SymmetryControlErrors_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsTopoSCErrCode_IncorrectPlaneSelectionsForGivenSymmetryType | 4 = For swsTopologySymmetryControlOption_e : swsTopologySymmetryControlType_HalfSymmetry, a single plane can be selected swsTopologySymmetryControlType_QuarterSymmetry, two planes can be selected swsTopologySymmetryControlType_OneEighthSymmetry, three planes can be selected |
| swsTopoSCErrCode_InvalidEntitySelectedAsPlane | 2 |
| swsTopoSCErrCode_InvalidTypeSelected | 3 |
| swsTopoSCErrCode_SetOperationNotSupported | 1 = BeginEdit must be called before setting values |
| swsTopoSCErrCode_SetSymmetryTypeBeforeSelectingPlane | 5 |
| swsTopoSCErrCode_Success | 0 |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
