---
title: "swsMeshState_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsMeshState_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMeshState_e.html"
---

# swsMeshState_e Enumeration

Mesh states

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsMeshState_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsMeshState_e
```

### C#

```csharp
public enum swsMeshState_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsMeshState_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsMeshStateExistsAndCurrent | 1 = Mesh exists and it is current |
| swsMeshStateExistsAndNotCurrent | 2 = Mesh exists but it is not current |
| swsMeshStateFailed | 3 = Mesh failed |
| swsMeshStateInterrupted | 4 = Mesh interrupted |
| swsMeshStateNoMesh | 0 = No mesh exists |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
