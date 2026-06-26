---
title: "swLoadAddinError_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swLoadAddinError_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLoadAddinError_e.html"
---

# swLoadAddinError_e Enumeration

Add-in load errors.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swLoadAddinError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swLoadAddinError_e
```

### C#

```csharp
public enum swLoadAddinError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swLoadAddinError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAddinAlreadyLoaded | 2 |
| swAddinNotLoaded | 1 |
| swAddinsDisabled | 4 |
| swFileNotFound | 3 |
| swLicenseError | 7 |
| swLoadConflict | 5 |
| swRegistrationError | 6 |
| swSuccess | 0 |
| swUnknownError | -1 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
