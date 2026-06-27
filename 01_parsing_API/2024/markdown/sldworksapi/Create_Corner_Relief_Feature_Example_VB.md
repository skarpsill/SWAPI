---
title: "Create Corner Relief Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Corner_Relief_Feature_Example_VB.htm"
---

# Create Corner Relief Feature Example (VBA)

This example shows how to create a corner relief feature.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' Open public_documents\samples\tutorial\sheetmetal\formtools\cover.sldprt.
 '
 ' Postconditions:
 ' 1. The model is rotated to the back view.
 ' 2. An edge flange is created.
 ' 3. The model is rotated slightly about the x-axis.
 ' 4. A corner relief feature is created:
 '    * A rectangular corner relief is added to one corner of the edge flange.
 '    * An obround corner relief is added to another corner of the edge flange.
 '----------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp            As SldWorks.SldWorks
     Dim swModel          As SldWorks.ModelDoc2
     Dim bValue           As Boolean
     Dim swEdge           As SldWorks.Edge
     Dim dAngle           As Double
     Dim dLength          As Double
     Dim swFeature        As SldWorks.Feature
     Dim swEntity         As SldWorks.Entity
     Dim swSketch         As SldWorks.Sketch
     Dim vSketchSegments  As Variant
     Dim swSketchLine     As SldWorks.SketchLine
     Dim swStartPoint     As SldWorks.SketchPoint
     Dim swEndPoint       As SldWorks.SketchPoint
     Dim nOptions         As SwConst.swInsertEdgeFlangeOptions_e
     Dim dSize            As Double
     Dim dFactor1         As Double
     Dim dFactor2         As Double
     Dim aFlangeEdges(0)  As SldWorks.Edge
     Dim vFlangeEdges     As Variant
     Dim aSketchFeats(0)  As SldWorks.Sketch
     Dim vSketchFeats     As Variant
    ' Connect to SOLIDWORKS
     Set swApp = Application.SldWorks
    ' Get active document
     Set swModel = swApp.ActiveDoc
    ' Flange parameters
    ' Set the angle
     dAngle = (90# / 180#) * 3.1415926535897
    dLength = 0.01
    ' Rotate model so that IModelDocExtension::SelectByID2 coordinates can be found
     swModel.ShowNamedView2 "*Back", -1
     swModel.ViewZoomtofit2
    ' Select edge for flange
     bValue = swModel.Extension.SelectByID2("", "EDGE", 3.72105002552985E-02, 0.052846642716446, -9.93711211094706E-06, False, 0, Nothing, 0)
    ' Get edge
     Set swEdge = swModel.SelectionManager.GetSelectedObject6(1, -1)
    ' Insert a sketch for an edge flange
     Set swFeature = swModel.InsertSketchForEdgeFlange(swEdge, dAngle, False)
    ' Select
     bValue = swFeature.Select2(False, 0)
    ' Start sketch editing
     swModel.EditSketch
    ' Get the active sketch
     Set swSketch = swModel.SketchManager.ActiveSketch
    ' Add the edge to the sketch
    ' Cast edge to entity
     Set swEntity = swEdge
    ' Select edge
     bValue = swEntity.Select4(False, Nothing)
    ' Use the edge in the sketch
     bValue = swModel.SketchManager.SketchUseEdge(False)
    ' Get the created sketch line
     vSketchSegments = swSketch.GetSketchSegments
    Set swSketchLine = vSketchSegments(0)
    ' Get start and end point
     Set swStartPoint = swSketchLine.GetStartPoint2
     Set swEndPoint = swSketchLine.GetEndPoint2

     ' Create additional lines to define sketch
     ' Set parameters defining the sketch geometry
     dSize = swEndPoint.X - swStartPoint.X
     dFactor1 = 0.1
     dFactor2 = 1.25

     swModel.SetAddToDB True
     swModel.SetDisplayWhenAdded False
    swModel.SketchManager.CreateLine swStartPoint.X, swStartPoint.Y, 0#, swStartPoint.X, swStartPoint.Y + dLength, 0#
     swModel.SketchManager.CreateLine swStartPoint.X, swStartPoint.Y + dLength, 0#, swStartPoint.X + dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0#
     swModel.SketchManager.CreateLine swStartPoint.X + dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0#, swEndPoint.X - dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0#
     swModel.SketchManager.CreateLine swEndPoint.X - dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0#, swEndPoint.X, swEndPoint.Y + dLength, 0#
     swModel.SketchManager.CreateLine swEndPoint.X, swEndPoint.Y, 0#, swEndPoint.X, swEndPoint.Y + dLength, 0#
    ' Reset
     swModel.SetDisplayWhenAdded True
     swModel.SetAddToDB False
    ' Commit changes made to the sketch
     swModel.SketchManager.InsertSketch True
    ' Set options
     nOptions = swInsertEdgeFlangeOptions_e.swInsertEdgeFlangeUseDefaultRadius + swInsertEdgeFlangeOptions_e.swInsertEdgeFlangeUseDefaultRelief
    Set aFlangeEdges(0) = swEdge
     Set aSketchFeats(0) = swSketch
    vFlangeEdges = aFlangeEdges
     vSketchFeats = aSketchFeats
    Set swFeature = swModel.FeatureManager.InsertSheetMetalEdgeFlange2((vFlangeEdges), (vSketchFeats), nOptions, dAngle, 0#, swFlangePositionTypes_e.swFlangePositionTypeBendOutside, dLength, swSheetMetalReliefTypes_e.swSheetMetalReliefNone, 0#, 0#, 0#, swFlangeDimTypes_e.swFlangeDimTypeInnerVirtualSharp, Nothing)
    ' Rotate view so that IModelDocExtension::SelectByID2 coordinates can be found
     Dim myModelView As SldWorks.ModelView
     Set myModelView = swModel.ActiveView
     myModelView.RotateAboutCenter 45, 9.11235438195936E-03
    ' Select the sheet metal body to which to apply a corner relief
     bValue = swModel.Extension.SelectByID2("Edge-Flange1", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)
     swModel.ClearSelection2 True
    ' Specify two corners of the edge flange for which to create a corner relief
    ' Select faces that define the first corner
     bValue = swModel.Extension.SelectByID2("", "FACE", 5.49242492243928E-02, 0.053073918098565, 2.42634000000049E-02, True, 4, Nothing, 0)
     bValue = swModel.Extension.SelectByID2("", "FACE", 2.76778697571744E-02, 5.30739180985651E-02, -1.04170971004399E-03, True, 4, Nothing, 0)
     Dim myCorner As Long
     myCorner = swModel.FeatureManager.AddCornerReliefCorner()
    ' Specify the type of corner relief to apply to the first corner
     Dim myReliefType As Boolean
     myReliefType = swModel.FeatureManager.AddCornerReliefType(-1, swCornerSquareRelief, 0.0001, 0.0007366, 0.00018415, False, False, False, True, False)
     swModel.ClearSelection2 True
    ' Select faces that define the second corner
     bValue = swModel.Extension.SelectByID2("", "FACE", 2.76778697571744E-02, 5.30739180985651E-02, -1.04170971004399E-03, True, 4, Nothing, 0)
     bValue = swModel.Extension.SelectByID2("", "FACE", 4.31490289955978E-04, 0.053073918098565, 2.42634000000049E-02, True, 4, Nothing, 0)
     myCorner = swModel.FeatureManager.AddCornerReliefCorner()
    ' Specify the type of corner relief to apply to the second corner
     myReliefType = swModel.FeatureManager.AddCornerReliefType(-1, swCornerObroundRelief, 0.0001, 0.0029464, 0.0007366, False, False, False, False, False)
    ' Create the corner relief feature
     Dim myFeature As SldWorks.Feature
     Set myFeature = swModel.FeatureManager.FinishCornerRelief()

End Sub
```
