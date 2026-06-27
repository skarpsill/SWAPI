---
title: "swKeepReplacedCompOption_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swKeepReplacedCompOption_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swKeepReplacedCompOption_e.html"
---

# swKeepReplacedCompOption_e Enumeration

Options for replacing components in BOM features.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swKeepReplacedCompOption_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swKeepReplacedCompOption_e
```

### C#

```csharp
public enum swKeepReplacedCompOption_e : System.Enum
```

### C++/CLI

```cpp
public enum class swKeepReplacedCompOption_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swKeepBothNewItemNumber | 0 = Keep both with new item number |
| swKeepBothSameItemNumber | 1 = Keep both with same item number |
| swKeepItemNumber | 2 = Keep item number and do not keep replaced component |
| swKeepNewItemNumberRemoveReplacedComp | 3 = Assign new item number and do not keep replaced component |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
