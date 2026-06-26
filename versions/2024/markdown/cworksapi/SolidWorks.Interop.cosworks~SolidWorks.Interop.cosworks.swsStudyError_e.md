---
title: "swsStudyError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsStudyError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsStudyError_e.html"
---

# swsStudyError_e Enumeration

Study errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsStudyError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsStudyError_e
```

### C#

```csharp
public enum swsStudyError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsStudyError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsNewStudyErrorInvalidMeshType | 4 = Invalid mesh type |
| swsNewStudyErrorInvalidStudySubOption | 5 = Invalid study sub-option |
| swsNewStudyErrorNoSolidBody | 1 = No solid body to process |
| swsNewStudyErrorSameNameStudyExistsOrInvalidStudyName | 2 = A study with this name already exists or invalid study name |
| swsNewStudyErrorSuccessful | 0 = Successful |
| swsNewStudyErrorTypeNotDefined | 3 = Study type not defined; valid study types are 0 to 7 |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
