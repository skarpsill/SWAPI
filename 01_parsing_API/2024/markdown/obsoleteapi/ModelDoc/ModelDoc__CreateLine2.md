---
title: "ModelDoc::CreateLine2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateLine2.htm"
---

# ModelDoc::CreateLine2

This
method is obsolete and has been superseded by[ModelDoc2::CreateLine2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__CreateLine2.htm).

Description

This method creates a sketch line in the currently
active 2D or 3D sketch.

Syntax (OLE Automation)

retval = ModelDoc.CreateLine2 ( xStart, yStart, zStart,
xEnd, yEnd, zEnd )

(Table)=========================================================

| Input: | (double) xStart | X value of the line start point |
| --- | --- | --- |
| Input: | (double) yStart | Y value of the line start point |
| Input: | (double) zStart | Z value of the line start point |
| Input: | (double) xEnd | X value of the line end point |
| Input: | (double) yEnd | Y value of the line end point |
| Input: | (double)zEnd | Z value of the line end oint |
| Return: | (LPDISPATCH) retval | Pointer to a dispatch object, the newly created
SketchSegment object; if the operation fails, then NULL is returned |

Syntax (COM)

status = ModelDoc->ICreateLine2 ( xStart, yStart,
zStart, xEnd, yEnd, zEnd, &retval )

(Table)=========================================================

| Input: | (double) xStart | X value of the line start point |
| --- | --- | --- |
| Input: | (double) yStart | Y value of the line start point |
| Input: | (double) zStart | Z value of the line start point |
| Input: | (double) xEnd | X value of the line end point |
| Input: | (double) yEnd | Y value of the line end point |
| Input: | (double) zEnd | Z value of the line end oint |
| Output: | (LPSKETCHSEGMENT) retval | Pointer to the newly created SketchSegment object;
if the operation fails, then NULL is returned |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

If a sketch is not active, then thekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}line
is not be created and NULL is returned. You can check for an active sketch
using the ModelDoc::GetActiveSketch2 method.

For COM applications, obtain the underlying SketchLine
object using QueryInterface on the SketchSegment object returned. C++
Dispatch applications can define a new SketchLine or SketchSegment object,
which uses this dispatch pointer. Visual Basic applications interpret
the pointer for you automatically so you can use the returned object to
call SketchSegment or SketchLine functions.

ModelDoc::SetAddToDB and ModelDoc::SetDisplayWhenAdded increase performance
during entity creation by adding entities directly to the SolidWorks database.
ModelDoc::SetAddToDB avoids inferencing.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZCreateSketchEntity$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\ModelDoc\ModelDoc__CreateLine2.htm" >
<param name="_ID" value="RelatedTopic0" >
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
<param name="Items" value="Create_Sketch_Line_With_Visual_Properties_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\ModelDoc\ModelDoc__CreateLine2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
