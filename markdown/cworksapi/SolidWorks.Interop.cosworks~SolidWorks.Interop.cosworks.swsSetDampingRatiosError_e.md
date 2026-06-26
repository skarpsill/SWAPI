---
title: "swsSetDampingRatiosError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsSetDampingRatiosError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsSetDampingRatiosError_e.html"
---

# swsSetDampingRatiosError_e Enumeration

Errors when setting damping ratios

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsSetDampingRatiosError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsSetDampingRatiosError_e
```

### C#

```csharp
public enum swsSetDampingRatiosError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsSetDampingRatiosError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsSetDampingRatiosError_InCorrectValues | 4 = The ratio values are incorrect |
| swsSetDampingRatiosError_InvalidArray | 3 = Number of elements in the array is invalid |
| swsSetDampingRatiosError_InvalidRows | 2 = Number of rows should be greater than 0 |
| swsSetDampingRatiosError_NoError | 0 = Successful |
| swsSetDampingRatiosError_NotAvailable | 1 = Damping ratios are not available for this study |
| swsSetDampingRatiosError_OptionsNotAvailable | 5 = Damping options are not available |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
