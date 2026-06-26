---
title: "swSetValueInConfiguration_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swSetValueInConfiguration_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSetValueInConfiguration_e.html"
---

# swSetValueInConfiguration_e Enumeration

Values for indicating in which configurations the value should be set.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swSetValueInConfiguration_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swSetValueInConfiguration_e
```

### C#

```csharp
public enum swSetValueInConfiguration_e : System.Enum
```

### C++/CLI

```cpp
public enum class swSetValueInConfiguration_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swSetValue_InAllConfigurations | 2 = Set the value in all configurations |
| swSetValue_InSpecificConfigurations | 3 = Set the value in the specific configuration |
| swSetValue_InThisConfiguration | 1 = Set the value in the current configuration only |
| swSetValue_NoConfiguration | -1 = Ignore configurations in drawing sketches |
| swSetValue_UseCurrentSetting | 0 = Use whatever setting this parameter currently has |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
