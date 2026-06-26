---
title: "swSMBendState_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swSMBendState_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSMBendState_e.html"
---

# swSMBendState_e Enumeration

Bend state values for a sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swSMBendState_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swSMBendState_e
```

### C#

```csharp
public enum swSMBendState_e : System.Enum
```

### C++/CLI

```cpp
public enum class swSMBendState_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swSMBendStateFlattened | 2 = The bends are flattened; the model is rolled back to just after a FlattenBends feature, but just before the corresponding ProcessBends feature |
| swSMBendStateFolded | 3 = The bends are folded; the model is rolled back to just after a FlattenBends ProcessBends feature pair |
| swSMBendStateNone | 0 = Not a sheet metal part; no SheetMetal features present |
| swSMBendStateSharps | 1 = The bends are in their sharp state; the part is rolled back to just before the first FlattenBends feature |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
