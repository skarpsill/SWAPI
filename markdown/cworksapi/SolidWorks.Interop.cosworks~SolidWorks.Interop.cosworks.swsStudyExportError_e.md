---
title: "swsStudyExportError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsStudyExportError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsStudyExportError_e.html"
---

# swsStudyExportError_e Enumeration

Export study errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsStudyExportError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsStudyExportError_e
```

### C#

```csharp
public enum swsStudyExportError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsStudyExportError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsStudyExportError_CreepMaterial | 4 = Creep material does not have the force control method |
| swsStudyExportError_DropTestNotAvailable | 3 = Drop test parameters are not exported |
| swsStudyExportError_LoadOnPointsNotAvailable | 6 = Export option is not available for load on points |
| swsStudyExportError_NoError | 0 = No error |
| swsStudyExportError_OptimizationNotAvailable | 1 = Export option is not available for an optimization study |
| swsStudyExportError_RemoteLoadConnectorNotAvailable | 5 = Export option is not available with remote load or connector |
| swsStudyExportError_TransientThermalNotAvailable | 2 = Transient thermal analysis does not have an initial temperature |
| swsStudyExportError_Wrong_NastranExportUnit | 11 = The specified unit is incorrect for the NASTRAN export option |
| swsStudyExportError_WrongCosmosExportOption | 9 = The Cosmos export option is not supported (should not exceed the value of swsCosmosExportOption_e if study export option swsStudyExportOption_e .swsStudyExport_Cosmos is selected) |
| swsStudyExportError_WrongCosmosExportOptionForNoMesh | 8 = Wrong Cosmos export option for no mesh export |
| swsStudyExportError_WrongCosmosExportUnit | 12 = The specified unit is incorrect for GEOSTAR export option |
| swsStudyExportError_WrongFileOption | 7 = The study export option is not supported (should not exceed the value of swsStudyExportOption_e ) |
| swsStudyExportError_WrongNastranExportOption | 10 = The NASTRAN export option is not supported (should not exceed the value of swsNastranExportOption_e if study export option swsStudyExportOption_e .swsStudyExport_Nastran is selected) |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
