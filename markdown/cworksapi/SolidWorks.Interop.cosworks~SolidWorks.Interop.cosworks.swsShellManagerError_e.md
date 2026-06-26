---
title: "swsShellManagerError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsShellManagerError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsShellManagerError_e.html"
---

# swsShellManagerError_e Enumeration

Shell creation errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsShellManagerError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsShellManagerError_e
```

### C#

```csharp
public enum swsShellManagerError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsShellManagerError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsShellManagerErrorCannotApplyShellForMesh | 2 = Shell cannot be applied for this mesh type |
| swsShellManagerErrorCannotApplyShellForStudy | 1 = Shell cannot be applied for this study type |
| swsShellManagerErrorEmptyArray | 3 = Empty array; no faces selected |
| swsShellManagerErrorFaceAlreadyDefinedAsShell | 6 = A face is already defined as a shell |
| swsShellManagerErrorFaceAlreadyExists | 7 = At least on face is specified more than once |
| swsShellManagerErrorInvalidArray | 4 = Invalid array |
| swsShellManagerErrorSelectFacesOnly | 5 = Select faces only |
| swsShellManagerErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
