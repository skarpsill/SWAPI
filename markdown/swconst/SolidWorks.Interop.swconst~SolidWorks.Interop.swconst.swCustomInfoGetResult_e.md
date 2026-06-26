---
title: "swCustomInfoGetResult_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCustomInfoGetResult_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCustomInfoGetResult_e.html"
---

# swCustomInfoGetResult_e Enumeration

Result codes when getting custom properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCustomInfoGetResult_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCustomInfoGetResult_e
```

### C#

```csharp
public enum swCustomInfoGetResult_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCustomInfoGetResult_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCustomInfoGetResult_CachedValue | 0 = Cached value was returned |
| swCustomInfoGetResult_NotPresent | 1 = Custom property does not exist |
| swCustomInfoGetResult_ResolvedValue | 2 = Resolved value was returned |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
