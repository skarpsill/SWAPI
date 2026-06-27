---
title: "swMirrorComponentMirrorType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swMirrorComponentMirrorType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMirrorComponentMirrorType_e.html"
---

# swMirrorComponentMirrorType_e Enumeration

Mirror positions for mirroring components.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swMirrorComponentMirrorType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swMirrorComponentMirrorType_e
```

### C#

```csharp
public enum swMirrorComponentMirrorType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swMirrorComponentMirrorType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swMirrorType_CenterOfBoundingBox | 0 = Positions the mirror so that the center of a bounding box for the selected components is mirrored about the mirror plane |
| swMirrorType_CenterOfMass | 1 = Positions the mirror so that the center of mass of the selected components is mirrored about the mirror plane |
| swMirrorType_ComponentOrigin | 2 = Positions the mirror so that the component origins are mirrored about the mirror plane |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
