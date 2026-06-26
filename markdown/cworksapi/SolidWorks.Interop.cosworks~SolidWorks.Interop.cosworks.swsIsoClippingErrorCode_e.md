---
title: "swsIsoClippingErrorCode_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsIsoClippingErrorCode_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsIsoClippingErrorCode_e.html"
---

# swsIsoClippingErrorCode_e Enumeration

Iso Clipping error codes

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsIsoClippingErrorCode_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsIsoClippingErrorCode_e
```

### C#

```csharp
public enum swsIsoClippingErrorCode_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsIsoClippingErrorCode_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsIsoClippingCosworksViewNotPresent | 1 = Cosmos view not present |
| swsIsoClippingIsoInvalidVariantError | 7 = Invalid variant |
| swsIsoClippingIsoPlanesError | 2 = The number of iso planes is incorrect |
| swsIsoClippingIsoValueError | 5 = Iso value is incorrect |
| swsIsoClippingIsoVariantValueError | 6 = Variant containing iso values is empty |
| swsIsoClippingNoError | 0 = No error |
| swsIsoClippingNotAvailable | 8 = Iso clipping is not available for this plot |
| swsIsoClippingPlotNotFound | 3 = The plot name does not exist |
| swsIsoClippingPostDataNotExist | 4 = Database not present |

## Remarks

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
