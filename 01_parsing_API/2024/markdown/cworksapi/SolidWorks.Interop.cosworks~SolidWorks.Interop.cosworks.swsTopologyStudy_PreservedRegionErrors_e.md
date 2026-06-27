---
title: "swsTopologyStudy_PreservedRegionErrors_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsTopologyStudy_PreservedRegionErrors_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_PreservedRegionErrors_e.html"
---

# swsTopologyStudy_PreservedRegionErrors_e Enumeration

Topology study preserved region manufacturing control result codes

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsTopologyStudy_PreservedRegionErrors_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsTopologyStudy_PreservedRegionErrors_e
```

### C#

```csharp
public enum swsTopologyStudy_PreservedRegionErrors_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsTopologyStudy_PreservedRegionErrors_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsTopoPRErrCode_InvalidAreaDepth | 3 = Area depth must be > 0 |
| swsTopoPRErrCode_InvalidAreaDepthUnit | 4 |
| swsTopoPRErrCode_InvalidArray | 5 |
| swsTopoPRErrCode_InvalidEntities | 6 = Input array contains non-face entities |
| swsTopoPRErrCode_InvalidFaceCount | 2 = You must select at least one face |
| swsTopoPRErrCode_SetOperationNotSupported | 1 = BeginEdit must be called before setting values |
| swsTopoPRErrCode_Success | 0 |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
