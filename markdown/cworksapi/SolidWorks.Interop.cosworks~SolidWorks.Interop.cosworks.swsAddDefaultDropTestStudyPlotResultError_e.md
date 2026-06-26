---
title: "swsAddDefaultDropTestStudyPlotResultError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsAddDefaultDropTestStudyPlotResultError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsAddDefaultDropTestStudyPlotResultError_e.html"
---

# swsAddDefaultDropTestStudyPlotResultError_e Enumeration

Drop test study result plot errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsAddDefaultDropTestStudyPlotResultError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsAddDefaultDropTestStudyPlotResultError_e
```

### C#

```csharp
public enum swsAddDefaultDropTestStudyPlotResultError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsAddDefaultDropTestStudyPlotResultError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsDropTestResultDisplacementRangeError | 4 = Displacement component value is outside the range of supported values |
| swsDropTestResultElementalStrainRangeError | 5 = Elemental strain component value is outside the range of supported values |
| swsDropTestResultElementalStressRangeError | 3 = Elemental stress component value is outside the range of supported values |
| swsDropTestResultNodalStressRangeError | 2 = Nodal stress component value is outside the range of supported values |
| swsDropTestResultNoError | 0 |
| swsDropTestResultRangeError | 1 = Result is outside the range of supported values |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
