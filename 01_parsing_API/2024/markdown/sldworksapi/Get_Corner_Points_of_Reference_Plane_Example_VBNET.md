---
title: "Get Corner Points of a Reference Plane Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Corner_Points_of_Reference_Plane_Example_VBNET.htm"
---

# Get Corner Points of a Reference Plane Example (VB.NET)

This example shows how to obtain the four corner points of a reference plane.

```
'-----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part.
' 2. Creates 3DSketch1 containing four corner points of the reference plane.
' 3. Gets the coordinates of each corner point.
' 4. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'----------------------------------------------------------------------------
```

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}Dim
swModel As ModelDoc2
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
boolstatus As Boolean
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFeature As Feature
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swRefPlane As RefPlane
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelExt As ModelDocExtension
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelMgr As SelectionMgr
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vMathPoints As Object
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vArrayData As Object
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
pMathPoint As MathPoint
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
i As Integer
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSketch As Sketch
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
sketchMgr As SketchManager
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
sketchPt As SketchPoint
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swRefPlaneFeatData As RefPlaneFeatureData
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
filename As String
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
errors As Long
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
warnings As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Sub
main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}filename
= "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\swutilities\bracket_a.sldprt"
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel
= swApp.**OpenDoc6**(filename, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent,
"", errors, warnings)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModelExt
= swModel.**Extension**kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelMgr
= swModel.**SelectionManager**kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sketchMgr
= swModel.**SketchManager**kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelExt.**SelectByID2**("Plane4", "PLANE", 0, 0,
0, False, 0, Nothing, swSelectOption_e.swSelectOptionDefault)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFeature
= swSelMgr.**GetSelectedObject6**(1, -1)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swRefPlane
= swFeature.**GetSpecificFeature2**kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vMathPoints
= swRefPlane.CornerPoints'Four
(4) MathPoint objects are always returned
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sketchMgr.**Insert3DSketch**(True)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i = 0 To UBound(vMathPoints)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vArrayData
= vMathPoints(i).**ArrayData**kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("
Point x = " & vArrayData(0))
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("
Point y = " & vArrayData(1))
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("
Point z = " & vArrayData(2))
Debug.Print("")
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sketchPt
= sketchMgr.**CreatePoint**(vArrayData(0), vArrayData(1), vArrayData(2))
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
i
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sketchMgr.**Insert3DSketch(True)**kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Public
swApp As SldWorks

End Class
