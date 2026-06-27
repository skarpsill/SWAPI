---
title: "swSetValueReturnStatus_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swSetValueReturnStatus_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSetValueReturnStatus_e.html"
---

# swSetValueReturnStatus_e Enumeration

Return values for attempting to set the value of a parameter.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swSetValueReturnStatus_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swSetValueReturnStatus_e
```

### C#

```csharp
public enum swSetValueReturnStatus_e : System.Enum
```

### C++/CLI

```cpp
public enum class swSetValueReturnStatus_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swSetValue_DrivenDimension | 3 = Cannot be done on a dimension driven by geometry |
| swSetValue_Failure | 1 = Failed for an unknown reason |
| swSetValue_FrozenFeatureOwner | 5 = Owner of the dimension is frozen |
| swSetValue_InvalidValue | 2 = Not a valid value for change parameter |
| swSetValue_ModelNotLoaded | 4 = Model must be loaded in order to set this value |
| swSetValue_Successful | 0 = Successful |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
