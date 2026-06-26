---
title: "swsRunStudiesErrorCode_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsRunStudiesErrorCode_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRunStudiesErrorCode_e.html"
---

# swsRunStudiesErrorCode_e Enumeration

Error codes for studies run in batch mode

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsRunStudiesErrorCode_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsRunStudiesErrorCode_e
```

### C#

```csharp
public enum swsRunStudiesErrorCode_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsRunStudiesErrorCode_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsRunStudiesErrorCode_AllStudiesRunFailed | 4 |
| swsRunStudiesErrorCode_FewStudiesRunFailed | 5 |
| swsRunStudiesErrorCode_InvalidStudiesAreSelected | 2 |
| swsRunStudiesErrorCode_NoActiveStudy | 6 |
| swsRunStudiesErrorCode_NoStudyIsSelectedOrDefined | 1 |
| swsRunStudiesErrorCode_Success | 0 |
| swsRunStudiesErrorCode_UnknownError | 3 |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
