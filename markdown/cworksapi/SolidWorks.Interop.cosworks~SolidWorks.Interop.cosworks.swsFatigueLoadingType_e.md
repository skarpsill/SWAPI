---
title: "swsFatigueLoadingType_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsFatigueLoadingType_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFatigueLoadingType_e.html"
---

# swsFatigueLoadingType_e Enumeration

Types of fatigue loading

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsFatigueLoadingType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsFatigueLoadingType_e
```

### C#

```csharp
public enum swsFatigueLoadingType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsFatigueLoadingType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsFatigueLoadingType_FullyReversed | 0 = The fatigue event is based on one reference study; all loads and stress components in the reference study reverse their directions simultaneously for the specified number of cycles in the event |
| swsFatigueLoadingType_LoadingRatio | 2 = The fatigue event is based on one reference study; each load and each stress component in the reference study changes its magnitude proportionally from its maximum value (S max ) to a minimum value defined by R*S max , where R is the loading ratio; a negative ratio indicates a reversal of the load direction |
| swsFatigueLoadingType_NonProportional | 3 = The fatigue event is based on one reference study; each load and each stress component in the reference study changes its magnitude non-proportionally from its maximum value (S max ) to a minimum value defined by R*S max , where R is the loading ratio; a negative ratio indicates a reversal of the load direction |
| swsFatigueLoadingType_ZeroBased | 1 = The fatigue event is based on one reference study; all loads and stress components in the reference study change their magnitudes proportionally from their maximum values as specified by the reference study to zero |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
