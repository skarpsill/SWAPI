---
title: "ICreateBrepBody3 Method (Modeler)"
project: "SOLIDWORKS Type Library"
interface: "Modeler"
member: "ICreateBrepBody3"
kind: "method"
source: "sldworksapivb6/SldWorks~Modeler~ICreateBrepBody3.html"
---

# ICreateBrepBody3 Method (Modeler)

## Syntax

### Visual Basic for Applications (VBA)

```vb
Public Function ICreateBrepBody3( _
   ByVal Type As Integer, _
   ByVal NTopologies As Integer, _
   ByRef Topologies As Integer, _
   ByRef EdgeTolArray As Double, _
   ByRef VertexTolArray As Double, _
   ByRef PointArray As Double, _
   ByVal CurveArra1 As Curve, _
   ByVal CurveSurfaceArray1 As Surface, _
   ByVal CurveArray2 As Curve, _
   ByVal CurveSurfaceArray2 As Surface, _
   ByVal SurfaceArray As Surface, _
   ByVal NRelations As Integer, _
   ByRef Parents As Integer, _
   ByRef Children As Integer, _
   ByRef Senses As Integer, _
   ByVal Option As Long _
) As Body2
```
