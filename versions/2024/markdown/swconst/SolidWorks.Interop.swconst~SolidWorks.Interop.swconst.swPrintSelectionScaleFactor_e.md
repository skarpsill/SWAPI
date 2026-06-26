---
title: "swPrintSelectionScaleFactor_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swPrintSelectionScaleFactor_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPrintSelectionScaleFactor_e.html"
---

# swPrintSelectionScaleFactor_e Enumeration

Drawing print selection scale options.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swPrintSelectionScaleFactor_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swPrintSelectionScaleFactor_e
```

### C#

```csharp
public enum swPrintSelectionScaleFactor_e : System.Enum
```

### C++/CLI

```cpp
public enum class swPrintSelectionScaleFactor_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swPrintAll | 0 |
| swPrintCurrentSheet | 1; Print the current drawing sheet with a 1:1 scale |
| swPrintScreenImage | 2 |
| swPrintSelection | 3; Specify custom scale factors for the current drawing sheet |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
