---
title: "swComponentResolveStatus_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swComponentResolveStatus_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swComponentResolveStatus_e.html"
---

# swComponentResolveStatus_e Enumeration

States for resolving components.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swComponentResolveStatus_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swComponentResolveStatus_e
```

### C#

```csharp
public enum swComponentResolveStatus_e : System.Enum
```

### C++/CLI

```cpp
public enum class swComponentResolveStatus_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swResolveAbortedByUser | 1 = User aborted resolving the components |
| swResolveError | 3 = Not used |
| swResolveNotPerformed | 2 = Some of the components did not get resolved despite the user requesting it |
| swResolveOk | 0 = Components resolved okay |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
