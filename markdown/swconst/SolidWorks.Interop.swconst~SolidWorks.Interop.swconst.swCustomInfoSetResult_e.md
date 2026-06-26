---
title: "swCustomInfoSetResult_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCustomInfoSetResult_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCustomInfoSetResult_e.html"
---

# swCustomInfoSetResult_e Enumeration

Result codes when setting custom properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCustomInfoSetResult_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCustomInfoSetResult_e
```

### C#

```csharp
public enum swCustomInfoSetResult_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCustomInfoSetResult_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCustomInfoSetResult_LinkedProp | 3 |
| swCustomInfoSetResult_NotPresent | 1 = Custom property does not exist |
| swCustomInfoSetResult_OK | 0 = Success |
| swCustomInfoSetResult_TypeMismatch | 2 = Specified value has an incorrect type |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
