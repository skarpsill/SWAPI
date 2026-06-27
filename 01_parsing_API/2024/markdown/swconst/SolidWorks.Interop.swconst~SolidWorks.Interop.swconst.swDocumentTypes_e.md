---
title: "swDocumentTypes_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swDocumentTypes_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDocumentTypes_e.html"
---

# swDocumentTypes_e Enumeration

Document types.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swDocumentTypes_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swDocumentTypes_e
```

### C#

```csharp
public enum swDocumentTypes_e : System.Enum
```

### C++/CLI

```cpp
public enum class swDocumentTypes_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDocASSEMBLY | 2 |
| swDocDRAWING | 3 |
| swDocIMPORTED_ASSEMBLY | 7; Multi-CAD |
| swDocIMPORTED_PART | 6; Multi-CAD |
| swDocLAYOUT | 5 |
| swDocNONE | 0 |
| swDocPART | 1 |
| swDocSDM | 4 |

## Remarks

When opening library feature parts, use swDocPART.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
