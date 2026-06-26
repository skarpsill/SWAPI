---
title: "fwPerformanceOptions_e Enumeration"
project: "FeatureWorks API Help"
interface: "fwPerformanceOptions_e"
member: ""
kind: "enum"
source: "fworksapi/SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.fwPerformanceOptions_e.html"
---

# fwPerformanceOptions_e Enumeration

Performance options.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum fwPerformanceOptions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As fwPerformanceOptions_e
```

### C#

```csharp
public enum fwPerformanceOptions_e : System.Enum
```

### C++/CLI

```cpp
public enum class fwPerformanceOptions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| fwDoNotPerformBodyCheck | 0x0001 = When you do not specify this option, the software periodically checks the body during feature recognition; if this option is specified, then the software does not check the body for any errors (resulting in faster performance) |
| fwDoNotPerformIntrusionCheck | 0x0002 = When you specify this option, the software does not check for features that intrude upon one another during automatic feature recognition |

## See Also

[SolidWorks.Interop.fworks Namespace](SolidWorks.Interop.fworks~SolidWorks.Interop.fworks_namespace.html)
