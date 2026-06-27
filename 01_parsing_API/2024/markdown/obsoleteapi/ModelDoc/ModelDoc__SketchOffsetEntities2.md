---
title: "ModelDoc::SketchOffsetEntities2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchOffsetEntities2.htm"
---

# ModelDoc::SketchOffsetEntities2

This
method is obsolete and has been superseded by[ModelDoc2::SketchOffsetEntities2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SketchOffsetEntities2.htm).

Description

This method generates entities in the active sketch by offsetting the
selected geometry by the specified amount.

Syntax (OLE Automation)

retval = ModelDoc.SketchOffsetEntities2 ( offset,
bothDirections, chain )

(Table)=========================================================

| Input: | (double) offset | Offset distance in meters |
| --- | --- | --- |
| Input: | (BOOL) bothDirections | TRUE to offset in both directions |
| Input: | (BOOL) chain | TRUE if you want entire chain of entities offset,
FALSE if you want only selected sketch entities offset |
| Return: | (BOOL) retval | TRUE if the offset was successful |

Syntax (COM)

status = ModelDoc->SketchOffsetEntities2 ( offset,
bothDirections, chain, &retval )

(Table)=========================================================

| Input: | (double) offset | Offset distance in meters |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) bothDirections | TRUE to offset in both directions |
| Input: | (VARIANT_BOOL) chain | TRUE if you want entire chain of entities offset,
FALSE if you want only selected sketch entities offset |
| Output: | (VARIANT_BOOL) retval | TRUE if the offset was successful |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The geometry selected for offset can be an edge,
loop, face, external sketch curve, external sketch contour, set of edges,
or set of external sketch curves.

Specifying TRUE to the chain argument offsets the
selected entity and any other entities that belong to the same contour
or chain; for example, contiguous geometric entities like edges.

NOTE: If
the selected geometry is a sketch item, it must be an external sketch
curve; for example, it cannot be an item in the active sketch. To offset
sketch segments within the active sketch, usekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ModelDoc::SketchOffset.

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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SketchOffsetEntities2.htm" >
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SketchOffsetEntities2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
