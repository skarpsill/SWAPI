---
title: "swCheckOutOfDate_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCheckOutOfDate_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCheckOutOfDate_e.html"
---

# swCheckOutOfDate_e Enumeration

Check for out-of-date lightweight components options.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCheckOutOfDate_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCheckOutOfDate_e
```

### C#

```csharp
public enum swCheckOutOfDate_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCheckOutOfDate_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCheckOutOfDate_AlwaysResolve | Resolve out-of-date components; other lightweight components are not resolved |
| swCheckOutOfDate_DoNotCheck | Do not check |
| swCheckOutOfDate_Indicate | Mark out-of-date components with a broken feather; good lightweight models are not marked with the broken feather; instead, they are marked with the regular feather |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
