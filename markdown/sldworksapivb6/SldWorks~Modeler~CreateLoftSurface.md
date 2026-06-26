---
title: "CreateLoftSurface Method (Modeler)"
project: "SOLIDWORKS Type Library"
interface: "Modeler"
member: "CreateLoftSurface"
kind: "method"
source: "sldworksapivb6/SldWorks~Modeler~CreateLoftSurface.html"
---

# CreateLoftSurface Method (Modeler)

## Syntax

### Visual Basic for Applications (VBA)

```vb
Public Function CreateLoftSurface( _
   ByVal CurveArray As Variant, _
   ByVal BBlendClosed As Boolean, _
   ByVal BForceCubic As Boolean, _
   ByVal GuideCrvArray As Variant, _
   ByVal StartMatchingType As Long, _
   ByVal EndMatchingType As Long, _
   ByVal NormalAtStartSection As Object, _
   ByVal NormalAtEndSection As Object, _
   ByVal StartMatchingFaceList As Variant, _
   ByVal EndMatchingFaceList As Variant, _
   ByVal DegeneratedStart As Boolean, _
   ByVal DegeneratedEnd As Boolean, _
   ByVal StartPointOfStartSection As Object, _
   ByVal StartPointOfEndSection As Object, _
   ByVal SectionIndexStart As Long, _
   ByVal SectionIndexEnd As Long, _
   ByVal GuideIndexStart As Long, _
   ByVal GuideIndexEnd As Long _
) As Object
```
