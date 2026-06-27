---
title: "swsShellEndEditError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsShellEndEditError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsShellEndEditError_e.html"
---

# swsShellEndEditError_e Enumeration

Shell editing errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsShellEndEditError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsShellEndEditError_e
```

### C#

```csharp
public enum swsShellEndEditError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsShellEndEditError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsShellEndEditErrorFaceAlreadyDefinedAsShell | 6 = This face is already defined as shell |
| swsShellEndEditErrorFaceAlreadyExists | 5 = At least one face is specified more than once |
| swsShellEndEditErrorFormulation | 2 = Specify either 0 or 1 for formulation |
| swsShellEndEditErrorNoEntitySelected | 7 = Shell cannot be edited. No entity selected |
| swsShellEndEditErrorNotEntityAtIndex | 3 = No entity at index passed for removal |
| swsShellEndEditErrorOffsetOption | 9 = Specify shell offset option |
| swsShellEndEditErrorOffsetValue | 10 = Specify shell offset value |
| swsShellEndEditErrorSelectFace | 4 = Specify face for entity |
| swsShellEndEditErrorShellThickness | 1 = Specify a number between 1e-007 and 1e+006 for shell thickness |
| swsShellEndEditErrorSuccessful | 0 = Successful |
| swsShellEndEditErrorUnit | 8 = Specify 0 to 5 for unit |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
