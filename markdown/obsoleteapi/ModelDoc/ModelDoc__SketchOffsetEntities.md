---
title: "ModelDoc::SketchOffsetEntities"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchOffsetEntities.htm"
---

# ModelDoc::SketchOffsetEntities

This
method is obsolete and is now superseded by[ModelDoc::SketchOffsetEntities2](ModelDoc__SketchOffsetEntities2.htm).

Description

This method generates entities in the active sketch by offsetting the
selected geometry by the specified amount.

Syntax (OLE Automation)

void ModelDoc.SketchOffsetEntities
( offset, flip)

(Table)=========================================================

| Input: | (double) offset | Offset distance in meters |
| --- | --- | --- |
| Input: | (BOOL) flip | TRUE if the offset direction should be flipped, FALSE otherwise |

Syntax (COM)

status = ModelDoc->SketchOffsetEntities
( offset, flip )

(Table)=========================================================

| Input: | (double) offset | Offset distance in meters |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flip | TRUE if the offset direction should be flipped, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The geometry selected for offset can be an edge,
loop, face, external sketch curve, external sketch contour, set of edges,
or set of external sketch curves.

NOTE: If
the selected geometry is a sketch item, it must be an external sketch
curve; for example, it cannot be an item in the active sketch. To offset
sketch segments within the active sketch, use ModelDoc::SketchOffset.

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
<param name="Items" value="ModelDoc_Object$$**$$ModelDoc::SketchOffset$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SketchOffsetEntities.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
