---
title: "ICreateBlockDefinition Method (DrawingDoc)"
project: "SOLIDWORKS Type Library"
interface: "DrawingDoc"
member: "ICreateBlockDefinition"
kind: "method"
source: "sldworksapivb6/SldWorks~DrawingDoc~ICreateBlockDefinition.html"
---

# ICreateBlockDefinition Method (DrawingDoc)

## Syntax

### Visual Basic for Applications (VBA)

```vb
Public Function ICreateBlockDefinition( _
   ByVal Name As String, _
   ByVal XRefFileName As String, _
   ByVal Instance As Boolean, _
   ByVal SegmentCount As Long, _
   ByVal Segments As SketchSegment, _
   ByVal PointCount As Long, _
   ByVal Points As SketchPoint, _
   ByVal NoteCount As Long, _
   ByVal Notes As Note, _
   ByVal DimensionCount As Long, _
   ByVal Dimensions As DisplayDimension, _
   ByVal BlockCount As Long, _
   ByVal Blocks As BlockInstance _
) As BlockDefinition
```
