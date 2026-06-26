---
title: "swMatesDefaultMisalignment_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swMatesDefaultMisalignment_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMatesDefaultMisalignment_e.html"
---

# swMatesDefaultMisalignment_e Enumeration

Concentric mate misalignment options.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swMatesDefaultMisalignment_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swMatesDefaultMisalignment_e
```

### C#

```csharp
public enum swMatesDefaultMisalignment_e : System.Enum
```

### C++/CLI

```cpp
public enum class swMatesDefaultMisalignment_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swMatesAlignFirstConcentricMate | 0; Align this mate; align the mate currently being edited to be exactly concentric, causing the linked mate to be misaligned |
| swMatesAlignSecondConcentricMate | 1; Align linked mate; aligns the linked mate to be exactly concentric, causing the currently edited mate to be misaligned |
| swMatesSymmetric | 2; Symmetric; misaligns both concentric mates, splitting the deviation evenly between mates |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
