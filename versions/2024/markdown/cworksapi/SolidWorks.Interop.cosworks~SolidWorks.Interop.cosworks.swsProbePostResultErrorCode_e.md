---
title: "swsProbePostResultErrorCode_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsProbePostResultErrorCode_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsProbePostResultErrorCode_e.html"
---

# swsProbePostResultErrorCode_e Enumeration

Results probe error codes

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsProbePostResultErrorCode_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsProbePostResultErrorCode_e
```

### C#

```csharp
public enum swsProbePostResultErrorCode_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsProbePostResultErrorCode_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsProbePostResultError_ActiveStudyIsNotRun | 6 = Active Simulation study must be analyzed before results can be probed |
| swsProbePostResultError_InitializationFailure | 11 = Unable to probe results; re-run the study and try again |
| swsProbePostResultError_InvalidOrEmptyInputArray | 5 = Invalid or empty node/element list |
| swsProbePostResultError_MeshDataLoadFailure | 7 = Unable to load mesh data; remesh the study and try again |
| swsProbePostResultError_NoActiveStudy | 2 = No active study found; activate a Simulation study and try again |
| swsProbePostResultError_NoActiveView | 1 = No active view is available |
| swsProbePostResultError_NoAssociatedStudyFoundForFatigueAnalysis | 12 = No associated study for fatigue analysis was found |
| swsProbePostResultError_NoResultOrMeshPlotIsActivated | 13 = No mesh or result plot was found; re-run the study and try again |
| swsProbePostResultError_NotAllNodeElemsAreAnnotated | 14 = Not all of the specified nodes or elements are annotated |
| swsProbePostResultError_ProbingNotSupportedOnDeformationPlot | 9 = Probing is not supported for deformation result plot |
| swsProbePostResultError_ProbingNotSupportedOnSectionPlotExplodedAfterClip | 10 = Probing is not supported for exploded after clip section result plot |
| swsProbePostResultError_ProbingNotSupportedOnShellForSectionPlot | 8 = Probing is not supported for shell or section result plot |
| swsProbePostResultError_ResultPlotActivationFailure | 3 = Failed to activate the selected result plot |
| swsProbePostResultError_Success | 0 |
| swsProbePostResultError_UsedBeforeCallingBeginProbing | 4 = Cannot make the current results probe edit; call ICWResultsProbeManager::BeginProbing before making results probe edits |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
