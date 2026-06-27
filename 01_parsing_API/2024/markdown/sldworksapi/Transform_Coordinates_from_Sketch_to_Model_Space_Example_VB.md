---
title: "Transform Coordinates from Sketch to Model Space Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Transform_Coordinates_from_Sketch_to_Model_Space_Example_VB.htm"
---

# Transform Coordinates from Sketch to Model Space Example (VBA)

When an entity is selected while editing a sketch, for example a sketch
point, the coordinates of the point are shown in the space of the sketch.
Sometimes it is desirable to know the coordinates of this point in the
space of the model.

This example shows how to use various transforms and math utilities
to transform a point in sketch space to model space.

'------------------------------------------------------------------

'

' Preconditions:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(1)
Part, assembly or drawing is open.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(2)
If a part or assembly, then a sketch is being edited.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(3)
If a part or assembly, then an entity is selected in

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}the
sketch.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(4)
If a drawing, then an entity is selected.

'

' Postconditions: None

'

' NOTES:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(1)
If the sketch is a 3D sketch, then the selected sketch

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}point
is automatically in model coordinates.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(2)
If the sketch is a 3D sketch, then its transform is the

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}unit
transform.

'

'------------------------------------------------------------------

Option Explicit

Public Function GetModelCoordinates _

( _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp
As SldWorks.SldWorks, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSketch
As SldWorks.sketch, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vPtArr
As Variant _

) As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swMathPtkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.MathPoint

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swMathUtilkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.MathUtility

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swMathTranskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.MathTransform

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swMathUtil = swApp.GetMathUtility

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swMathPt = swMathUtil.CreatePoint(vPtArr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Is a unit transform if 3D sketch; for example, selected sketch

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
point is automatically in model space

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swMathTrans = swSketch.ModelToSketchTransform

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swMathTrans = swMathTrans.Inverse

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swMathPt = swMathPt.MultiplyTransform(swMathTrans)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetModelCoordinates
= swMathPt.ArrayData

End Function

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelMgrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SelectionMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSketchkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.sketch

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vSketchSelPtkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vModelSelPtkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ikadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSketch = swModel.GetActiveSketch2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vSketchSelPt
= swSelMgr.GetSelectionPointInSketchSpace(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vModelSelPt
= GetModelCoordinates(swApp, swSketch, vSketchSelPt)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"File = " & swModel.GetPathName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Is3D
sketchkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swSketch.Is3D

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SelPt
(sketch space) = (" & vSketchSelPt(0) * 1000# & ", "
& vSketchSelPt(1) * 1000# & ", " & vSketchSelPt(2)
* 1000# & ") mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SelPt
(modelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}space)
= (" & vModelSelPt(0) * 1000# & ", " & vModelSelPt(1)
* 1000# & ", " & vModelSelPt(2) * 1000# & ")
mm"

End Sub

'------------------------------------------
