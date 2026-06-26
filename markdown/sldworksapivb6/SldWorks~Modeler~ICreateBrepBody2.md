---
title: "ICreateBrepBody2 Method (Modeler)"
project: "SOLIDWORKS Type Library"
interface: "Modeler"
member: "ICreateBrepBody2"
kind: "method"
source: "sldworksapivb6/SldWorks~Modeler~ICreateBrepBody2.html"
---

# ICreateBrepBody2 Method (Modeler)

## Syntax

### Visual Basic for Applications (VBA)

```vb
Public Function ICreateBrepBody2( _
   ByVal Type As Integer, _
   ByVal NTopologies As Integer, _
   ByRef Topologies As Integer, _
   ByRef EdgeTolArray As Double, _
   ByRef VertexTolArray As Double, _
   ByRef PointArray As Double, _
   ByVal CurveArray As Curve, _
   ByVal SurfaceArray As Surface, _
   ByVal NRelations As Integer, _
   ByRef Parents As Integer, _
   ByRef Children As Integer, _
   ByRef Senses As Integer _
) As Body2
```
