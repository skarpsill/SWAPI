---
title: "swComponentReloadError_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swComponentReloadError_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swComponentReloadError_e.html"
---

# swComponentReloadError_e Enumeration

Codes returned when reloading components in assemblies.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swComponentReloadError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swComponentReloadError_e
```

### C#

```csharp
public enum swComponentReloadError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swComponentReloadError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swComponentLightWeightError | 8 |
| swDocumentAlreadyOpenedError | 12 |
| swDocumentEventError | 13 |
| swDocumentHasNoView | 11 |
| swDocumentNotChanged | 14 |
| swFileDoesntExistError | 9 |
| swFileInvalidOrSameNameError | 10 |
| swFileNotSavedError | 5 |
| swFutureVersionError | 2 |
| swInvalidComponentError | 6 |
| swInvalidOption | 4 |
| swModifiedNotReloadedError | 3 |
| swReadOnlyChanged | 16 |
| swReloadCancel | 15 |
| swReloadOkay | 0 |
| swUnexpectedError | 7 |
| swWriteAccessError | 1 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
