---
title: "ModelDoc::InsertRib2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertRib2.htm"
---

# ModelDoc::InsertRib2

This
method is obsolete and has been superseded by[ModelDoc2::InsertRib2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertRib2.htm).

Description

This method inserts a rib.

Syntax (OLE Automation)

void ModelDoc.InsertRib2 (is2Sided,
reverseThicknessDir, thickness, referenceEdgeIndex, reverseMaterialDir,
isDrafted, draftOutward, draftAngle, isNormToSketch)

(Table)=========================================================

| Input: | (BOOL) is2Sided | TRUE if the rib will be a double-sided rib or FALSE if the rib is single-sided.;
a double-sided rib will thicken on both sides of the sketch |
| --- | --- | --- |
| Input: | (BOOL) reverseThicknessDir | For single side ribs, this will thicken on the opposite side of the
sketch normal |
| Input: | (double) thickness | Rib thickness |
| Input: | (long) referenceEdgeIndex | Edge in the sketch will be used to determine the material direction
and for draft reference when the rib is drafted, the midpoint of this
edge will maintain the thickness value other points on the rib may have
a different thickness due to the draft |
| Input: | (BOOL) reverseMaterialDir | Direction the rib has material; it will be on one side or the order
side of the reference edge base on this flag |
| Input: | (BOOL) isDrafted | TRUE if the rib will be drafted, FALSE otherwise |
| Input: | (BOOL) draftOutward | TRUE to draft outwards, FALSE inwards |
| Input: | (double) draftAngle | Draft angle applied to the rib |
| Input: | (BOOL) isNormToSketch | TRUE if the rib will be normal to the sketch, FALSE if the rib will
be parallel to the sketch |

Syntax (COM)

status = ModelDoc->InsertRib2 ( is2Sided, reverseThicknessDir,
thickness, referenceEdgeIndex, reverseMaterialDir, isDrafted, draftOutward,
draftAngle, isNormToSketch )

(Table)=========================================================

| Input: | (VARIANT_BOOL) is2Sided | TRUE if the rib will be a double-sided rib or FALSE if the rib is single-sided;
a double-sided rib will thicken on both sides of the sketch |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) reverseThicknessDir | For single side ribs, this will thicken on the opposite side of the
sketch normal |
| Input: | (double) thickness | Rib thickness |
| Input: | (long) referenceEdgeIndex | Edge in the sketch will be used to determine the material direction
and for draft reference; when the rib is drafted, the midpoint of this
edge will maintain the thickness value other points on the rib may have
a different thickness due to the draft |
| Input: | (VARIANT_BOOL) reverseMaterialDir | Direction the rib has material; it will be on one side or the order
side of the reference edge base on this flag |
| Input: | (VARIANT_BOOL) isDrafted | TRUE if the rib will be drafted, FALSE otherwise |
| Input: | (VARIANT_BOOL) draftOutward | TRUE to draft outwards, FALSE inwards |
| Input: | (double) draftAngle | Draft angle applied to the rib |
| Input: | (VARIANT_BOOL) isNormToSketch | TRUE if the rib will be normal to the sketch, FALSE if the rib will
be parallel to the sketch |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__InsertRib2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
