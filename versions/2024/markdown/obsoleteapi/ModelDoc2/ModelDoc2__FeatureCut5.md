---
title: "ModelDoc2::FeatureCut5"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__FeatureCut5.htm"
---

# ModelDoc2::FeatureCut5

This method is obsolete and has been superseded
by[FeatureManager::FeatureCut](sldworksAPI.chm::/FeatureManager/FeatureManager__FeatureCut.htm).

Description

This method creates a cut feature in this model
document.

Syntax (OLE Automation)

void = ModelDoc2.FeatureCut5 ( sd, flip, dir, t1,
t2, d1, d2, dchk1, dchk2, ddir1, ddir2, dang1, dang2, offsetReverse1,
offsetReverse2, translateSurface1, translateSurface2, keepPieceIndex,
normalCut )

(Table)=========================================================

| Input: | (VARIANT_BOOL) sd | TRUE for single ended, FALSE for double ended |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flip | Flip side to cut; TRUE if you want to remove the material outside of
the profile |
| Input: | (VARIANT_BOOL) dir | Reverse direction; TRUE if you want Direction1 to be opposite the default
direction |
| Input: | (long) t1 | Termination type for first end as defined in swEndConditions_e |
| Input: | (long) t2 | Termination type for second end as defined in swEndConditions_e |
| Input: | (double) d1 | Depth of extrusion for first end in meters |
| Input: | (double) d2 | Depth of extrusion for second end in meters |
| Input: | (VARIANT_BOOL) dchk1 | TRUE allows draft angle in first direction, FALSE does not allow drafting |
| Input: | (VARIANT_BOOL) dchk2 | TRUE allows draft angle in second direction, FALSE does not allow drafting |
| Input: | (VARIANT_BOOL) ddir1 | For first draft angle to be inward use TRUE, for draft angle outward
use FALSE |
| Input: | (VARIANT_BOOL) ddir2 | For second draft angle to be inward use TRUE, for draft angle outward
use FALSE |
| Input: | (double) dang1 | Draft angle for first end |
| Input: | (double) dang2 | Draft angle for second end |
| Input: | (VARIANT_BOOL) offsetReverse1 | TRUE specifies offset in direction away from the sketch if you chose
to offset the first end condition from another face or plane, FALSE specifies
offset from the face or plane in a direction toward the sketch |
| Input: | (VARIANT_BOOL) offsetReverse2 | TRUE specifies offset in direction away from the sketch if you chose
to offset the second end condition from another face or plane, FALSE specifies
offset from the face or plane in a direction toward the sketch |
| Input: | (VARIANT_BOOL) translateSurface1 | TRUE specifies that the end of the extrusion is a translation of the
reference surface when you choose swEndcondOffsetFromSurface as the termination
type for the first end, FALSE specifies to use a true offset |
| Input: | (VARIANT_BOOL) translateSurface2 | TRUE specifies that the end of the extrusion is a translation of the
reference surface when you choose swEndcondOffsetFromSurface as the termination
type for the second end, FALSE specifies to use a true offset |
| Input: | (long) keepPieceIndex | Piece to keep if ambiguity exists |
| Input: | (VARIANT_BOOL) normalCut | TRUE uses the normal cut option, FALSE does not; this parameter applies
only to sheet metal parts; non-sheet metal parts should use FALSE; when
adding a cut to the folded sheet metal part, you can set this parameter
to TRUE to ensure that the cut is created normal to the sheet metal thickness |

Syntax (COM)

status = ModelDoc2->FeatureCut5 ( sd, flip, dir,
t1, t2, d1, d2, dchk1, dchk2, ddir1, ddir2, dang1, dang2, offsetReverse1,
offsetReverse2, translateSurface1, translateSurface2, keepPieceIndex,
normalCut )

Parameters Table Start

(Table)=========================================================

| Input: | (VARIANT_BOOL) sd | TRUE for single-ended, FALSE for double-ended |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flip | Flip side to cut; TRUE if you want to remove the material outside of
the profile |
| Input: | (VARIANT_BOOL) dir | Reverse direction; TRUE if you want Direction 1 to be opposite the default
direction |
| Input: | (long) t1 | Termination type for first end as defined in swEndConditions_e |
| Input: | (long) t2 | Termination type for second end as defined in swEndConditions_e |
| Input: | (double) d1 | Depth of extrusion for first end in meters |
| Input: | (double) d2 | Depth of extrusion for second end in meters |
| Input: | (VARIANT_BOOL) dchk1 | TRUE allows draft angle in first direction, FALSE does not allow drafting |
| Input: | (VARIANT_BOOL) dchk2 | TRUE allows draft angle in second direction, FALSE does not allow drafting |
| Input: | (VARIANT_BOOL) ddir1 | TRUE for first draft angle to be inward, FALSE for draft angle outward |
| Input: | (VARIANT_BOOL) ddir2 | TRUE for second draft angle to be inward, FALSE for draft angle outward |
| Input: | (double) dang1 | Draft angle for first end |
| Input: | (double) dang2 | Draft angle for second end |
| Input: | (VARIANT_BOOL) offsetReverse1 | TRUE specifies offset in direction away from the sketch if you chose
to offset the first end condition from another face or plane, FALSE specifies
offset from the face or plane in a direction toward the sketch |
| Input: | (VARIANT_BOOL) offsetReverse2 | TRUE specifies offset in direction away from the sketch if you chose
to offset the second end condition from another face or plane, FALSE specifies
offset from the face or plane in a direction toward the sketch |
| Input: | (VARIANT_BOOL) translateSurface1 | TRUE specifies that the end of the extrusion is a translation of the
reference surface when you choose swEndcondOffsetFromSurface as the termination
type for the first end, FALSE specifies to use a true offset |
| Input: | (VARIANT_BOOL) translateSurface2 | TRUE specifies that the end of the extrusion is a translation of the
reference surface when you choose swEndcondOffsetFromSurface as the termination
type for the second end, FALSE specifies to use a true offset |
| Input: | (long) keepPieceIndex | Piece to keep if ambiguity exists |
| Input: | (VARIANT_BOOL) normalCut | TRUE uses the normal cut option, FALSE does not; this parameter applies
only to sheet metal parts; non-sheet metal parts should use FALSE; when
adding a cut to the folded sheet metal part, you can set this parameter
to TRUE to ensure that the cut is created normal to the sheet metal thickness |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The default direction for cut operations is opposite
the sketch normal. The default direction for boss operations is along
the sketch normal. Setting the dir argument to TRUE reverses the default
direction. For double-ended extrusions, Direction2 is always opposite
to Direction1.

The default sketch normal is the same as the face
or plane normal where the sketch was placed. To determine this normal
vector, see Face2::Normal and RefPlane::Transform, respectively.

When there is ambiguity in the result of a cut,
the keepPieceIndex is used to resolve which of the possible results is
used. This can be set to -1 if there is no ambiguity; otherwise, it should
be the index of the result, starting from 0 (up to 1less than the possible
number of outcomes.)

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__FeatureCut5.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__FeatureCut5.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
