---
title: "swsDynamicExtraFrequenciesError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsDynamicExtraFrequenciesError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDynamicExtraFrequenciesError_e.html"
---

# swsDynamicExtraFrequenciesError_e Enumeration

Result codes for harmonic and random vibration study extra frequencies.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsDynamicExtraFrequenciesError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsDynamicExtraFrequenciesError_e
```

### C#

```csharp
public enum swsDynamicExtraFrequenciesError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsDynamicExtraFrequenciesError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsDynamicExtraFrequenciesError_DynamicParamEmpty | 3 |
| swsDynamicExtraFrequenciesError_InvalidInput | 5 = Expected 1 to 20 extra frequencies in ascending order |
| swsDynamicExtraFrequenciesError_NoError | 0 |
| swsDynamicExtraFrequenciesError_NotAvailable | 1 |
| swsDynamicExtraFrequenciesError_NotAvailableForSubType | 2 |
| swsDynamicExtraFrequenciesError_OutOfRange | 4 |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
