---
title: "ModelDoc::SimpleHole2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SimpleHole2.htm"
---

# ModelDoc::SimpleHole2

This method is obsolete
and has been superseded by[ModelDoc2::SimpleHole2](../ModelDoc2/ModelDoc2__SimpleHole2.htm).

Description

This method creates a simple hole.

Syntax (OLE Automation)

void ModelDoc.SimpleHole2
( dia, sd, flip, dir, t1, t2, d1, d2, dchk1, dchk2, ddir1, ddir2, dang1,
dang2, offsetReverse1, offsetReverse2)

(Table)=========================================================

| Input: | (double)dia | Hole diameter |
| --- | --- | --- |
| Input: | (BOOL) sd | TRUE for single-ended, FALSE for double-ended |
| Input: | (BOOL) flip | TRUE to flip the direction to cut |
| Input: | (BOOL) dir | TRUE to flip direction to extrude |
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
plane, then TRUE would specify offset in direction away from the sketch
and FALSE would specify offset from the face or plane in a direction toward
the sketch |
| Input: | (BOOL) offsetReverse2 | If you chose to offset the second end condition from another face or
plane, then TRUE would specify offset in direction away from the sketch
and FALSE would specify offset from the face or plane in a direction toward
the sketch |

Syntax (COM)

status = ModelDoc->SimpleHole2
( dia, sd, flip, dir, t1, t2, d1, d2, dchk1, dchk2, ddir1, ddir2, dang1,
dang2, offsetReverse1, offsetReverse2 )

(Table)=========================================================

| Input: | (double)dia | Hole diameter |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) sd | TRUE for single-ended, FALSE for double-ended |
| Input: | (VARIANT_BOOL) flip | TRUE to flip the direction to cut |
| Input: | (VARIANT_BOOL) dir | TRUE to flip direction to extrude |
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
plane, then TRUE would specify offset in direction away from the sketch
and FALSE would specify offset from the face or plane in a direction toward
the sketch |
| Input: | (VARIANT_BOOL) offsetReverse2 | If you chose to offset the second end condition from another face or
plane, then TRUE would specify offset in direction away from the sketch
and FALSE would specify offset from the face or plane in a direction toward
the sketch |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The t1 and t2 arguments can be any of the values in the swEndConditions_e
enumeration.

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
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SimpleHole2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
