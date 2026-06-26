---
title: "swsModeCombinationMethod_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsModeCombinationMethod_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsModeCombinationMethod_e.html"
---

# swsModeCombinationMethod_e Enumeration

Mode combination methods for calculating a peak response in dynamic studies

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsModeCombinationMethod_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsModeCombinationMethod_e
```

### C#

```csharp
public enum swsModeCombinationMethod_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsModeCombinationMethod_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsModeCombinationMethod_AbsSum | 1 = Absolute Sum; This method calculates the peak response as the sum of the maximum modal responses |
| swsModeCombinationMethod_CQC | 2 = Complete Quadratic Combination (CQC); This method calculates the peak response using cross-modal correlation coefficients, modal damping coefficients, and a double summation equation based on random vibration theories |
| swsModeCombinationMethod_NRL | 3 = Naval Research Laboratory (NRL); This method calculates the peak response as the sum of the absolute value of the response of the mode that exhibits the largest response and the SRSS response of the remaining modes |
| swsModeCombinationMethod_SRSS | 0 = Square Root of the Sum of Squares (SRSS); This method calculates the peak response as the square root of the sum of the maximum modal responses squared |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
