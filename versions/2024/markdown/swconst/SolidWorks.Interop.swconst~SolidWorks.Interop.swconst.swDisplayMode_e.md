---
title: "swDisplayMode_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swDisplayMode_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDisplayMode_e.html"
---

# swDisplayMode_e Enumeration

Display modes of drawing views.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swDisplayMode_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swDisplayMode_e
```

### C#

```csharp
public enum swDisplayMode_e : System.Enum
```

### C++/CLI

```cpp
public enum class swDisplayMode_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDisplayModeDEFAULT | 8 |
| swDisplayModeUNKNOWN | -1 |
| swFACETED_HIDDEN | 6 |
| swFACETED_HIDDEN_GREYED | 5 |
| swFACETED_WIREFRAME | 4 |
| swHIDDEN | 2; Hidden Lines Removed (HLR) |
| swHIDDEN_GREYED | 1; Hidden Lines Visible (HLV) |
| swSHADED | 3 |
| swSHADED_EDGES | 7 |
| swWIREFRAME | 0 |

## Remarks

A faceted display mode is draft quality.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
