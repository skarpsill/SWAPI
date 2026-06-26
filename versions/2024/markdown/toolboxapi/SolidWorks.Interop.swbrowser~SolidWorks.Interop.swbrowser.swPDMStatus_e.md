---
title: "swPDMStatus_e Enumeration"
project: "SOLIDWORKS Toolbox Browser API"
interface: "swPDMStatus_e"
member: ""
kind: "enum"
source: "toolboxapi/SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.swPDMStatus_e.html"
---

# swPDMStatus_e Enumeration

PDM document statuses.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swPDMStatus_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swPDMStatus_e
```

### C#

```csharp
public enum swPDMStatus_e : System.Enum
```

### C++/CLI

```cpp
public enum class swPDMStatus_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swPDMStatusError | 0 |
| swPDMStatusKnownAndAvailable | 2 = Document is known to PDM and writable |
| swPDMStatusKnownAndUnavailable | 3 = Document is known to PDM and not writable |
| swPDMStatusUnknown | 1 = Document is unknown to PDM |

## See Also

[SolidWorks.Interop.swbrowser Namespace](SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser_namespace.html)
