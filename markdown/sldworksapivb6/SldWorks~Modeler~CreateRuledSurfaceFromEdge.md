---
title: "CreateRuledSurfaceFromEdge Method (Modeler)"
project: "SOLIDWORKS Type Library"
interface: "Modeler"
member: "CreateRuledSurfaceFromEdge"
kind: "method"
source: "sldworksapivb6/SldWorks~Modeler~CreateRuledSurfaceFromEdge.html"
---

# CreateRuledSurfaceFromEdge Method (Modeler)

## Syntax

### Visual Basic for Applications (VBA)

```vb
Public Function CreateRuledSurfaceFromEdge( _
   ByVal ModDoc As ModelDoc2, _
   ByVal Edges As Variant, _
   ByVal Type As Long, _
   ByVal Length As Double, _
   ByVal FlipPullDir As Boolean, _
   ByVal FlipDir As Boolean, _
   ByVal TrimAndSew As Boolean, _
   ByVal Angle As Double, _
   ByVal CoordInput As Boolean, _
   ByVal X As Double, _
   ByVal Y As Double, _
   ByVal Z As Double, _
   ByVal BConnectSurface As Boolean, _
   ByRef RuledSurface As Object _
) As Long
```
