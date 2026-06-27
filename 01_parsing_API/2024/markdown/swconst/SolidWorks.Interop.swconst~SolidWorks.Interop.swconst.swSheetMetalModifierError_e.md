---
title: "swSheetMetalModifierError_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swSheetMetalModifierError_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSheetMetalModifierError_e.html"
---

# swSheetMetalModifierError_e Enumeration

Sheet metal feature data errors.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swSheetMetalModifierError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swSheetMetalModifierError_e
```

### C#

```csharp
public enum swSheetMetalModifierError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swSheetMetalModifierError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swSheetMetalModifierError_GaugeTablePathNotEmpty | 5 = ISheetMetalFeatureData::SetUseGaugeTable's GaugeTableFile parameter must be an empty string for derived sheet-metal features |
| swSheetMetalModifierError_InvalidProperty | 3 |
| swSheetMetalModifierError_NoError | 0 |
| swSheetMetalModifierError_NotEnabledOnTemplate | 2 |
| swSheetMetalModifierError_OldArchitecture | 1 |
| swSheetMetalModifierError_UnspecifiedError | 4 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
