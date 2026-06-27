---
title: "swDmUnitsDecimalRounding_e Enumeration"
project: "SOLIDWORKS Document Manager API Help"
interface: "swDmUnitsDecimalRounding_e"
member: ""
kind: "enum"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmUnitsDecimalRounding_e.html"
---

# swDmUnitsDecimalRounding_e Enumeration

Rounding options for decimal units.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swDmUnitsDecimalRounding_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swDmUnitsDecimalRounding_e
```

### C#

```csharp
public enum swDmUnitsDecimalRounding_e : System.Enum
```

### C++/CLI

```cpp
public enum class swDmUnitsDecimalRounding_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDmUnitsDecimalRounding_HalfAway | 0 = Round up to the nearest decimal |
| swDmUnitsDecimalRounding_HalfToEven | 2 = Round up or down to the next even decimal |
| swDmUnitsDecimalRounding_HalfTowards | 1 = Round down to the nearest decimal |
| swDmUnitsDecimalRounding_Truncate | 3 = Truncate the decimal without rounding |

## See Also

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
