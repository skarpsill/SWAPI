---
title: "swsTopologyStudy_ThicknessControlErrors_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsTopologyStudy_ThicknessControlErrors_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_ThicknessControlErrors_e.html"
---

# swsTopologyStudy_ThicknessControlErrors_e Enumeration

Topology study thickness manufacturing control result codes

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsTopologyStudy_ThicknessControlErrors_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsTopologyStudy_ThicknessControlErrors_e
```

### C#

```csharp
public enum swsTopologyStudy_ThicknessControlErrors_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsTopologyStudy_ThicknessControlErrors_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsTopoTCErrCode_InvalidThickness | 2 = Thickness must be > 0 |
| swsTopoTCErrCode_InvalidThicknessUnit | 3 |
| swsTopoTCErrCode_SetOperationNotSupported | 1 = BeginEdit must be called before setting values |
| swsTopoTCErrCode_Success | 0 |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
