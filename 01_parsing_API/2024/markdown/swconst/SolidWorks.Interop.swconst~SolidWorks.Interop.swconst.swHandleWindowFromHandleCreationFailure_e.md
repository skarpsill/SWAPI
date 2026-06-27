---
title: "swHandleWindowFromHandleCreationFailure_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swHandleWindowFromHandleCreationFailure_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swHandleWindowFromHandleCreationFailure_e.html"
---

# swHandleWindowFromHandleCreationFailure_e Enumeration

Actions on failure to create a .NET control on a PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swHandleWindowFromHandleCreationFailure_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swHandleWindowFromHandleCreationFailure_e
```

### C#

```csharp
public enum swHandleWindowFromHandleCreationFailure_e : System.Enum
```

### C++/CLI

```cpp
public enum class swHandleWindowFromHandleCreationFailure_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swHandleWindowFromHandleCreationFailure_Cancel | 1 = Create the PropertyManager page without the .NET control. (default) |
| swHandleWindowFromHandleCreationFailure_Continue | 3 = Cancel the creation of the PropertyManager page. |
| swHandleWindowFromHandleCreationFailure_Retry | 2 = Try to create the .NET control again. |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
