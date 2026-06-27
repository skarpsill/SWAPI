---
title: "ModelDoc::InsertHelix"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertHelix.htm"
---

# ModelDoc::InsertHelix

This
method is obsolete and has been superseded by[ModelDoc2::InsertHelix](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertHelix.htm).

Description

This method creates a helix.

Syntax (OLE Automation)

void ModelDoc.InsertHelix
( reversed, clockwised, tapered, outward, helixdef, height, pitch, revolution,
taperangle, startangle)

(Table)=========================================================

| Input: | (BOOL) reversed | TRUE will create helix in opposite direction of the circle used to define
the helix diameter, FALSE will create the helix in direction of the circle's
normal vector; the normal vector of a circle, for example, would be out
of the screen if the circle were drawn in a CCW direction |
| --- | --- | --- |
| Input: | (BOOL) clockwised | TRUE for clockwise, FALSE for counter-clockwise |
| Input: | (BOOL) tapered | TRUE to taper the helix, FALSE for no taper |
| Input: | (BOOL) outward | TRUE to taper the helix outward, FALSE for inward |
| Input: | (long) helixdef | Helix definition; based on this value, fill in appropriate arguments: 0
= (pitch and rev) 1
= (height and rev) 2
= (height and pitch) 3
= (Spiral) |
| Input: | (double) height | Height of helix in meters |
| Input: | (double) pitch | Helix pitch |
| Input: | (double) revolution | Number of revolutions |
| Input: | (double) taperangle | Taper angle |
| Input: | (double) startangle | Start angle rotation from base axis in radians |

Syntax (COM)

status = ModelDoc->InsertHelix
( reversed, clockwised, tapered, outward, helixdef, height, pitch, revolution,
taperangle, startangle )

(Table)=========================================================

| Input: | (VARIANT_BOOL) reversed | TRUE will create helix in opposite direction of the circle used to define
the helix diameter, FALSE will create the helix in direction of the circle's
normal vector; the normal vector of a circle, for example, would be out
of the screen if the circle were drawn in a CCW direction |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) clockwised | TRUE for clockwise, FALSE for counter-clockwise |
| Input: | (VARIANT_BOOL) tapered | TRUE to taper the helix, FALSE for no taper |
| Input: | (VARIANT_BOOL) outward | TRUE to taper the helix outward, FALSE for inward |
| Input: | (long) helixdef | Helix definition; based on this value, fill in appropriate arguments: 0
= (pitch and rev) 1
= (height and rev) 2
= (height and pitch) 3
= (Spiral) |
| Input: | (double) height | Hheight of helix in meters |
| Input: | (double) pitch | Helix pitch |
| Input: | (double) revolution | Number of revolutions |
| Input: | (double) taperangle | Taper angle |
| Input: | (double) startangle | Start angle rotation from base axis in radians |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

When creating a helix defined as spiral, you need to specify the helix
pitch and number of revolutions using the appropriate arguments.

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
<param name="Items" value="ModelDoc_Object$$**$$ZInsertFeature$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__InsertHelix.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
