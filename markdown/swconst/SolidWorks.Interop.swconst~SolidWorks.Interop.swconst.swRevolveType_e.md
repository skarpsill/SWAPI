---
title: "swRevolveType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swRevolveType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRevolveType_e.html"
---

# swRevolveType_e Enumeration

Revolve feature types.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swRevolveType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swRevolveType_e
```

### C#

```csharp
public enum swRevolveType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swRevolveType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swRevolveTypeMidPlane | 1 = Mid-plane revolution |
| swRevolveTypeMidPlane360Degrees | 4 = Create revolve: mid-plane revolution with a 360-degree angle - or - Edit revolve: mid-plane revolution with a 360-degree angle; if you use IRevolveFeatureData2::SetRevolutionAngle , then the 360-degree angle is overwritten |
| swRevolveTypeOneDirection | 0 = One-direction revolution |
| swRevolveTypeOneDirection360Degrees | 3 = Create revolve: one direction revolution with a 360-degree angle - or - Edit revolve: one direction revolution with a 360-degree angle; if you use IRevolveFeatureData2::SetRevolutionAngle , then the 360-degree angle is overwritten |
| swRevolveTypeTwoDirection | 2 = Two direction revolution |
| swRevolveTypeTwoDirection360Degrees | 5 = Create and edit revolves: two direction revolution |

## Remarks

| To... | Use... |
| --- | --- |
| Create revolve | IFeatureManager::FeatureRevolve IFeatureManager::FeatureRevolveCut IFeatureManager::FeatureRevolveThin IFeatureManager::FeatureRevolveThinCut |
| Edit revolve | IRevolveFeatureData2::Type |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
