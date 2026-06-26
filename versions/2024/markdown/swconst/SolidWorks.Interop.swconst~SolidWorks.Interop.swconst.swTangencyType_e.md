---
title: "swTangencyType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swTangencyType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTangencyType_e.html"
---

# swTangencyType_e Enumeration

Tangency options for lofts and profile twist options for sweeps.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swTangencyType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swTangencyType_e
```

### C#

```csharp
public enum swTangencyType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swTangencyType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swMinimumTwist | 10 = Prevents the profile from becoming self-intersecting as it follows the sweep or loft path; valid only for 3D paths; corresponds to Profile Twist > Minimum Twist in the Sweep PropertyManager |
| swTangencyAllFaces | 3 = Makes the adjacent faces tangent at the profile; valid only if swTwistControlType_e is set to swTwistControlFollowPath and only when attaching a sweep or loft to existing geometry; corresponds to Profile Twist > Tangent to Adjacent Faces in the Sweep PropertyManager |
| swTangencyDirectionVector | 2 = Sets a direction plane, planar face, line, edge, cylinder, axis, or a pair of vertices; valid only if swTwistControlType_e is set to swTwistControlFollowPath; corresponds to Profile Twist > Specify Direction Vector in the Sweep PropertyManager |
| swTangencyNone | 0 |
| swTangencyNormalToProfile | 1 = Aligns the profile normal to the sweep or loft path; valid only for 2D paths; corresponds to Profile Twist > None in the Sweep PropertyManager |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
