---
title: "swPropertyManagerColorScheme_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swPropertyManagerColorScheme_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropertyManagerColorScheme_e.html"
---

# swPropertyManagerColorScheme_e Enumeration

Color schemes for PropertyManager pages.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swPropertyManagerColorScheme_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swPropertyManagerColorScheme_e
```

### C#

```csharp
public enum swPropertyManagerColorScheme_e : System.Enum
```

### C++/CLI

```cpp
public enum class swPropertyManagerColorScheme_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swPropertyManagerColorScheme_Blue | 1 |
| swPropertyManagerColorScheme_Default | 7 |
| swPropertyManagerColorScheme_Gray | 2 |
| swPropertyManagerColorScheme_Mustard | 3 |
| swPropertyManagerColorScheme_Olive | 4 |
| swPropertyManagerColorScheme_Sand | 5 |
| swPropertyManagerColorScheme_SeaGreen | 6 |
| swPropertyManagerColorScheme_Windows | 8 |

## Remarks

These enumerators describe themes for the various colors used in the PropertyManager pages, not a specific color. When a scheme is changed, any open PropertyManager pages are immediately updated to the new color scheme.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
