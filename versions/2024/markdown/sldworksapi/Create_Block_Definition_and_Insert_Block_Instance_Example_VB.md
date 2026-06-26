---
title: "Create Block Definition and Insert Block Instance Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Block_Definition_and_Insert_Block_Instance_Example_VB.htm"
---

# Create Block Definition and Insert Block Instance Example (VBA)

This example shows how to create a block definition and insert a block
instance in a drawing.

'---------------------------------------------------------------------------
' Preconditions: Open a drawing document.
'
' Postconditions:
'kadov_tag{{<spaces>}}1. Creates a block definition.
'kadov_tag{{<spaces>}}2. Inserts a first instance of the block in the upper-left corner
of the
' drawing sheet.
'kadov_tag{{<spaces>}}3. Inserts a second instance of the block in the drawing
sheet.
'---------------------------------------------------------------------------

Option Explicit

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDrawkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.DrawingDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSkSeg(13)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SketchSegment

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSkPt(3)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SketchPoint

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSkNote(2)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Note

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vSkSegkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vSkPtkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vSkNotekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSketchBlockDefkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SketchBlockDefinition

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swBlockInstkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SketchBlockInstance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSketchMgrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SketchManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelDocExtkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDocExtension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swMathUtilkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.MathUtility

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swMathPointkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.MathPoint

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nPt(2)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vPtkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nbrSelObjectskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.**ActiveDoc**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDraw = swModel

kadov_tag{{<spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSketchMgr = swModel.SketchManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModelDocExt = swModel.Extension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swMathUtil = swApp.GetMathUtility

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSketchMgr.AddToDB= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Revision box

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSkSeg(0) = swSketchMgr.CreateLine(0.008372353756316,
0.207929860362, 0#, 0.05495488122133, 0.207929860362, 0#)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSkSeg(1) = swSketchMgr.CreateLine(0.05495488122133,
0.207929860362, 0#, 0.05495488122133, 0.1992788195471, 0#)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSkSeg(2) = swSketchMgr.CreateLine(0.05495488122133,
0.1992788195471, 0#, 0.008372353756316, 0.1992788195471, 0#)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSkSeg(3) = swSketchMgr.CreateLine(0.008372353756316,
0.1992788195471, 0#, 0.008372353756316, 0.207929860362, 0#)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSkSeg(4) = swSketchMgr.CreateLine(0.023613610833382,
0.207929860362, 0#, 0.023613610833382, 0.1992788195471, 0#)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSkSeg(5) = swSketchMgr.CreateLine(0.03964919362569,
0.207929860362, 0#, 0.03964919362569, 0.1992788195471, 0#)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Clear selections; otherwise, notes are attached to line

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ClearSelection2True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Revision notes

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSkNote(0) = swModel.InsertNote("Cell
1")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSkNote(1) = swModel.InsertNote("Cell
2")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSkNote(2) = swModel.InsertNote("Cell
3")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}PositionNote
swApp, swModel, swSkNote(0), 0.009481461553102, 0.2052680016497, 0#

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}PositionNote
swApp, swModel, swSkNote(1), 0.025613610833382, 0.2052680016497, 0#

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}PositionNote
swApp, swModel, swSkNote(2), 0.04275469545669, 0.2052680016497, 0#

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Points for circles

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSkPt(0) = swSketchMgr.CreatePoint(0.02700536474232,
0.1708856599494, 0#)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSkPt(1) = swSketchMgr.CreatePoint(0.02700536474232,
0.1815330947985, 0#)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSkPt(2) = swSketchMgr.CreatePoint(0.03964919362569,
0.1815330947985, 0#)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSkPt(3) = swSketchMgr.CreatePoint(0.05029662847483,
0.1708856599494, 0#)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Circles

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSkSeg(6) = swSketchMgr.CreateCircle(swSkPt(0).X,
swSkPt(0).Y, swSkPt(0).Z, 0.03050393605009, 0.169349494074, 0#)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSkSeg(7) = swSketchMgr.CreateCircle(swSkPt(1).X,
swSkPt(1).Y, swSkPt(1).Z, 0.03305243799009, 0.183621104938, 0#)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSkSeg(8) = swSketchMgr.CreateCircle(swSkPt(2).X,
swSkPt(2).Y, swSkPt(2).Z, 0.04426584652606, 0.182092003774, 0#)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSkSeg(9) = swSketchMgr.CreateCircle(swSkPt(3).X,
swSkPt(3).Y, swSkPt(3).Z, 0.05496955467404, 0.164252490194, 0#)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Lines between circles

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSkSeg(10) = swSketchMgr.CreateLine(swSkPt(0).X,
swSkPt(0).Y, swSkPt(0).Z, swSkPt(1).X, swSkPt(1).Y, swSkPt(1).Z)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSkSeg(11) = swSketchMgr.CreateLine(swSkPt(1).X,
swSkPt(1).Y, swSkPt(1).Z, swSkPt(2).X, swSkPt(2).Y, swSkPt(2).Z)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSkSeg(12) = swSketchMgr.CreateLine(swSkPt(2).X,
swSkPt(2).Y, swSkPt(2).Z, swSkPt(3).X, swSkPt(3).Y, swSkPt(3).Z)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSkSeg(13) = swSketchMgr.CreateLine(swSkPt(3).X,
swSkPt(3).Y, swSkPt(3).Z, swSkPt(0).X, swSkPt(0).Y, swSkPt(0).Z)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vSkSeg
= swSkSeg

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vSkPt
= swSkPt

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vSkNote
= swSkNote

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nbrSelObjects
= swModelDocExt.MultiSelect2(vSkSeg,
True, Nothing)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nbrSelObjects
= swModelDocExt.MultiSelect2(vSkPt,
True, Nothing)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nbrSelObjects
= swModelDocExt.MultiSelect2(vSkNote,
True, Nothing)

kadov_tag{{<spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSketchBlockDef = swSketchMgr.MakeSketchBlockFromSelected(Nothing)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}'
Define an insertion point

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nPt(0)
= 60# / 1000#

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nPt(1)
= 60# / 1000#

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nPt(2)
= 0#

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vPt
= nPt

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swMathPoint = swMathUtil.CreatePoint(vPt)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Insert an instance of the block definition

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swBlockInst = swSketchMgr.InsertSketchBlockInstance(swSketchBlockDef,
swMathPoint, 1, 0)

kadov_tag{{<spaces>}}swSketchMgr.AddToDB= False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Redraw to see all changes

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.GraphicsRedraw2

End Sub

Sub PositionNote (swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2,
swSkNote As SldWorks.Note, X_pos As Double, Y_pos As Double, Z_pos As
Double)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAnnkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Annotation

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nRetValkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swAnn = swSkNote.GetAnnotation

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSkNote.Angle
= 0#

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swSkNote.SetBalloon(swBS_None,
swBF_Tightest)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

nRetVal
= swAnn.SetLeader3(swLeaderStyle_e.swBENT, swLS_SMART,
True, False, False, False)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swAnn.SetPosition2(X_pos, Y_pos,
Z_pos)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Redraw to see changes

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.GraphicsRedraw2

End Sub
