---
title: "CreateLoftBody2 Method (Modeler)"
project: "SOLIDWORKS Type Library"
interface: "Modeler"
member: "CreateLoftBody2"
kind: "method"
source: "sldworksapivb6/SldWorks~Modeler~CreateLoftBody2.html"
---

# CreateLoftBody2 Method (Modeler)

## Syntax

### Visual Basic for Applications (VBA)

```vb
Public Function CreateLoftBody2( _
   ByVal PModDoc As ModelDoc2, _
   ByVal Profile As Variant, _
   ByVal GuideCurve As Variant, _
   ByVal Centerline As Object, _
   ByVal IsThinBody As Boolean, _
   ByVal ThinType As Long, _
   ByVal Thickness1 As Double, _
   ByVal Thickness2 As Double, _
   ByVal FeatureScope As Boolean, _
   ByVal IsBlendClosed As Boolean, _
   ByVal KeepTangency As Boolean, _
   ByVal ForceNonRational As Boolean, _
   ByVal IsSolidBody As Boolean, _
   ByVal TessTolFactor As Double, _
   ByVal StartTangentLength As Double, _
   ByVal EndTangentLength As Double, _
   ByVal StartTangentDir As Boolean, _
   ByVal EndTangentDir As Boolean, _
   ByVal StartMatchingType As Long, _
   ByVal EndMatchingType As Long, _
   ByVal Merge As Boolean _
) As Body2
```
