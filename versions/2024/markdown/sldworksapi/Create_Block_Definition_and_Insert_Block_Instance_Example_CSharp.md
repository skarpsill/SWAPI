---
title: "Create Block Definition and Insert Block Instance Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Block_Definition_and_Insert_Block_Instance_Example_CSharp.htm"
---

# Create Block Definition and Insert Block Instance Example (C#)

This example shows how to create a block definition and insert a block
instance in a drawing.

//---------------------------------------------------------------------------
// Preconditions: Open a drawing document.
//
// Postconditions:
//kadov_tag{{<spaces>}}1. Creates a block definition.
//kadov_tag{{<spaces>}}2. Inserts a first instance of the block in the upper-left corner
of the
// drawing sheet.
//kadov_tag{{<spaces>}}3. Inserts a second instance of the block in the
drawing
sheet.
//---------------------------------------------------------------------------

using System;

using System.Collections.Generic;

using System.Text;

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;

namespace SketchBlocks.csproj

{

kadov_tag{{<spaces>}}partialkadov_tag{{</spaces>}}class SolidWorksMacro

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
void Main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SldWorks.SldWorks
swApp = new SldWorks.SldWorks();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ModelDoc2
swModel;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ModelDoc2
swModel2;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}DrawingDoc
swDraw;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SketchSegment[]
swSkSeg = new SketchSegment[14];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SketchPoint[]
swSkPt = new SketchPoint[4];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Note[]
swSkNote = new Note[3];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Object
vSkSeg;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Object
vSkPt;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Object
vSkNote;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SketchBlockDefinition
swSketchBlockDef;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SketchBlockInstance
swBlockInst;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SketchManager
swSketchMgr;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ModelDocExtension
swModelDocExt;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MathUtility
swMathUtil;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MathPoint
swMathPoint;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double[]
nPt = new double[3];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Object
vPt;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int nbrSelObjects;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel
= swApp.IActiveDoc2;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDraw
= (DrawingDoc)swModel;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//Interfaces
needed for block APIs

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSketchMgr
= swModel.SketchManager;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModelDocExt
= swModel.Extension;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swMathUtil
= swApp.IGetMathUtility();

