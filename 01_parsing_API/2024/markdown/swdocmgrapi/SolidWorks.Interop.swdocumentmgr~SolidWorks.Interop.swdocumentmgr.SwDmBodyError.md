---
title: "SwDmBodyError Enumeration"
project: "SOLIDWORKS Document Manager API Help"
interface: "SwDmBodyError"
member: ""
kind: "enum"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmBodyError.html"
---

# SwDmBodyError Enumeration

Body errors.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum SwDmBodyError
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As SwDmBodyError
```

### C#

```csharp
public enum SwDmBodyError : System.Enum
```

### C++/CLI

```cpp
public enum class SwDmBodyError : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swBodyErrorDecompression | 16 = Decompression error |
| swBodyErrorFileCreation | 8 = Failed to create output/intermediate files |
| swBodyErrorNoData | 4 = Body data not present |
| swDmBodyErrorGetCountNotCalled | 1 = Before calling ISwDMConfiguration::GetBody , call ISwDMConfiguration::GetBodiesCount |
| swDmBodyErrorInvalidStorage | 2 = Invalid storage |
| swDmBodyErrorNone | 0 = Success |

## See Also

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
