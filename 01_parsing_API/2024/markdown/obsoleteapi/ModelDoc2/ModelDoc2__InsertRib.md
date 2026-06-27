---
title: "ModelDoc2::InsertRib"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertRib.htm"
---

# ModelDoc2::InsertRib

This method is obsolete and has been superseded
by[ModelDoc2::InsertRib2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertRib2.htm).

Description

This method inserts a rib.

Syntax (OLE Automation)

void ModelDoc2.InsertRib
( is2Sided, reverseThicknessDir, thickness, referenceEdgeIndex, reverseMaterialDir,
isDrafted, draftOutward, draftAngle)

(Table)=========================================================

| Input: | (BOOL) is2Sided | TRUE if the rib is double-sided, FALSE if single-sided; a double-sided
rib thickens
on both sides of the sketch |
| --- | --- | --- |
| Input: | (BOOL) reverseThicknessDir | Thicken on the opposite side of the sketch normal for single-sided ribs |
| Input: | (double) thickness | Rib thickness |
| Input: | (long) referenceEdgeIndex | Edge in the sketch to us to determine the material direction and for
draft reference; when the rib is drafted, the mid point of this edge maintains
the thickness value; other points on the rib may have a different thickness
due to the draft |
| Input: | (BOOL) reverseMaterialDir | Direction the rib has material; it can be on one side or the order side
of the reference edge base on this flag |
| Input: | (BOOL) isDrafted | TRUE if the rib will be drafted, FALSE otherwise |
| Input: | (BOOL) draftOutward | TRUE to draft outwards, FALSE inwards |
| Input: | (double) draftAngle | Draft angle applied to the rib |

Syntax (COM)

status = ModelDoc2->InsertRib
( is2Sided, reverseThicknessDir, thickness, referenceEdgeIndex, reverseMaterialDir,
isDrafted, draftOutward, draftAngle )

(Table)=========================================================

| Input: | (VARIANT_BOOL) is2Sided | TRUE if the rib is double-sided, FALSE if single-sided; a double-sided
rib thickens
on both sides of the sketch |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) reverseThicknessDir | Thicken on the opposite side of the sketch normal for single-sided ribs |
| Input: | (double) thickness | Rib thickness |
| Input: | (long) referenceEdgeIndex | Edge in the sketch to us to determine the material direction and for
draft reference; when the rib is drafted, the mid point of this edge maintains
the thickness value; other points on the rib may have a different thickness
due to the draft |
| Input: | (VARIANT_BOOL) reverseMaterialDir | Direction the rib has material; it can be on one side or the order side
of the reference edge base on this flag |
| Input: | (VARIANT_BOOL) isDrafted | TRUE if the rib will be drafted, FALSE otherwise |
| Input: | (VARIANT_BOOL) draftOutward | TRUE to draft outwards, FALSE inwards |
| Input: | (double) draftAngle | Draft angle applied to the rib |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc2\ModelDoc2__InsertRib.htm" >
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc2\ModelDoc2__InsertRib.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
