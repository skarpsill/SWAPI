---
title: "swPipingPenetrationStatus_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swPipingPenetrationStatus_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPipingPenetrationStatus_e.html"
---

# swPipingPenetrationStatus_e Enumeration

Piping pentration status.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swPipingPenetrationStatus_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swPipingPenetrationStatus_e
```

### C#

```csharp
public enum swPipingPenetrationStatus_e : System.Enum
```

### C++/CLI

```cpp
public enum class swPipingPenetrationStatus_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swPenetrationFailed | 1 = Unspecified error |
| swPenetrationFailedAlreadyPenetrating | 8 = Pipe is already penetrating |
| swPenetrationFailedBadFitting | 7 = Pipe cannot be found or fitting to pierce cannot be found |
| swPenetrationFailedBadSelection | 6 = Sketch point cannot be used for penetration |
| swPenetrationFailedDllNotLoaded | 3 = Routing not installed |
| swPenetrationFailedMultiBody | 9 = Pipe cannot pentrate multibody |
| swPenetrationFailedNoSelection | 4 = No sketch point selected |
| swPenetrationFailedNotRouting | 5 = Sketch is not a routing sketch |
| swPenetrationFailedPipeTooWide | 2 = Pipe too wide to cut other pipe |
| swPenetrationSucceeded | 0 = Okay |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
