---
title: "swReorderComponentsWhere_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swReorderComponentsWhere_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swReorderComponentsWhere_e.html"
---

# swReorderComponentsWhere_e Enumeration

Where to move the components.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swReorderComponentsWhere_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swReorderComponentsWhere_e
```

### C#

```csharp
public enum swReorderComponentsWhere_e : System.Enum
```

### C++/CLI

```cpp
public enum class swReorderComponentsWhere_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swReorderComponents_After | 1 = Move the source components to just after the target |
| swReorderComponents_Before | 2 = Move the source components to just before the target |
| swReorderComponents_FirstInFolder | 4 = Move the source components into the target folder, as the first items in the folder |
| swReorderComponents_LastInFolder | 3 = Move the source components into the target folder, as the last items in the folder |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
