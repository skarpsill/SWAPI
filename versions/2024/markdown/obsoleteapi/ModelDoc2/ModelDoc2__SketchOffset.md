---
title: "ModelDoc2::SketchOffset"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SketchOffset.htm"
---

# ModelDoc2::SketchOffset

This
method is now obsolete and has been superseded by[ModelDoc2::SketchOffset2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SketchOffset2.htm).

Description

This method offsets the selected sketch segments.

Syntax (OLE Automation)

void ModelDoc2.SketchOffset (offset,
chainMode)

(Table)=========================================================

| Input: | (double) offset | Offset value; negative value offsets in opposite
direction |
| --- | --- | --- |
| Input: | (BOOL) chainMode | TRUE if you want entire chain of entities offset,
FALSE if you want only selected sketch entities offset |

Syntax (COM)

status = ModelDoc2->SketchOffset (offset, chainMode)

(Table)=========================================================

| Input: | (double) offset | Offset value; negative value offset in opposite
direction |
| --- | --- | --- |
| Input: | (BOOL) chainMode | TRUE if you want entire chain of entities offset,
FALSE if you want only selected sketch entities offset |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Specifying TRUE for chainMode offsets the selected
entity and any other entities that belong to the same contour or chain.

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc2\ModelDoc2__SketchOffset.htm" >
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
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc2\ModelDoc2__SketchOffset.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
