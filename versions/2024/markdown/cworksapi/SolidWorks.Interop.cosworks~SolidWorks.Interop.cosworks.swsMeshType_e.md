---
title: "swsMeshType_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsMeshType_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMeshType_e.html"
---

# swsMeshType_e Enumeration

Mesh types

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsMeshType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsMeshType_e
```

### C#

```csharp
public enum swsMeshType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsMeshType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsMeshTypeBeam | 4 = Beam mesh; supported for static, frequency, and buckling studies only |
| swsMeshTypeMidSurface | 1 = Shell using mid-surface; supported for part documents with simple geometry |
| swsMeshTypeMixed | 3 = Mixed mesh; mixed solids, shells, and beams are supported for static, frequency, and buckling studies; nonlinear, thermal, and linear dynamic studies support mixed meshes with solids and shells only (no beams) |
| swsMeshTypeSolid | 0 = Solid mesh |
| swsMeshTypeSurfaces | 2 = Shell mesh using surfaces; supported for parts and assemblies |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
