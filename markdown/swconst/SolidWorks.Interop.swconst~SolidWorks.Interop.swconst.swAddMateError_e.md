---
title: "swAddMateError_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swAddMateError_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAddMateError_e.html"
---

# swAddMateError_e Enumeration

Status after adding or editing a mate.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swAddMateError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swAddMateError_e
```

### C#

```csharp
public enum swAddMateError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swAddMateError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAddMateError_ErrorUknown | 0 = Unknown error occurred |
| swAddMateError_IncorrectAlignment | 3 = Unknown mate alignment or mate alignment is not present in swMateAlign_e |
| swAddMateError_IncorrectGearRatios | 6 = Mate gear ratios are invalid |
| swAddMateError_IncorrectMateType | 2 = Unknown mate type or mate type not present in swMateType_e |
| swAddMateError_IncorrectSelections | 4 = Incorrect selections for mate |
| swAddMateError_NoError | 1 = Success, no error |
| swAddMateError_OverDefinedAssembly | 5 = Mate is over-defining the assembly |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
