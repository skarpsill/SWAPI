---
title: "Body::GetExtremePoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__GetExtremePoint.htm"
---

# Body::GetExtremePoint

This
method is obsolete and has been superseded by[Body2::GetExtremePoint](sldworksAPI.chm::/Body2/Body2__GetExtremePoint.htm).

Description

This method calculates the extreme point of the model in the given direction.

Syntax
(OLE Automation)

retval
= Body.GetExtremePoint ( x, y, z, &outx, &outy, &outz )

(Table)=========================================================

| Input: | (double)
x | X
component of the direction vector |
| --- | --- | --- |
| Input: | (double)
y | Y
component of the direction vector |
| Input: | (double)
z | Z
component of the direction vector |
| Output: | (double)
outx | Extreme
point X coordinate |
| Output: | (double)
outy | Extreme
point Y coordinate |
| Output: | (double)
outz | Extreme
point Z coordinate |
| Return: | (BOOL)
retval | TRUE
if a point was found, FALSE if it was not |

Syntax
(COM)

status
= Body->GetExtremePoint ( x, y, z, &outx, &outy, &outz,
&found )

(Table)=========================================================

| Input: | (double)
x | X
component of the direction vector |
| --- | --- | --- |
| Input: | (double)
y | Y
component of the direction vector |
| Input: | (double)
z | Z
component of the direction vector |
| Output: | (double)
outx | Extreme
point X coordinate |
| Output: | (double)
outy | Extreme
point Y coordinate |
| Output: | (double)
outz | Extreme
point Z coordinate |
| Output: | (VARIANT_BOOL)
found | TRUE
if a point was found, FALSE if it was not |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

This
method returns the furthest possible intersection point between a plane
normal to the specified direction vector and the model, as the plane moves
along the direction vector.

For
example, if the model is a right cube centered on the origin and the direction
vector is (1.0, 1.0, 1.0), then the extreme point is the vertex at (1.0,
1.0, 1.0).

If
there is more than one point (for example, if there is a face perpendicular
to the direction vector), then SolidWorks returns a unique point found
in a deterministic way.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Body_Object$$**$$ZGetInfoBox$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\sw2003\Body\Body__GetExtremePoint.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
