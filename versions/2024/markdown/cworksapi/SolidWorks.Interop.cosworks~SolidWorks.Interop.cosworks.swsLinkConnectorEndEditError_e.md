---
title: "swsLinkConnectorEndEditError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsLinkConnectorEndEditError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLinkConnectorEndEditError_e.html"
---

# swsLinkConnectorEndEditError_e Enumeration

Link connector editing errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsLinkConnectorEndEditError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsLinkConnectorEndEditError_e
```

### C#

```csharp
public enum swsLinkConnectorEndEditError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsLinkConnectorEndEditError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsLinkConnectorEndEditErrorBodyExcludedFromAnalysis | 7 = Selected entity is on a body excluded from analysis |
| swsLinkConnectorEndEditErrorEntityAlreadyExists | 1 = Entity already exists |
| swsLinkConnectorEndEditErrorHasBeamBody | 5 = Connector has a beam body |
| swsLinkConnectorEndEditErrorHasMassElement | 6 = Connector has a mass element |
| swsLinkConnectorEndEditErrorNullEntity | 4 = Entity is NULL |
| swsLinkConnectorEndEditErrorSelectDatumPointOrVertices | 2 = Select a datum point or vertices |
| swsLinkConnectorEndEditErrorSelectEntity | 3 = Select an entity |
| swsLinkConnectorEndEditErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
