---
title: "swsShellOffsetOption_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsShellOffsetOption_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsShellOffsetOption_e.html"
---

# swsShellOffsetOption_e Enumeration

Shell offset options

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsShellOffsetOption_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsShellOffsetOption_e
```

### C#

```csharp
public enum swsShellOffsetOption_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsShellOffsetOption_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsShellOffsetOption_Bottom | 2 = Align the mesh with the bottom surface of the shell |
| swsShellOffsetOption_Middle | 0 = Align the mesh with the middle surface of the shell |
| swsShellOffsetOption_SpecifyRatio | 3 = Align the mesh with a reference surface defined by an offset value that is a fraction of the total thickness of the shell; set ICWShell::ShellOffsetValue to a non-zero number between -0.5 and 0.5 |
| swsShellOffsetOption_Top | 1 = Align the mesh with the top surface of the shell |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
