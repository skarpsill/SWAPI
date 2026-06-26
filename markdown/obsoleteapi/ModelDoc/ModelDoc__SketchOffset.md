---
title: "ModelDoc::SketchOffset"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchOffset.htm"
---

# ModelDoc::SketchOffset

This
method is obsolete and has been superseded by[ModelDoc::SketchOffset2](ModelDoc__SketchOffset2.htm).

Description

This method offsets the selected sketch segments.

Syntax (OLE Automation)

void ModelDoc.SketchOffset (offset,
chainMode)

(Table)=========================================================

| Input: | (double) offset | Offset value; negative value will offset in opposite
direction |
| --- | --- | --- |
| Input: | (BOOL) chainMode | TRUE if you want entire chain of entities offset,
FALSE if you want only selected sketch entities offset |

Syntax (COM)

status = ModelDoc->SketchOffset (offset, chainMode)

(Table)=========================================================

| Input: | (double) offset | Offset value; negative value will offset in opposite
direction |
| --- | --- | --- |
| Input: | (BOOL) chainMode | TRUE if you want entire chain of entities offset,
FALSE if you want only selected sketch entities offset |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Specifying TRUE to the chainMode argument offsets
the selected entity and any other entities that belong to the same contour
or chain.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="16777215" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZCreateSketchEntity$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SketchOffset.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
