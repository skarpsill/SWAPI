---
title: "swsFatigueMeanStressCorrectionType_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsFatigueMeanStressCorrectionType_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFatigueMeanStressCorrectionType_e.html"
---

# swsFatigueMeanStressCorrectionType_e Enumeration

Mean stress correction options for calculating alternating stresses

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsFatigueMeanStressCorrectionType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsFatigueMeanStressCorrectionType_e
```

### C#

```csharp
public enum swsFatigueMeanStressCorrectionType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsFatigueMeanStressCorrectionType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsFatigueMeanStressCorrectionType_Gerber | 2 = Use the Gerber mean stress correction equation; suitable for ductile materials |
| swsFatigueMeanStressCorrectionType_Goodman | 1 = Use the Goodman mean stress correction equation; suitable for brittle materials |
| swsFatigueMeanStressCorrectionType_None | 0 = Do not use a mean stress correction |
| swsFatigueMeanStressCorrectionType_Soderberg | 3 = Use the Soderberg mean stress correction equation; this is the most conservative method |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