kadov_tag{{<spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSketchMgr.AddToDB= true;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Revision box

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSkSeg[0]
= (SketchSegment)swSketchMgr.CreateLine(0.008372353756316,
0.207929860362, 0, 0.05495488122133, 0.207929860362, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSkSeg[1]
= (SketchSegment)swSketchMgr.CreateLine(0.05495488122133,
0.207929860362, 0, 0.05495488122133, 0.1992788195471, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSkSeg[2]
= (SketchSegment)swSketchMgr.CreateLine(0.05495488122133,
0.1992788195471, 0, 0.008372353756316, 0.1992788195471, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSkSeg[3]
= (SketchSegment)swSketchMgr.CreateLine(0.008372353756316,
0.1992788195471, 0, 0.008372353756316, 0.207929860362, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSkSeg[4]
= (SketchSegment)swSketchMgr.CreateLine(0.023613610833382,
0.207929860362, 0, 0.023613610833382, 0.1992788195471, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSkSeg[5]
= (SketchSegment)swSketchMgr.CreateLine(0.03964919362569,
0.207929860362, 0, 0.03964919362569, 0.1992788195471, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Clear selections; otherwise, notes are attached to line

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ClearSelection2(true);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Revision notes

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSkNote[0]
= (Note)swModel.InsertNote("Cell
1");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSkNote[1]
= (Note)swModel.InsertNote("Cell
2");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSkNote[2]
= (Note)swModel.InsertNote("Cell
3");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}PositionNote(swModel,
swSkNote[0], 0.009481461553102, 0.2052680016497, 0.0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}PositionNote(swModel,
swSkNote[1], 0.025613610833382, 0.2052680016497, 0.0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}PositionNote(swModel,
swSkNote[2], 0.04275469545669, 0.2052680016497, 0.0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Points for circles

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSkPt[0]
= (SketchPoint)swSketchMgr.CreatePoint(0.02700536474232,
0.1708856599494, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSkPt[1]
= (SketchPoint)swSketchMgr.CreatePoint(0.02700536474232,
0.1815330947985, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSkPt[2]
= (SketchPoint)swSketchMgr.CreatePoint(0.03964919362569,
0.1815330947985, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSkPt[3]
= (SketchPoint)swSketchMgr.CreatePoint(0.05029662847483,
0.1708856599494, 0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Circles

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSkSeg[6]
= (SketchSegment)swSketchMgr.CreateCircle(swSkPt[0].X,
swSkPt[0].Y, swSkPt[0].Z, 0.03050393605009, 0.169349494074, 0.0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSkSeg[7]
= (SketchSegment)swSketchMgr.CreateCircle(swSkPt[1].X,
swSkPt[1].Y, swSkPt[1].Z, 0.03305243799009, 0.183621104938, 0.0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSkSeg[8]
= (SketchSegment)swSketchMgr.CreateCircle(swSkPt[2].X,
swSkPt[2].Y, swSkPt[2].Z, 0.04426584652606, 0.182092003774, 0.0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSkSeg[9]
= (SketchSegment)swSketchMgr.CreateCircle(swSkPt[3].X,
swSkPt[3].Y, swSkPt[3].Z, 0.05496955467404, 0.164252490194, 0.0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

//
Lines between circles

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSkSeg[10]
= (SketchSegment)swSketchMgr.CreateLine(swSkPt[0].X,
swSkPt[0].Y, swSkPt[0].Z, swSkPt[1].X, swSkPt[1].Y, swSkPt[1].Z);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSkSeg[11]
= (SketchSegment)swSketchMgr.CreateLine(swSkPt[1].X,
swSkPt[1].Y, swSkPt[1].Z, swSkPt[2].X, swSkPt[2].Y, swSkPt[2].Z);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSkSeg[12]
= (SketchSegment)swSketchMgr.CreateLine(swSkPt[2].X,
swSkPt[2].Y, swSkPt[2].Z, swSkPt[3].X, swSkPt[3].Y, swSkPt[3].Z);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSkSeg[13]
= (SketchSegment)swSketchMgr.CreateLine(swSkPt[3].X,
swSkPt[3].Y, swSkPt[3].Z, swSkPt[0].X, swSkPt[0].Y, swSkPt[0].Z);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vSkSeg
= swSkSeg;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vSkPt
= swSkPt;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vSkNote
= swSkNote;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

//
Select all sketch segments, sketch points,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
and notes for the block definition

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nbrSelObjects
= swModelDocExt.MultiSelect2(vSkSeg,
true, null);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nbrSelObjects
= swModelDocExt.MultiSelect2(vSkPt,
true, null);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nbrSelObjects
= swModelDocExt.MultiSelect2(vSkNote,
true, null);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//Create
block definition

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSketchBlockDef
= swSketchMgr.MakeSketchBlockFromSelected(null);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel2
= (ModelDoc2)swApp.ActiveDoc;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSketchMgr
= swModel2.SketchManager;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Define an insertion point

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nPt[0]
= 60.0 / 1000.0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nPt[1]
= 60.0 / 1000.0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nPt[2]
= 0.0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vPt
= nPt;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swMathPoint
= (MathPoint)swMathUtil.CreatePoint(vPt);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

//
Insert an instance of the block definition

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swBlockInst
= swSketchMgr.InsertSketchBlockInstance(swSketchBlockDef, swMathPoint,
1, 0);

kadov_tag{{<spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSketchMgr.AddToDB= false;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Redraw to see all changes

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel2.GraphicsRedraw2();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}static
private void PositionNote(ModelDoc2 swModel, Note swSkNote, double X_pos,
double Y_pos, double Z_pos)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Annotation
swAnn;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int nRetVal;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bool
bRet;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swAnn
= (Annotation)swSkNote.GetAnnotation();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSkNote.Angle= 0.0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swSkNote.SetBalloon((int)swBalloonStyle_e.swBS_None,
(int)swBalloonFit_e.swBF_Tightest);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nRetVal
= swAnn.SetLeader3((int)swLeaderStyle_e.swBENT, (int)swLeaderSide_e.swLS_SMART,
true, false, false, false);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swAnn.SetPosition2(X_pos, Y_pos,
Z_pos);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Redraw to see changes; however, this is expensive

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.GraphicsRedraw2();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

public SldWorks
swApp;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

}
