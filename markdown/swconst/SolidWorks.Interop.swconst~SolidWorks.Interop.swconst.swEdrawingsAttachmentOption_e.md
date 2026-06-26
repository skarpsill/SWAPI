---
title: "swEdrawingsAttachmentOption_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swEdrawingsAttachmentOption_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEdrawingsAttachmentOption_e.html"
---

# swEdrawingsAttachmentOption_e Enumeration

Configuration options for creating and attaching STEP files when publishing a part or assembly to eDrawings.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swEdrawingsAttachmentOption_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swEdrawingsAttachmentOption_e
```

### C#

```csharp
public enum swEdrawingsAttachmentOption_e : System.Enum
```

### C++/CLI

```cpp
public enum class swEdrawingsAttachmentOption_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swEdrawingsAttachActive | 1 = Create and attach STEP files to the active configuration only |
| swEdrawingsAttachAll | 2 = Create and attach STEP files to all configurations |
| swEdrawingsAttachNone | 0 = Do not create and attach any STEP files |
| swEdrawingsAttachSelected | 3 = Create and attach STEP files to specified configurations only |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
