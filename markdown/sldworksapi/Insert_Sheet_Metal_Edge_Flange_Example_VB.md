---
title: "Insert Sheet Metal Edge Flange Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Sheet_Metal_Edge_Flange_Example_VB.htm"
---

# Insert Sheet Metal Edge Flange Example (VBA)

This example shows how to insert a sheet metal edge flange.

'-----------------------------------------------------

'

' Preconditions: A sheet metal part is open and the edge
for

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}the
flange is selected.

'

' Postconditions: An edge flange is created.

'

'------------------------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bValuekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swEdgekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Edge

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
dAnglekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
dLengthkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFeaturekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swEntitykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Entity

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSketchkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Sketch

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vSketchSegmentskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSketchLinekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SketchLine

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swStartPointkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SketchPoint

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swEndPointkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SketchPoint

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nOptionskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SwConst.swInsertEdgeFlangeOptions_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
dSizekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
dFactor1kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
dFactor2kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
aFlangeEdges(0)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Edge

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vFlangeEdgeskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
aSketchFeats(0)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Sketch

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vSketchFeatskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variantkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Connect to SOLIDWORKS

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get active document

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Flange parameters

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Set the angle.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dAngle
= (90# / 180#) * 3.1415926535897

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dLength
= 0.01kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Position view so SelctByID2 coordinates will lead to a pick

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ShowNamedView2"*Trimetric",
-1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ViewZoomtofit2kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Select edge for flange

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bValue
= swModel.Extension.SelectByID2("",
"EDGE", 0.007817329387943, 0.001156559535341, 0.04430115457222,
False, 0, Nothing, 0)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get edge

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swEdge = swModel.SelectionManager.GetSelectedObject6(1,
-1)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Insert a sketch for an Edge Flange

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFeature = swModel.InsertSketchForEdgeFlange(swEdge,
dAngle, False)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Select

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bValue
= swFeature.Select2(False, 0)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Start sketch editing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.EditSketchkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the active sketch

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSketch = swModel.GetActiveSketch2kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Add the edge to the sketch

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Cast edge to entity

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swEntity = swEdge

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Select edge

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bValue
= swEntity.Select4(False, Nothing)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Use the edge in the sketch

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bValue
= swModel.SketchManager.SketchUseEdge(False)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the created sketch line

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vSketchSegments
= swSketch.GetSketchSegments

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSketchLine = vSketchSegments(0)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get start and end point

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swStartPoint = swSketchLine.GetStartPoint2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swEndPoint = swSketchLine.GetEndPoint2kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Create additional lines to define sketch

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Set parameters defining the sketch geometry

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dSize
= swEndPoint.X - swStartPoint.X

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dFactor1
= 0.1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dFactor2
= 1.25kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Add directly and do not display to speed things up

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.SetAddToDBTrue

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.SetDisplayWhenAddedFalse

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.CreateLine2swStartPoint.X, swStartPoint.Y,
0#, swStartPoint.X, swStartPoint.Y + dLength, 0#

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.CreateLine2swStartPoint.X, swStartPoint.Y
+ dLength, 0#, swStartPoint.X + dFactor1 * dSize, swStartPoint.Y + dFactor2
* dLength, 0#

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.CreateLine2swStartPoint.X + dFactor1
* dSize, swStartPoint.Y + dFactor2 * dLength, 0#, swEndPoint.X - dFactor1
* dSize, swStartPoint.Y + dFactor2 * dLength, 0#

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.CreateLine2swEndPoint.X - dFactor1
* dSize, swStartPoint.Y + dFactor2 * dLength, 0#, swEndPoint.X, swEndPoint.Y
+ dLength, 0#

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.CreateLine2swEndPoint.X, swEndPoint.Y,
0#, swEndPoint.X, swEndPoint.Y + dLength, 0#

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Reset

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.SetDisplayWhenAdded
True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.SetAddToDBFalse

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Commit changes made to the sketch

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.InsertSketch2Truekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Set options

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nOptions
= swInsertEdgeFlangeOptions_e.swInsertEdgeFlangeUseDefaultRadius + swInsertEdgeFlangeOptions_e.swInsertEdgeFlangeUseDefaultRelief

#If 0 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Insert the edge flange

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFeature = swModel.FeatureManager.InsertSheetMetalEdgeFlange(swEdge,
swSketch, nOptions, dAngle, 0#, swFlangePositionTypes_e.swFlangePositionTypeBendOutside,
dLength, swSheetMetalReliefTypes_e.swSheetMetalReliefNone, 0#, 0#, 0#,
swFlangeDimTypes_e.swFlangeDimTypeInnerVirtualSharp, Nothing)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

#Else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
aFlangeEdges(0) = swEdge

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
aSketchFeats(0) = swSketch

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vFlangeEdges
= aFlangeEdges

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vSketchFeats
= aSketchFeats

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFeature = swModel.FeatureManager.InsertSheetMetalEdgeFlange2((vFlangeEdges),
(vSketchFeats), nOptions, dAngle, 0#, swFlangePositionTypes_e.swFlangePositionTypeBendOutside,
dLength, swSheetMetalReliefTypes_e.swSheetMetalReliefNone, 0#, 0#, 0#,
swFlangeDimTypes_e.swFlangeDimTypeInnerVirtualSharp, Nothing)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

#End If

End Sub
