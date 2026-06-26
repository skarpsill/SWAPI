---
title: "swsDistributedMassError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsDistributedMassError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDistributedMassError_e.html"
---

# swsDistributedMassError_e Enumeration

Errors for distributed mass loads

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsDistributedMassError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsDistributedMassError_e
```

### C#

```csharp
public enum swsDistributedMassError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsDistributedMassError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsDistributedMassError_ImproperEntities | 2 = Selected entities are not proper |
| swsDistributedMassError_InvalidMass | 5 = Specified mass is invalid |
| swsDistributedMassError_InvalidUnits | 4 = Selected units are invalid |
| swsDistributedMassError_NoError | 0 = Successful |
| swsDistributedMassError_NotAvailable | 1 = Not available for this study |
| swsDistributedMassError_SelectOnlyFaces | 3 = Select only faces |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
