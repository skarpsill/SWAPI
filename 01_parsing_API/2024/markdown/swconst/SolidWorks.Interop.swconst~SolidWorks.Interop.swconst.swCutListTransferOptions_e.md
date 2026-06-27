---
title: "swCutListTransferOptions_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCutListTransferOptions_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCutListTransferOptions_e.html"
---

# swCutListTransferOptions_e Enumeration

Options for transferring the cut list when saving a weldment member, surface body, or solid body to another part.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCutListTransferOptions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCutListTransferOptions_e
```

### C#

```csharp
public enum swCutListTransferOptions_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCutListTransferOptions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCutListTransferOptions_CutListProperties | 2 = Transfer to a cut list in the new part |
| swCutListTransferOptions_FileProperties | 1 = Transfer to file properties of the new part |
| swCutListTransferOptions_None | 0 = No transfer |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
