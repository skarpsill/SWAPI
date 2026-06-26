---
title: "SwDmMassPropError Enumeration"
project: "SOLIDWORKS Document Manager API Help"
interface: "SwDmMassPropError"
member: ""
kind: "enum"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmMassPropError.html"
---

# SwDmMassPropError Enumeration

Mass property errors.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum SwDmMassPropError
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As SwDmMassPropError
```

### C#

```csharp
public enum SwDmMassPropError : System.Enum
```

### C++/CLI

```cpp
public enum class SwDmMassPropError : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDmMassPropErrorEarlierVersion | 1 = Mass properties are stored as document properties in version 2500 and later |
| swDmMassPropErrorNoData | 2 = Reason for error could be that mass properties were not calculated before the part was saved |
| swDmMassPropErrorNone | 0 = Success |
| swDmMassPropErrorUnknown | 3 = Unknown error |

## See Also

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
