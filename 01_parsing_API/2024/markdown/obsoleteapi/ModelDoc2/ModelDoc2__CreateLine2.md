---
title: "ModelDoc2::CreateLine2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateLine2.htm"
---

# ModelDoc2::CreateLine2

This method is obsolete and has been superseded
by[SketchManager::CreateLine](sldworksAPI.chm::/SketchManager/SketchManager__CreateLine.htm).

Description

This method creates a sketch line in the currently
active 2D or 3D sketch.

Syntax (OLE Automation)

retval = ModelDoc2.CreateLine2 ( xStart, yStart,
zStart, xEnd, yEnd, zEnd )

(Table)=========================================================

| Input: | (double )p1x | X value of the line start point |
| --- | --- | --- |
| Input: | (double) p1y | Y value of the line start point |
| Input: | (double) p1z | Z value of the line start point |
| Input: | (double) p2x | X value of the line end point |
| Input: | (double) p2y | Y value of the line end point |
| Input: | (double) p2z | Z value of the line end point |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created
SketchSegment object; if the operation fails, then NULL is returned |

Syntax (COM)

status = ModelDoc2->ICreateLine2 ( xStart, yStart,
zStart, xEnd, yEnd, zEnd, &retval )

(Table)=========================================================

| Input: | (double) p1x | X value of the line start point |
| --- | --- | --- |
| Input: | (double) p1y | Y value of the line start point |
| Input: | (double) p1z | Z value of the line start point |
| Input: | (double) p2x | X value of the line end point |
| Input: | (double) p2y | Y value of the line end point |
| Input: | (double) p2z | Z value of the line end point |
| Output: | (LPSKETCHSEGMENT) retval | Pointer to the newly created SketchSegment object;
if the operation fails, then NULL is returned |
| Return: | (HRESULT) status | S_OK if successful; S_FALSE otherwise |

Remarks

If a sketch is not active, then the line is not
created and NULL is returned. You can check for an active sketch using
the ModelDoc2::GetActiveSketch2 function.

For COM applications, the underlying SketchLine
object can be obtained using QueryInterface on the SketchSegment object
returned. C++ Dispatch applications can define a new ISketchLine or ISketchSegment
object that uses this Dispatch pointer. Visual Basic applications interpret
the pointer for you automatically so you can use the returned object to
call SketchSegment or SketchLine functions.

ModelDoc2::SetAddToDB and ModelDoc2::SetDisplayWhenAdded increase performance
during entity creation by adding entities directly to the SolidWorks database.
ModelDoc2::SetAddToDB also avoids inferencing.

When this method is used with a drawing document, this method creates
the line relative to the active drawing view, DrawingDoc::ActiveDrawingView.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__CreateLine2.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc2_Object$$**$$CreatePoint2$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__CreateLine2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic4
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="EXGetAssemblyBoundingBox$$**$$EXCreateSketchLine$$**$$EXCalcClosestDistanceFaces$$**$$EXIntersectFaces$$**$$EXCreateSectionViewAtLocation$$**$$EXClosestDistanceBetweenModelComponents$$**$$EXOutsideEdgesFace$$**$$EXReturnUntrimmedCurve$$**$$EXCreateBlockDefinitionCSharp$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__CreateLine2.htm" >
<param name="_ID" value="RelatedTopic4" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
