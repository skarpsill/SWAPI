---
title: "swsDropTestSetUpError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsDropTestSetUpError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDropTestSetUpError_e.html"
---

# swsDropTestSetUpError_e Enumeration

Setup errors for drop test studies

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsDropTestSetUpError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsDropTestSetUpError_e
```

### C#

```csharp
public enum swsDropTestSetUpError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsDropTestSetUpError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsDropTestSetUpError_AvailableOnlyForDropTestStudy | 1 = Not available for this study type |
| swsDropTestSetUpError_GravityEntityIsNULL | 3 = Gravity entity is NULL |
| swsDropTestSetUpError_GravityEntityShouldBeEdgeFaceOrPlane | 4 = Gravity entity should be an edge, face, or plane |
| swsDropTestSetUpError_NoError | 0 = No error |
| swsDropTestSetUpError_SetUpAlreadyAdded | 2 = Setup already exists |
| swsDropTestSetUpError_SetupNotExists | 6 = Setup does not exist |
| swsDropTestSetUpError_ShouldBeStraightEdgeOrPlaneFace | 5 = Gravity entity should be straight edge or planar face |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
