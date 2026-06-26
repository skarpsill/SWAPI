---
title: "swNormalCutParameters_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swNormalCutParameters_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swNormalCutParameters_e.html"
---

# swNormalCutParameters_e Enumeration

Sheet metal normal cut parameters.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swNormalCutParameters_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swNormalCutParameters_e
```

### C#

```csharp
public enum swNormalCutParameters_e : System.Enum
```

### C++/CLI

```cpp
public enum class swNormalCutParameters_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swNormalCutExtent | 0 = Cuts the maximum amount from the intersection profiles on the top and bottom of the sheet metal body |
| swNormalCutOffsetPlane | 1 = Adjusts the layer where the intersection curve intersects the sheet metal body; Select a reference plane or top or bottom face to define the offset plane and then either set ISMNormalCutFeatureData2::LinkToKFactor to true or set ISMNormalCutFeatureData2::LayerAdjustmentValue to a value between 0 and 1 to adjust the layer |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
