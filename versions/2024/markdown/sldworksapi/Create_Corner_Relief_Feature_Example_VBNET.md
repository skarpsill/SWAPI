---
title: "Create Corner Relief Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Corner_Relief_Feature_Example_VBNET.htm"
---

# Create Corner Relief Feature Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim bValue As Boolean
         Dim swEdge As Edge
         Dim dAngle As Double
         Dim dLength As Double
         Dim swFeature As Feature
         Dim swEntity As Entity
         Dim swSketch As Sketch
         Dim vSketchSegments As Object
         Dim swSketchLine As SketchLine
         Dim swStartPoint As SketchPoint
         Dim swEndPoint As SketchPoint
         Dim nOptions As swInsertEdgeFlangeOptions_e
         Dim dSize As Double
         Dim dFactor1 As Double
         Dim dFactor2 As Double
         Dim aFlangeEdges(0) As Edge
         Dim vFlangeEdges As Object
         Dim aSketchFeats(0) As Sketch
         Dim vSketchFeats As Object

         ' Get active document
         swModel = swApp.ActiveDoc

         ' Flange parameters

         ' Set the angle
         dAngle = (90.0# / 180.0#) * 3.1415926535897

         dLength = 0.01

         ' Rotate model so that IModelDocExtension::SelectByID2 coordinates can be found
         swModel.ShowNamedView2("*Back", -1)
         swModel.ViewZoomtofit2()

         ' Select edge for flange
         bValue = swModel.Extension.SelectByID2("", "EDGE", 0.0372105002552985, 0.052846642716446, -0.00000993711211094706,  False, 0,  Nothing, 0)

         ' Get edge
         swEdge = swModel.SelectionManager.GetSelectedObject6(1, -1)

         ' Insert a sketch for an edge flange
         swFeature = swModel.InsertSketchForEdgeFlange(swEdge, dAngle, False)

         ' Select
         bValue = swFeature.Select2(False, 0)

         ' Start sketch editing
         swModel.EditSketch()

         ' Get the active sketch
         swSketch = swModel.SketchManager.ActiveSketch

         ' Add the edge to the sketch

         ' Cast edge to entity
         swEntity = swEdge

         ' Select edge
         bValue = swEntity.Select4(False, Nothing)

         ' Use the edge in the sketch
         bValue = swModel.SketchManager.SketchUseEdge(False)

         ' Get the created sketch line
         vSketchSegments = swSketch.GetSketchSegments

         swSketchLine = vSketchSegments(0)

         ' Get start and end point
         swStartPoint = swSketchLine.GetStartPoint2
         swEndPoint = swSketchLine.GetEndPoint2

         ' Create additional lines to define sketch
         ' Set parameters defining the sketch geometry
         dSize = swEndPoint.X - swStartPoint.X
         dFactor1 = 0.1
         dFactor2 = 1.25

         swModel.SetAddToDB(True)
         swModel.SetDisplayWhenAdded(False)

         swModel.SketchManager.CreateLine(swStartPoint.X, swStartPoint.Y, 0.0#, swStartPoint.X, swStartPoint.Y + dLength, 0.0#)
         swModel.SketchManager.CreateLine(swStartPoint.X, swStartPoint.Y + dLength, 0.0#, swStartPoint.X + dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0.0#)
         swModel.SketchManager.CreateLine(swStartPoint.X + dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0.0#, swEndPoint.X - dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0.0#)
         swModel.SketchManager.CreateLine(swEndPoint.X - dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0.0#, swEndPoint.X, swEndPoint.Y + dLength, 0.0#)
         swModel.SketchManager.CreateLine(swEndPoint.X, swEndPoint.Y, 0.0#, swEndPoint.X, swEndPoint.Y + dLength, 0.0#)

         ' Reset
         swModel.SetDisplayWhenAdded(True)
         swModel.SetAddToDB(False)

         ' Commit changes made to the sketch
         swModel.SketchManager.InsertSketch(True)

         ' Set options
         nOptions = swInsertEdgeFlangeOptions_e.swInsertEdgeFlangeUseDefaultRadius + swInsertEdgeFlangeOptions_e.swInsertEdgeFlangeUseDefaultRelief

         aFlangeEdges(0) = swEdge
         aSketchFeats(0) = swSketch

         vFlangeEdges = aFlangeEdges
         vSketchFeats = aSketchFeats

         swFeature = swModel.FeatureManager.InsertSheetMetalEdgeFlange2((vFlangeEdges), (vSketchFeats), nOptions, dAngle, 0.0#, swFlangePositionTypes_e.swFlangePositionTypeBendOutside, dLength, swSheetMetalReliefTypes_e.swSheetMetalReliefNone, 0.0#, 0.0#, 0.0#, swFlangeDimTypes_e.swFlangeDimTypeInnerVirtualSharp,  Nothing)

         ' Rotate view so that IModelDocExtension::SelectByID2 coordinates can be found
         Dim myModelView As ModelView
         myModelView = swModel.ActiveView
         myModelView.RotateAboutCenter(45, 0.00911235438195936)

         ' Select the sheet metal body to which to apply a corner relief
         bValue = swModel.Extension.SelectByID2("Edge-Flange1", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)
         swModel.ClearSelection2(True)

         ' Specify two corners of the edge flange for which to create a corner relief

         ' Select faces that define the first corner
         bValue = swModel.Extension.SelectByID2("", "FACE", 0.0549242492243928, 0.053073918098565, 0.0242634000000049,  True, 4,  Nothing, 0)
         bValue = swModel.Extension.SelectByID2("", "FACE", 0.0276778697571744, 0.0530739180985651, -0.00104170971004399,  True, 4,  Nothing, 0)
         Dim myCorner As Long
         myCorner = swModel.FeatureManager.AddCornerReliefCorner()

         ' Specify the type of corner relief to apply to the first corner
         Dim myReliefType As Boolean
         myReliefType = swModel.FeatureManager.AddCornerReliefType(-1, swCornerReliefType_e.swCornerSquareRelief, 0.0001, 0.0007366, 0.00018415, False, False, False, True, False)
         swModel.ClearSelection2(True)

         ' Select faces that define the second corner
         bValue = swModel.Extension.SelectByID2("", "FACE", 0.0276778697571744, 0.0530739180985651, -0.00104170971004399,  True, 4,  Nothing, 0)
         bValue = swModel.Extension.SelectByID2("", "FACE", 0.000431490289955978, 0.053073918098565, 0.0242634000000049,  True, 4,  Nothing, 0)
         myCorner = swModel.FeatureManager.AddCornerReliefCorner()

         ' Specify the type of corner relief to apply to the second corner
         myReliefType = swModel.FeatureManager.AddCornerReliefType(-1, swCornerReliefType_e.swCornerObroundRelief, 0.0001, 0.0029464, 0.0007366, False, False, False, False, False)

         ' Create the corner relief feature
         Dim myFeature As Feature
         myFeature = swModel.FeatureManager.FinishCornerRelief()

     End Sub

     Public swApp As SldWorks

 End  Class
```
