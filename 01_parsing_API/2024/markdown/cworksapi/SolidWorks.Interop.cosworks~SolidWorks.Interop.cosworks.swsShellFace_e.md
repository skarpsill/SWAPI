---
title: "swsShellFace_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsShellFace_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsShellFace_e.html"
---

# swsShellFace_e Enumeration

Options for evaluating membrane and bending components of study result quantities

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsShellFace_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsShellFace_e
```

### C#

```csharp
public enum swsShellFace_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsShellFace_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsShellFace_Bending | 3 = Bending component only |
| swsShellFace_Bottom | 1 = Total (bending + membrane) at the bottom face; for a composite shell, this is the bottom face of the selected ply under Composite Options |
| swsShellFace_Membrane | 2 = Membrane component only |
| swsShellFace_Top | 0 = Total (bending + membrane) at the top face; for a composite shell, this is the top face of the selected ply under Composite Options |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
