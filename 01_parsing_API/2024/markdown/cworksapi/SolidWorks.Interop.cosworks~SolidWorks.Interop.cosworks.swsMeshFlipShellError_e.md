---
title: "swsMeshFlipShellError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsMeshFlipShellError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMeshFlipShellError_e.html"
---

# swsMeshFlipShellError_e Enumeration

Flipping shell elements errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsMeshFlipShellError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsMeshFlipShellError_e
```

### C#

```csharp
public enum swsMeshFlipShellError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsMeshFlipShellError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsMeshFlipShellErrorEmptyArray | 2 = No faces selected (empty array) |
| swsMeshFlipShellErrorInvalidArray | 1 = Invalid array |
| swsMeshFlipShellErrorMeshInformationNotFound | 5 = Mesh information not found |
| swsMeshFlipShellErrorNotShell | 3 = Mesh is not shell type |
| swsMeshFlipShellErrorSelectFaces | 4 = Select faces |
| swsMeshFlipShellErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
