---
title: "swCreateAngRunDimError_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCreateAngRunDimError_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCreateAngRunDimError_e.html"
---

# swCreateAngRunDimError_e Enumeration

Statuses when inserting an angular running dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCreateAngRunDimError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCreateAngRunDimError_e
```

### C#

```csharp
public enum swCreateAngRunDimError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCreateAngRunDimError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCreateAngRunDimError_GenFailure | 0 = Cannot create this angular running dimension |
| swCreateAngRunDimError_IdenticalDimension | 2 = Identical dimensions cannot be created in the same angular running dimension |
| swCreateAngRunDimError_SelectAnotherEntity | 3 = Cannot use the selected entity to create this angular running dimension; select another entity |
| swCreateAngRunDimError_Success | 1 |
| swCreateAngRunDimError_Undefined | -1 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
