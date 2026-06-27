---
title: "swEdrawingSaveAsOption_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swEdrawingSaveAsOption_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEdrawingSaveAsOption_e.html"
---

# swEdrawingSaveAsOption_e Enumeration

eDrawings Save As options.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swEdrawingSaveAsOption_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swEdrawingSaveAsOption_e
```

### C#

```csharp
public enum swEdrawingSaveAsOption_e : System.Enum
```

### C++/CLI

```cpp
public enum class swEdrawingSaveAsOption_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swEdrawingSaveActive | 1 or 0x1; Publish the active configuration or sheet when saving as an eDrawings |
| swEdrawingSaveAll | 2 or 0x2; Publish all configurations or sheets when saving as an eDrawings |
| swEdrawingSaveSelected | 3 or 0x3; Publish sheets or configurations specified by swEmodelSelectionList when saving as an eDrawings |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
