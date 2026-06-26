---
title: "swCustomPropertyAddOption_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCustomPropertyAddOption_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCustomPropertyAddOption_e.html"
---

# swCustomPropertyAddOption_e Enumeration

Options when adding custom properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCustomPropertyAddOption_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCustomPropertyAddOption_e
```

### C#

```csharp
public enum swCustomPropertyAddOption_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCustomPropertyAddOption_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCustomPropertyDeleteAndAdd | 1 = Delete an existing custom property having the same name and add the new custom property |
| swCustomPropertyOnlyIfNew | 0 = Add the custom property only if it is new |
| swCustomPropertyReplaceValue | 2 = Replace the value of an existing custom property having the same name |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
