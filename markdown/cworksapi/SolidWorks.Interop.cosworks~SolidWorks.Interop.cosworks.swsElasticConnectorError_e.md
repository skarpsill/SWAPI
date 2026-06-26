---
title: "swsElasticConnectorError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsElasticConnectorError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsElasticConnectorError_e.html"
---

# swsElasticConnectorError_e Enumeration

Elastic connector errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsElasticConnectorError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsElasticConnectorError_e
```

### C#

```csharp
public enum swsElasticConnectorError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsElasticConnectorError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsElasticConnectorErrorBodyExcludedFromAnalysis | 10 = Selected entity is on a body excluded from analysis |
| swsElasticConnectorErrorFaceHasRemoteMassOrBeamBody | 9 = Selected face has a remote mass or has a beam body |
| swsElasticConnectorErrorInvalidArray | 4 = Invalid array |
| swsElasticConnectorErrorInvalidMesh | 1 = Invalid mesh |
| swsElasticConnectorErrorInvalidStudy | 3 = Invalid study type |
| swsElasticConnectorErrorNoEntityNoObject | 7 = No entity selected and object is empty |
| swsElasticConnectorErrorNonlinearStudyAndPartDocument | 2 = Study type equals nonlinear and document type equals part |
| swsElasticConnectorErrorNullOrEmptyArray | 8 = Array is null or empty |
| swsElasticConnectorErrorSelectFace | 5 = Select a face |
| swsElasticConnectorErrorSelectPlanarFace | 6 = Select a planar face |
| swsElasticConnectorErrorSuccessful | 0 = Successful |

## Remarks

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
