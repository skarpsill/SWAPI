---
title: "ModelDoc2::FeatureCutThin"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__FeatureCutThin.htm"
---

# ModelDoc2::FeatureCutThin

This method is obsolete and has been superseded
by[ModelDoc2::FeatureCutThin2](ModelDoc2__FeatureCutThin2.htm).

Description

This method creates a feature
by extruding a profile. A constant thickness is applied to the profile
during extrusion. The result is then removed from the existing work piece.

Syntax (OLE Automation)

(void) ModelDoc2.FeatureCutThin
( sd, flip, dir, t1, t2, d1, d2, dchk1, dchk2, ddir1, ddir2, dang1, dang2,
offsetReverse1, offsetReverse2, thk1, thk2, capThk, thinType, capEnds,
addFillets, filletRad )

(Table)=========================================================

| Input: | (BOOLEAN) sd | TRUE for single-ended, FALSE for double-ended |
| --- | --- | --- |
| Input: | (BOOL) flip | Flip side to cut; TRUE if you want to remove the material outside of
the profile |
| Input: | (BOOL) dir | Reverse direction; TRUE if you want Direction 1 to be opposite the default
direction |
| Input: | (long) t1 | Termination type for first end as defined in swEndConditions_e |
| Input: | (long) t2 | Termination type for second end as defined in swEndConditions_e |
| Input: | (double) d1 | Depth of extrusion for first end in meters |
| Input: | (double) d2 | Depth of extrusion for second end in meters |
| Input: | (BOOLEAN) dchk1 | TRUE allows draft angle in first direction, FALSE does not allow drafting |
| Input: | (BOOLEAN) dchk2 | TRUE allows draft angle in second direction, FALSE does not allow drafting |
| Input: | (BOOLEAN) ddir1 | TRUE for first draft angle to be inward, FALSE for draft angle outward |
| Input: | (BOOLEAN) ddir2 | TRUE for second draft angle to be inward, FALSE for draft angle outward |
| Input: | (double) dang1 | Draft angle for first end |
| Input: | (double) dang2 | Draft angle for second end |
| Input: | (BOOLEAN) offsetReverse1 | TRUE specifies offset in direction away from the sketch if you chose
to offset the first end condition from another face or plane, FALSE specifies
offset from the face or plane in a direction toward the sketch |
| Input: | (BOOLEAN) offsetReverse2 | TRUE specifies offset in direction away from the sketch if you chose
to offset the first second condition from another face or plane, FALSE
specifies offset from the face or plane in a direction toward the sketch |
| Input: | (double) thk1 | Wall thickness 1 (midplane type uses (thk1)/2 for each direction) |
| Input: | (double) thk2 | Wall thickness 2 (only used when thinType = 3) |
| Input: | (double) capThk | End cap thickness (only used when capEnds = 1) |
| Input: | (long) thinType | Thin feature type: 0
= one direction 1
= one direction reverse 2
= midplane 3
= two direction |
| Input: | (long) capEnds | Cap the ends: 0
= no cap 1
= cap (base features only) |
| Input: | (BOOLEAN) addFillets | TRUE to add auto fillets (open profile base features only) |
| Input: | (double) filletRad | Fillet radii if addFillets is TRUE |

Syntax (COM)

status = ModelDoc2->FeatureCutThin
( sd, flip, dir, t1, t2, d1, d2, dchk1, dchk2, ddir1, ddir2, dang1, dang2,
offsetReverse1, offsetReverse2, thk1, thk2, capThk, thinType, capEnds,
addFillets, filletRad )

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
| Input: | (double) thk1 | Wall thickness 1 (midplane uses (thk1)/2 for each direction) |
| Input: | (double) thk2 | Wall thickness 2 (only used when thinType = 3) |
| Input: | (double) capThk | end cap thickness (only used when capEnds = 1) |
| Input: | (long) thinType | Thin feature type: 0
= one direction 1
= one direction reverse 2
= midplane 3
= two direction |
| Input: | (long) capEnds | Cap the ends: 0
= no cap 1
= cap (base features only) |
| Input: | (BOOLEAN) addFillets | TRUE to add auto fillets (open profile base features only) |
| Input: | (double) filletRad | Fillet radii if addFillets is TRUE |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The default direction for cut operations is opposite the sketch normal.
The default direction for boss operations is along the sketch normal.
Setting the dir argument to TRUE reverses the default direction. For double-ended
extrusions, Direction 2 is always opposite to Direction 1.

The default sketch normal is the same as the face or pPlane normal where
the sketch was placed. To determine this normal vector, see Face::Normal
and RefPlane::GetRefPlaneParams, respectively.

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc2\ModelDoc2__FeatureCutThin.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc2\ModelDoc2__FeatureCutThin.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
