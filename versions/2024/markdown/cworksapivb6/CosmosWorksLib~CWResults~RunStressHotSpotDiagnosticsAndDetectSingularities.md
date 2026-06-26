---
title: "RunStressHotSpotDiagnosticsAndDetectSingularities Method (CWResults)"
project: "SOLIDWORKS Simulation Type Library"
interface: "CWResults"
member: "RunStressHotSpotDiagnosticsAndDetectSingularities"
kind: "method"
source: "cworksapivb6/CosmosWorksLib~CWResults~RunStressHotSpotDiagnosticsAndDetectSingularities.html"
---

# RunStressHotSpotDiagnosticsAndDetectSingularities Method (CWResults)

## Syntax

### Visual Basic for Applications (VBA)

```vb
Public Function RunStressHotSpotDiagnosticsAndDetectSingularities( _
   ByVal NSensitivityFactor As Long, _
   ByVal BRunForNodes As Boolean, _
   ByVal NMeshRefineLevels As Long, _
   ByVal DElemSizeReductionFactor As Double, _
   ByVal dGrowthRatio As Double, _
   ByVal NResultsRestoreOption As Long, _
   ByRef BFoundHotSpots As Boolean, _
   ByRef BFoundSingularities As Boolean _
) As Long
```
