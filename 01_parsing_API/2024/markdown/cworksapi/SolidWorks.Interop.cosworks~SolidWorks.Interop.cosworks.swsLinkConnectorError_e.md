---
title: "swsLinkConnectorError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsLinkConnectorError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLinkConnectorError_e.html"
---

# swsLinkConnectorError_e Enumeration

Link connector errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsLinkConnectorError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsLinkConnectorError_e
```

### C#

```csharp
public enum swsLinkConnectorError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsLinkConnectorError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsLinkConnectorErrorBodyExcludedFromAnalysis | 8 = Selected entity is on a body excluded from analysis |
| swsLinkConnectorErrorEmptyEntity | 5 = Either of the entities is empty |
| swsLinkConnectorErrorHasRemoteMassOrBeamBody | 7 = Connect has a remote mass or beam body |
| swsLinkConnectorErrorInvalidMesh | 1 = Invalid mesh type |
| swsLinkConnectorErrorInvalidStudy | 3 = Invalid study type |
| swsLinkConnectorErrorNonlinearStudyPartDocument | 2 = Study type equals nonlinear and document type equals part |
| swsLinkConnectorErrorSelectAssemblyDocument | 4 = Select assembly document |
| swsLinkConnectorErrorSelectVertexOrDatumPoint | 6 = Select a vertex or datum point |
| swsLinkConnectorErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
