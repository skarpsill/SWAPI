---
title: "ModelDoc::FeatureBossThin"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FeatureBossThin.htm"
---

# ModelDoc::FeatureBossThin

This
method is obsolete and has been superseded by[ModelDoc2::FeatureBossThin](../ModelDoc2/ModelDoc2__FeatureBossThin.htm).

Description

This method creates a feature by extruding
a profile. A constant thickness is applied to the to profile during the
extrusion. The result is then added to the existing work piece.

Syntax (OLE Automation)

(void) ModelDoc.FeatureBossThin
( sd, flip, dir, t1, t2, d1, d2, dchk1, dchk2, ddir1, ddir2, dang1, dang2,
offsetReverse1, offsetReverse2, thk1, thk2, capThk, thinType, capEnds,
addFillets, filletRad )

(Table)=========================================================

| Input: | (BOOL) sd | TRUE for single ended, FALSE for double ended |
| --- | --- | --- |
| Input: | (BOOL) flip | Not used |
| Input: | (BOOL) dir | Reverse direction; TRUE if you want Direction1 to be opposite the default
direction |
| Input: | (long) t1 | Termination type for first end |
| Input: | (long) t2 | Termination type for second end |
| Input: | (double) d1 | Depth of extrusion for first end in meters |
| Input: | (double) d2 | Depth of extrusion for second end in meters |
| Input: | (BOOL) dchk1 | TRUE allows draft angle in first direction, FALSE does not allow drafting |
| Input: | (BOOL) dchk2 | TRUE allows draft angle in second direction, FALSE does not allow drafting |
| Input: | (BOOL) ddir1 | For first draft angle to be inward use TRUE, for draft angle outward
use FALSE |
| Input: | (BOOL) ddir2 | For second draft angle to be inward use TRUE, for draft angle outward
use FALSE |
| Input: | (double) dang1 | Draft angle for first end |
| Input: | (double) dang2 | Draft angle for second end |
| Input: | (BOOL) offsetReverse1 | If you chose to offset the first end condition from another face or
plane, then TRUE specifies offset in direction away from the sketch and
FALSE specifies offset from the face or plane in a direction toward the
sketch |
| Input: | (BOOL) offsetReverse2 | If you chose to offset the second end condition from another face or
plane, then TRUE specifies offset in direction away from the sketch and
FALSE specifies offset from the face or plane in a direction toward the
sketch. |
| Input: | (double) thk1 | Wall thickness 1 (Mid-Plane type uses (thk1 ) /2
for each direction) |
| Input: | (double) thk2 | Wall thickness 2 (only used when thinType = 3) |
| Input: | (double) capThk | End cap thickness (only used when capEnds = 1) |
| Input: | (long) thinType | Thin feature type: 0
= One Direction 1
= One Direction Reverse 2
= Mid-Plane 3
= Two Direction |
| Input: | (long) capEnds | Cap the ends: 0 = no cap, 1 = cap (base features only) |
| Input: | (Boolean)addFillets | TRUE to add auto fillets (open profile base features only) |
| Input: | (double) filletRad | Fillet radii if addFillets =
TRUE |

Syntax (COM)

status = ModelDoc->FeatureBossThin
( sd, flip, dir, t1, t2, d1, d2, dchk1, dchk2, ddir1, ddir2, dang1, dang2,
offsetReverse1, offsetReverse2, thk1, thk2, capThk, thinType, capEnds,
addFillets, filletRad )

(Table)=========================================================

| Input: | (VARIANT_BOOL) sd | TRUE for single ended, FALSE for double ended |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) sd | Not used |
| Input: | (VARIANT_BOOL) flip | Flip side to cut; TRUE if you want to remove the material outside of
the profile |
| Input: | (long) t1 | Termination type for first end |
| Input: | (long) t2 | Termination type for second end |
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
| Input: | (VARIANT_BOOL) offsetReverse1 | If you chose to offset the first end condition from another face or
plane, then TRUE specifies offset in direction away from the sketch and
FALSE would specify offset from the face or plane in a direction toward
the sketch. |
| Input: | (VARIANT_BOOL) offsetReverse2 | if you chose to offset the second end condition from another face or
plane, then TRUE specifies offset in direction away from the sketch and
FALSE specifies offset from the face or plane in a direction toward the
sketch. |
| Input: | (double) thk1 | Wall thickness 1 (Mid-Plane type uses (thk1 ) /2
for each direction) |
| Input: | (double) thk2 | Wall thickness 2 (only used when thinType = 3) |
| Input: | (double) capThk | End cap thickness (only used when capEnds = 1) |
| Input: | (long) thinType | Thin feature type: 0
= One Direction 1
= One Direction Reverse 2
= Mid-Plane 3
= Two Direction |
| Input: | (long) capEnds | Cap the ends: 0 = no cap, 1 = cap (base features only) |
| Input: | (Boolean)addFillets | TRUE to add auto fillets (open profile base features only) |
| Input: | (double) filletRad | Fillet radii if addFillets =
TRUE |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Termination type can be any of the values as defined in swEndConditions_e.

The default direction for cut operations are opposite the sketch normal.
The default direction for boss operations is along the sketch normal.
Setting ddir1 and ddir2 arguments to TRUE reverses the default direction.
For double-ended extrusions, Direction2kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}is
always opposite to Direction1.

The default sketch normal is the same as the face or plane normal where
the sketch was placed. To determine this normal vector, use Face2::Normal
and RefPlane::GetRefPlaneParams, respectively.

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
<param name="Items" value="ModelDoc_Object$$**$$ZModifyBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__FeatureBossThin.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
