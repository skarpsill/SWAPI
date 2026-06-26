---
title: "AddForce3 Method (CWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation Type Library"
interface: "CWLoadsAndRestraintsManager"
member: "AddForce3"
kind: "method"
source: "cworksapivb6/CosmosWorksLib~CWLoadsAndRestraintsManager~AddForce3.html"
---

# AddForce3 Method (CWLoadsAndRestraintsManager)

## Syntax

### Visual Basic for Applications (VBA)

```vb
Public Function AddForce3( _
   ByVal ForceType As Long, _
   ByVal SelectionType As Long, _
   ByVal RefDirType As Long, _
   ByVal InterpolationMode As Long, _
   ByVal DistPercentageOpt As Long, _
   ByVal NumOfRows As Long, _
   ByVal DistValue As Variant, _
   ByVal ForceValue As Variant, _
   ByVal NonUniformLoading As Boolean, _
   ByVal NULoadingOnBeam As Boolean, _
   ByVal NonUniformLoadDistDef As Long, _
   ByVal NonUniformLoadDistType As Long, _
   ByVal Ucode As Long, _
   ByVal TorqueNFVal As Double, _
   ByVal Comps As Variant, _
   ByVal FlipOrigin As Boolean, _
   ByVal IsCurvedBeam As Boolean, _
   ByVal DispArray As Variant, _
   ByVal RefGeom As Object, _
   ByVal PerUnitLength As Boolean, _
   ByRef ErrorCode As Long _
) As CWForce
```
