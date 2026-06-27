---
title: "swsRestraintType_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsRestraintType_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRestraintType_e.html"
---

# swsRestraintType_e Enumeration

Restraint types

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsRestraintType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsRestraintType_e
```

### C#

```csharp
public enum swsRestraintType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsRestraintType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsRestraintTypeCyclicSymmetry | 9 = Cyclic symmetry |
| swsRestraintTypeCylindricalFaces | 7 = On cylindrical faces; specify translations for solids or translations and rotations for shells and beams |
| swsRestraintTypeFixed | 0 = Fixed (set translations and rotations to zero) |
| swsRestraintTypeFlatFace | 6 = On flat face; specify translations for solids or translations and rotations for shells and beams |
| swsRestraintTypeHinge | 4 = Hinge |
| swsRestraintTypeImmovable | 1 = Immovable (set translations to zero) |
| swsRestraintTypeReferenceGeometry | 5 = Use reference geometry |
| swsRestraintTypeRoller | 3 = Roller |
| swsRestraintTypeSphericalSurface | 8 = On spherical faces; specify translations for solids or translations and rotations for shells and beams |
| swsRestraintTypeSymmetric | 2 = Symmetric |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
