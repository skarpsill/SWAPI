---
title: "swSaveAsVersion_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swSaveAsVersion_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSaveAsVersion_e.html"
---

# swSaveAsVersion_e Enumeration

Version of a particular format to save the document.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swSaveAsVersion_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swSaveAsVersion_e
```

### C#

```csharp
public enum swSaveAsVersion_e : System.Enum
```

### C++/CLI

```cpp
public enum class swSaveAsVersion_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swSaveAsCurrentVersion | 0 = This is the typical save behavior. |
| swSaveAsDetachedDrawing | 4 |
| swSaveAsFormatProE | 2 |
| swSaveAsStandardDrawing | 3 |
| swSaveAsSW98plus | Obsolete and no longer supported. |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
