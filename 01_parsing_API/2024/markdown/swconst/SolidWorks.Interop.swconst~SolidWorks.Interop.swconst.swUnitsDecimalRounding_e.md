---
title: "swUnitsDecimalRounding_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swUnitsDecimalRounding_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUnitsDecimalRounding_e.html"
---

# swUnitsDecimalRounding_e Enumeration

Rounding options for decimal units.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swUnitsDecimalRounding_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swUnitsDecimalRounding_e
```

### C#

```csharp
public enum swUnitsDecimalRounding_e : System.Enum
```

### C++/CLI

```cpp
public enum class swUnitsDecimalRounding_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swUnitsDecimalRounding_HalfAway | 0 = Round up to the nearest decimal |
| swUnitsDecimalRounding_HalfToEven | 2 = Round up or down to the next even decimal |
| swUnitsDecimalRounding_HalfTowards | 1 = Round down to the nearest decimal |
| swUnitsDecimalRounding_Truncate | 3 = Truncate the decimal without rounding |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
