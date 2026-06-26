---
title: "swCreateFacesBodyAction_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCreateFacesBodyAction_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCreateFacesBodyAction_e.html"
---

# swCreateFacesBodyAction_e Enumeration

Options for creating missing faces on an open body.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCreateFacesBodyAction_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCreateFacesBodyAction_e
```

### C#

```csharp
public enum swCreateFacesBodyAction_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCreateFacesBodyAction_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCreateFacesBodyActionCap | 1 = Cap the missing face |
| swCreateFacesBodyActionGrow | 2 = Grow the missing face |
| swCreateFacesBodyActionGrowFromParent | 3 = Grow the missing face from the parent |
| swCreateFacesBodyActionLeaveRubber | 4 = Create a virtual face topological entity without any associated geometry |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
