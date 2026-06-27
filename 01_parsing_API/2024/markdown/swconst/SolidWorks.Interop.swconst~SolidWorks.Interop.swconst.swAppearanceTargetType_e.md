---
title: "swAppearanceTargetType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swAppearanceTargetType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAppearanceTargetType_e.html"
---

# swAppearanceTargetType_e Enumeration

Types of targets to which to apply a copied appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swAppearanceTargetType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swAppearanceTargetType_e
```

### C#

```csharp
public enum swAppearanceTargetType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swAppearanceTargetType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAppearanceTargetAppearanceFilter | 5 = All appearances in the model that match the appearance of the selected face are applied the copied appearance |
| swAppearanceTargetBody | 2 = The body of the selected face is applied the copied appearance |
| swAppearanceTargetComponent | 4 = The component of the selected face is applied the copied appearance |
| swAppearanceTargetFace | 0 = The selected face is applied the copied appearance |
| swAppearanceTargetFeature | 1 = The feature of the selected face is applied the copied appearance |
| swAppearanceTargetPart | 3 = The part of the selected face is applied the copied appearance |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
