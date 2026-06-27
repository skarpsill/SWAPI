---
title: "ModelDoc::SketchModifyTranslate"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchModifyTranslate.htm"
---

# ModelDoc::SketchModifyTranslate

This
method is obsolete and has been superseded by[ModelDoc2::SketchModifyTranslate](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SketchModifyTranslate.htm).

Description

This method translates the coordinate system
of the active or selected sketch.

Syntax (OLE Automation)

void ModelDoc.SketchModifyTranslate ( startX, startY,
endX, endY)

(Table)=========================================================

| Input: | (double) startX | X sketch value defining "from" position |
| --- | --- | --- |
| Input: | (double) startY | Y sketch value defining "from" position |
| Input: | (double) endX | X sketch value defining "to" position |
| Input: | (double) endY | Y sketch value defining "to" position |

Syntax (COM)

status = ModelDoc-> SketchModifyTranslate (double
startX, double startY, double endX, double endY )

(Table)=========================================================

| Input: | (double) startX | X sketch value defining "from" position |
| --- | --- | --- |
| Input: | (double) startY | Y sketch value defining "from" position |
| Input: | (double) endX | X sketch value defining "to" position |
| Input: | (double) endY | Y sketch value defining "to" position |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The sketch 9s translated from the XY start-point
position, to the XY end-point position.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
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
<param name="Items" value="ModelDoc_Object$$**$$ZModifySketch$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__SketchModifyTranslate.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
