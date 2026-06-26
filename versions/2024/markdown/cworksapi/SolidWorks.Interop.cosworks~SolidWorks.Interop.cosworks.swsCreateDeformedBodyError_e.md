---
title: "swsCreateDeformedBodyError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsCreateDeformedBodyError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCreateDeformedBodyError_e.html"
---

# swsCreateDeformedBodyError_e Enumeration

Errors during deformed body creation

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsCreateDeformedBodyError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsCreateDeformedBodyError_e
```

### C#

```csharp
public enum swsCreateDeformedBodyError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsCreateDeformedBodyError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsCreateDeformedBody_CorruptData | 1 |
| swsCreateDeformedBody_DisjointBodies | 4 |
| swsCreateDeformedBody_Failed | 7 |
| swsCreateDeformedBody_FailedToSubtractBody | 5 |
| swsCreateDeformedBody_FailToSew | 3 |
| swsCreateDeformedBody_IncorrectParameters | 6 |
| swsCreateDeformedBody_IncorrectStepNumber | 8 |
| swsCreateDeformedBody_InvalidPath | 11 |
| swsCreateDeformedBody_NoActiveStudy | 9 |
| swsCreateDeformedBody_NonSupportedStudy | 10 |
| swsCreateDeformedBody_UnfitFace | 2 |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
