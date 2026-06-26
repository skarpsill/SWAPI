---
title: "swLinkDimensionError_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swLinkDimensionError_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLinkDimensionError_e.html"
---

# swLinkDimensionError_e Enumeration

Link dimension errors.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swLinkDimensionError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swLinkDimensionError_e
```

### C#

```csharp
public enum swLinkDimensionError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swLinkDimensionError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swLinkDimensionError_AlreadyLinked | 4 = Dimension already linked elsewhere |
| swLinkDimensionError_CannotLink | 8 = The selected dimensions cannot be linked; combination of failures swLinkDimensionError_LinkAcrossDocs to swLinkDimensionError_DrivenByEquation |
| swLinkDimensionError_DrivenByEquation | 7 = Dimension's driven by an equation |
| swLinkDimensionError_EmptyString | 11 = Empty string passed as link text |
| swLinkDimensionError_ErrorUknown | 0 = Unknown error occurred |
| swLinkDimensionError_IncompatibleDimTypes | 3 = Cannot link incompatible dimension types |
| swLinkDimensionError_IncompatibleValues | 6 = Incompatible range of values make these dimensions not linkable |
| swLinkDimensionError_InvalidString | 12 = Invalid string passed as link text; cannot contain the at sign (@) character |
| swLinkDimensionError_LinkAcrossDocs | 2 = Values to be linked must belong to the same model |
| swLinkDimensionError_NoError | 1 = No error; success |
| swLinkDimensionError_ReadOnlyOrDriven | 5 = Dimension is a read-only, driven, or a reference dimension that cannot be linked |
| swLinkDimensionError_UnableToCreateSharedParam | 9 = Shared parameter could not be created |
| swLinkDimensionError_UnlinkFailure | 10 = Dimension was not already linked |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
