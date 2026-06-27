---
title: "swComponentSuppressionState_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swComponentSuppressionState_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swComponentSuppressionState_e.html"
---

# swComponentSuppressionState_e Enumeration

States for component suppression.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swComponentSuppressionState_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swComponentSuppressionState_e
```

### C#

```csharp
public enum swComponentSuppressionState_e : System.Enum
```

### C++/CLI

```cpp
public enum class swComponentSuppressionState_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swComponentFullyLightweight | 4 = Fully lightweight - recursively makes the component and any child components lightweight |
| swComponentFullyResolved | 2 = Fully resolved - recursively resolves the component and any child components |
| swComponentInternalIdMismatch | 5 |
| swComponentLightweight | 1 = Lightweight - makes only the component lightweight |
| swComponentResolved | 3 = Resolved - resolves only the component |
| swComponentSuppressed | 0 = Fully suppressed - recursively suppresses the component and any child components |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
