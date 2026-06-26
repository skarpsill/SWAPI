---
title: "InsertProtrusionBlend Method (FeatureManager)"
project: "SOLIDWORKS Type Library"
interface: "FeatureManager"
member: "InsertProtrusionBlend"
kind: "method"
source: "sldworksapivb6/SldWorks~FeatureManager~InsertProtrusionBlend.html"
---

# InsertProtrusionBlend Method (FeatureManager)

## Syntax

### Visual Basic for Applications (VBA)

```vb
Public Function InsertProtrusionBlend( _
   ByVal Closed As Boolean, _
   ByVal KeepTangency As Boolean, _
   ByVal ForceNonRational As Boolean, _
   ByVal TessToleranceFactor As Double, _
   ByVal StartMatchingType As Integer, _
   ByVal EndMatchingType As Integer, _
   ByVal StartTangentLength As Double, _
   ByVal EndTangentLength As Double, _
   ByVal StartTangentDir As Boolean, _
   ByVal EndTangentDir As Boolean, _
   ByVal IsThinBody As Boolean, _
   ByVal Thickness1 As Double, _
   ByVal Thickness2 As Double, _
   ByVal ThinType As Integer, _
   ByVal Merge As Boolean, _
   ByVal UseFeatScope As Boolean, _
   ByVal UseAutoSelect As Boolean _
) As Feature
```
