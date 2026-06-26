---
title: "swsStudyMeshError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsStudyMeshError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsStudyMeshError_e.html"
---

# swsStudyMeshError_e Enumeration

Mesh study errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsStudyMeshError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsStudyMeshError_e
```

### C#

```csharp
public enum swsStudyMeshError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsStudyMeshError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsStudyErrorElementSizeTooBig | 4 = Element size is too large; specify a smaller element size |
| swsStudyErrorElementSizeTooSmall | 3 = Element size is too small; specify a larger element size to run successfully |
| swsStudyErrorNoSolidBody | 2 = No solid body to process |
| swsStudyErrorNoValidShells | 1 = No valid shells defined |
| swsStudyErrorSpecifyElementSizeScaleFactor | 6 = Specify a number between 0.1 and 10 for element size scale factor |
| swsStudyErrorSpecifyPositiveValue | 5 = Specify a positive value |
| swsStudyErrorSpecifyToleranceScaleFactor | 7 = Specify a number between 0.01 and 100 for tolerance scale factor |
| swsStudyErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
