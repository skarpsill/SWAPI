---
title: "swsDropType_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsDropType_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDropType_e.html"
---

# swsDropType_e Enumeration

Setup input types for drop test studies

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsDropType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsDropType_e
```

### C#

```csharp
public enum swsDropType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsDropType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsDropType_DropHeight | 0 = Specify the height from which the model is dropped from rest |
| swsDropType_VelocityAtImpact | 1 = Specify the direction and magnitude of the model's velocity at the moment of impact with the target plane |

## Remarks

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
