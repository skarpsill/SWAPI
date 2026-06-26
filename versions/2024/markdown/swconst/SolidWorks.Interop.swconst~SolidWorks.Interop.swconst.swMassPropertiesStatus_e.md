---
title: "swMassPropertiesStatus_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swMassPropertiesStatus_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMassPropertiesStatus_e.html"
---

# swMassPropertiesStatus_e Enumeration

Mass property result codes.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swMassPropertiesStatus_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swMassPropertiesStatus_e
```

### C#

```csharp
public enum swMassPropertiesStatus_e : System.Enum
```

### C++/CLI

```cpp
public enum class swMassPropertiesStatus_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swMassPropertiesStatus_NoBody | 2 = Mass properties calculation failed because there is no body in the model |
| swMassPropertiesStatus_OK | 0 = Mass properties calculation successful |
| swMassPropertiesStatus_UnknownError | 1 = Mass properties calculation failed for an unknown reason |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
