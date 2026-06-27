---
title: "swConcentricAlignmentType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swConcentricAlignmentType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConcentricAlignmentType_e.html"
---

# swConcentricAlignmentType_e Enumeration

Concentric mate alignment types.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swConcentricAlignmentType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swConcentricAlignmentType_e
```

### C#

```csharp
public enum swConcentricAlignmentType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swConcentricAlignmentType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swConcentricAlignConcentric | 0; Align both mates to be exactly concentric; neither mate is misaligned |
| swConcentricAlignLinkedMate | 2; Align the linked mate to be exactly concentric, causing the currently edited mate to be misaligned |
| swConcentricAlignSymmetric | 3; Misalign both concentric mates, splitting the misalignment deviation evenly between mates |
| swConcentricAlignThisMate | 1; Align the mate currently being edited to be exactly concentric, causing the linked mate to be misaligned |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
