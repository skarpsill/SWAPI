---
title: "swsDropHeightType_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsDropHeightType_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDropHeightType_e.html"
---

# swsDropHeightType_e Enumeration

Distances between a dropped body and the rigid planar floor

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsDropHeightType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsDropHeightType_e
```

### C#

```csharp
public enum swsDropHeightType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsDropHeightType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsDropHeightType_FromCentroid | 0 = Distance between the geometric center of the body and the rigid planar floor |
| swsDropHeightType_FromLowestPoint | 1 = Distance between the lowest point of the body and the rigid planar floor |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
