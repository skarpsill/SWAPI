---
title: "swPMContainer_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swPMContainer_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMContainer_e.html"
---

# swPMContainer_e Enumeration

Docking states of PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swPMContainer_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swPMContainer_e
```

### C#

```csharp
public enum swPMContainer_e : System.Enum
```

### C++/CLI

```cpp
public enum class swPMContainer_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swPMFloating | 3 = True floating state where PropertyManager page lives inside new docking pane; a single floating window owns all PropertyManager pages of all open documents |
| swPMInTabsWithFM | 0 = Old-style PropertyManager page embedded in tabs at top |
| swPMPinnedAboveFM | 1 = Quasi floating state where PropertyManager page automatically displays, resizes itself in the lower-left corner of model frame window, and covers the FeatureManager design tree; one window for each open document |
| swPMPinnedLowerRight | 4 = Quasi floating state where PropertyManager page automatically displays, resizes itself in the lower-right corner of the model frame window, covers the graphic area, and has full height; one window for each open document |
| swPMPinnedNextToFM | 2 = Quasi floating state where PropertyManager page automatically displays, resizes itself to the right of the FeatureManager design tree, covers the graphics area, and has full height.; one window for each open document |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
