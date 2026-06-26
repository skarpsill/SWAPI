---
title: "ICreateLoftSurface Method (Modeler)"
project: "SOLIDWORKS Type Library"
interface: "Modeler"
member: "ICreateLoftSurface"
kind: "method"
source: "sldworksapivb6/SldWorks~Modeler~ICreateLoftSurface.html"
---

# ICreateLoftSurface Method (Modeler)

## Syntax

### Visual Basic for Applications (VBA)

```vb
Public Function ICreateLoftSurface( _
   ByVal NCurves As Long, _
   ByVal CurveArray As Curve, _
   ByVal BBlendClosed As Boolean, _
   ByVal BForceCubic As Boolean, _
   ByVal NGuides As Long, _
   ByVal GuideCrvArray As Curve, _
   ByVal StartMatchingType As Long, _
   ByVal EndMatchingType As Long, _
   ByVal NormalAtStartSection As MathVector, _
   ByVal NormalAtEndSection As MathVector, _
   ByVal NStartMatchingFaces As Long, _
   ByVal StartMatchingFaceList As Face2, _
   ByVal NEndMatchingFaces As Long, _
   ByVal EndMatchingFaceList As Face2, _
   ByVal DegeneratedStart As Boolean, _
   ByVal DegeneratedEnd As Boolean, _
   ByVal StartPointOfStartSection As MathPoint, _
   ByVal StartPointOfEndSection As MathPoint, _
   ByVal SectionIndexStart As Long, _
   ByVal SectionIndexEnd As Long, _
   ByVal GuideIndexStart As Long, _
   ByVal GuideIndexEnd As Long _
) As Surface
```
