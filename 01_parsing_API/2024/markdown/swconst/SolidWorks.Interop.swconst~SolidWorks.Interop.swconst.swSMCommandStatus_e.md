---
title: "swSMCommandStatus_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swSMCommandStatus_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSMCommandStatus_e.html"
---

# swSMCommandStatus_e Enumeration

Return conditions for various sheet metal APIs that attempt to do set operations.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swSMCommandStatus_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swSMCommandStatus_e
```

### C#

```csharp
public enum swSMCommandStatus_e : System.Enum
```

### C++/CLI

```cpp
public enum class swSMCommandStatus_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swSMErrorInvalidBendState | 4 = Failed, an invalid bend state was specified |
| swSMErrorNone | 0 = Successful, operation completed |
| swSMErrorNotAPart | 2 = Failed, sheet metal commands only apply to SOLIDWORKS parts |
| swSMErrorNotASheetMetalPart | 3 = Failed, the part contains no sheet metal features |
| swSMErrorUnknown | 1 = Failed, for an unknown reason |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
