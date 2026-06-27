---
title: "swCustomInfoAddResult_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCustomInfoAddResult_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCustomInfoAddResult_e.html"
---

# swCustomInfoAddResult_e Enumeration

Result codes when adding custom properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCustomInfoAddResult_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCustomInfoAddResult_e
```

### C#

```csharp
public enum swCustomInfoAddResult_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCustomInfoAddResult_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCustomInfoAddResult_AddedOrChanged | 0 = Success |
| swCustomInfoAddResult_GenericFail | 1 = Failed to add the custom property |
| swCustomInfoAddResult_MismatchAgainstExistingType | 2 = Existing custom property with the same name has a different type |
| swCustomInfoAddResult_MismatchAgainstLegacyTypes | 4 = Cannot add the specified custom property to legacy architecture |
| swCustomInfoAddResult_MismatchAgainstSpecifiedType | 3 = Specified value of the custom property does not match the specified type |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
