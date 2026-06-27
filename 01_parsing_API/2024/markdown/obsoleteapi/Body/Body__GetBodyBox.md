---
title: "Body::GetBodyBox"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__GetBodyBox.htm"
---

# Body::GetBodyBox

This method is obsolete and has been superseded by[Body2::GetBodyBox](sldworksAPI.chm::/Body2/Body2__GetBodyBox.htm).

Description

This method gets the bounding body box.

Syntax (OLE Automation)

retval = Body.GetBodyBox ( )

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray of 6 doubles representing the extents of the
bounding box |
| --- | --- | --- |

Syntax (COM)

status = Body->IGetBodyBox ( BoxCorners )

(Table)=========================================================

| Input: | (double*) BoxCorners | Pointer to an array of 6 doubles representing the extents of the bounding
box |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The X,Y,Z points returned are the lower and upper
diagonal corners that bound the body with the box sides parallel to the
X, Y and Z axes. The box dimensions returned enclose the body and are
typically close to the minimum possible size, but not always.

The return value is an array of doubles:

[XCorner1, YCorner1, ZCorner1, XCorner2,
YCorner2, ZCorner2]

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
<param name="Items" value="Body_Object$$**$$ZGetInfoBox$$**$$ZGetInfoBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\sw2003old\Body\Body__GetBodyBox.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
