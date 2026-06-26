---
title: "swConstrainedCornerAction_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swConstrainedCornerAction_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConstrainedCornerAction_e.html"
---

# swConstrainedCornerAction_e Enumeration

Actions to take if the corner to be filleted is constrained or has a dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swConstrainedCornerAction_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swConstrainedCornerAction_e
```

### C#

```csharp
public enum swConstrainedCornerAction_e : System.Enum
```

### C++/CLI

```cpp
public enum class swConstrainedCornerAction_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swConstrainedCornerDeleteGeometry | 2 = Delete the constraint or dimension and add the fillet |
| swConstrainedCornerInteract | 0 = Ask the user whether to delete the geometry or stop processing |
| swConstrainedCornerKeepGeometry | 1 = Keep the constraint or dimension by creating a virtual intersection point before adding the fillet |
| swConstrainedCornerStopProcessing | 3 = Do not delete the constraint or dimension and do not create the fillet |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
