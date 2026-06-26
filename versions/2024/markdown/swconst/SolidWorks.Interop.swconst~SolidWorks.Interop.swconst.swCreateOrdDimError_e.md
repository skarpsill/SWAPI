---
title: "swCreateOrdDimError_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCreateOrdDimError_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCreateOrdDimError_e.html"
---

# swCreateOrdDimError_e Enumeration

Errors when inserting an ordinate dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCreateOrdDimError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCreateOrdDimError_e
```

### C#

```csharp
public enum swCreateOrdDimError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCreateOrdDimError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCreateOrdDimErr_GenBadSel | 3 |
| swCreateOrdDimErr_GenExtraSelection | 6 |
| swCreateOrdDimErr_GenFailure | 7 |
| swCreateOrdDimErr_GenNeedModelLoaded | 4 |
| swCreateOrdDimErr_GenNoInternalDims | 2 |
| swCreateOrdDimErr_GenSamePartOnly | 5 |
| swCreateOrdDimErr_OrdBadDir | 9 |
| swCreateOrdDimErr_OrdDupInGroup | 8 |
| swCreateOrdDimErr_OrdFailure | 1 |
| swCreateOrdDimErr_Success | 0 |
| swCreateOrdDimErr_Undefined | -1 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
