---
title: "PartDoc::FeatureExtrusion3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__FeatureExtrusion3.htm"
---

# PartDoc::FeatureExtrusion3

This method is obsolete and has been superseded
by[FeatureManager::FeatureExtrusion](../FeatureManager/FeatureManager__FeatureExtrusion.htm).

Description

This method creates an extruded feature.

Syntax (OLE Automation)

void = PartDoc.FeatureExtrusion3 ( sd, flip, dir,
t1, t2, d1, d2, dchk1, dchk2, ddir1, ddir2, dang1, dang2, offsetReverse1,
offsetReverse2, translateSurface1, translateSurface2, merge )

(Table)=========================================================

| Input: | (VARIANT_BOOL) sd | TRUE for single-ended, FALSE for double-ended |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flip | TRUE to flip the direction to cut |
| Input: | (VARIANT_BOOL) dir | TRUE to flip direction to extrude |
| Input: | (long) t1 | Termination type for first end as defined in
swEndConditions_e |
| Input: | (long) t2 | Termination type for second end as defined in
swEndConditions_e |
| Input: | (double) d1 | Depth of extrusion for first end in meters |
| Input: | (double) d2 | Depth of extrusion for second end in meters |
| Input: | (VARIANT_BOOL) dchk1 | TRUE allows draft angle in first direction, FALSE
does not allow drafting |
| Input: | (VARIANT_BOOL) dchk2 | TRUE allows draft angle in second direction,
FALSE does not allow drafting |
| Input: | (VARIANT_BOOL) ddir1 | For first draft angle to be inward use TRUE,
for draft angle outward use FALSE |
| Input: | (VARIANT_BOOL) ddir2 | For second draft angle to be inward use TRUE,
for draft angle outward use FALSE |
| Input: | (double) dang1 | Draft angle for first end |
| Input: | (double) dang2 | Draft angle for second end |
| Input: | (VARIANT_BOOL) offsetReverse1 | If you chose to offset the first end condition
from another face or plane, then TRUE specifies offset in direction away
from the sketch, FALSE specifies offset from the face or plane in a direction
toward the sketch |
| Input: | (VARIANT_BOOL) offsetReverse2 | If you chose to offset the second end condition
from another face or plane, then TRUE specifies offset in direction away
from the sketch,FALSE specifies offset from the face or plane in a direction
toward the sketch |
| Input: | (VARIANT_BOOL) translateSurface1 | If you choose swEndcondOffsetFromSurface as the
termination type for the first end, then TRUE specifies that the end of
the extrusion is a translation of the reference surface, FALSE specifies
to use a true offset |
| Input: | (VARIANT_BOOL) translateSurface2 | If you choose swEndcondOffsetFromSurface as the
termination type for the second end, then TRUE specifies that the end
of the extrusion is a translation of the reference surface, FALSE specifies
to use a true offset |
| Input: | (VARIANT_BOOL) merge | TRUE to merge the feature, FALSE otherwise |

Syntax (COM)

status = PartDoc->FeatureExtrusion3 ( sd, flip,
dir, t1, t2, d1, d2, dchk1, dchk2, ddir1, ddir2, dang1, dang2, offsetReverse1,
offsetReverse2, translateSurface1, translateSurface2, merge )

Parameters Table Start

(Table)=========================================================

| Input: | (VARIANT_BOOL) sd | TRUE for single-ended, FALSE for double-ended |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flip | TRUE to flip the direction to cut |
| Input: | (VARIANT_BOOL) dir | TRUE to flip direction to extrude |
| Input: | (long) t1 | Termination type for first end as defined in
swEndConditions_e |
| Input: | (long) t2 | Termination type for second end as defined in
swEndConditions_e |
| Input: | (double) d1 | Depth of extrusion for first end in meters |
| Input: | (double) d2 | Depth of extrusion for second end in meters |
| Input: | (VARIANT_BOOL) dchk1 | TRUE allows draft angle in first direction, FALSE
does not allow drafting |
| Input: | (VARIANT_BOOL) dchk2 | TRUE allows draft angle in second direction,
FALSE does not allow drafting |
| Input: | (VARIANT_BOOL) ddir1 | For first draft angle to be inward use TRUE,
for draft angle outward use FALSE |
| Input: | (VARIANT_BOOL) ddir2 | For second draft angle to be inward use TRUE,
for draft angle outward use FALSE |
| Input: | (double) dang1 | Draft angle for first end |
| Input: | (double) dang2 | Draft angle for second end |
| Input: | (VARIANT_BOOL) offsetReverse1 | If you chose to offset the first end condition
from another face or plane than TRUE would specify offset in direction
away from the sketch and FALSE would specify offset from the face or plane
in a direction toward the sketch |
| Input: | (VARIANT_BOOL) offsetReverse2 | If you chose to offset the second end condition
from another face or plane, then TRUE specifies offset in direction away
from the sketch,FALSE specifies offset from the face or plane in a direction
toward the sketch |
| Input: | (VARIANT_BOOL) translateSurface1 | If you choose swEndcondOffsetFromSurface as the
termination type for the first end, then TRUE specifies that the end of
the extrusion is a translation of the reference surface, FALSE specifies
to use a true offset |
| Input: | (VARIANT_BOOL) translateSurface2 | If you choose swEndcondOffsetFromSurface as the
termination type for the second end, then TRUE specifies that the end
of the extrusion is a translation of the reference surface, FALSE specifies
to use a true offset |
| Input: | (VARIANT_BOOL) merge | TRUE to merge the feature, FALSE otherwise |
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\PartDoc\PartDoc__FeatureExtrusion3.htm" >
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
<param name="Items" value="PartDoc Method$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\PartDoc\PartDoc__FeatureExtrusion3.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
