---
title: "Face::GetBox"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetBox.htm"
---

# Face::GetBox

This
method is obsolete and has been superseded by[Face2::GetBox](sldworksAPI.chm::/Face2/Face2__GetBox.htm).

Description

This method gets the box boundaries for this face.

Syntax (OLE Automation)

retval
= Face.GetBox ()

(Table)=========================================================

| Return: | (VARIANT)
retval | VARIANT
SafeArray of 6 doubles containing the two diagonal points that bound the
component |
| --- | --- | --- |

Syntax (COM)

status
= Face->IGetBox ( retval )

(Table)=========================================================

| Output: | (double*)
retval | Two
diagonal points which bound the component in the form of a pointer to
an array of 6 doubles |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

The X,Y,Z points returned are the lower and upper diagonal corners that
bound the face with the box sides parallel to the X, Y and Z axes. The
box dimensions returned enclose the face and are typically close to the
minimum possible size, but not always.

The return value is an array of doubles as follows:

[ XCorner1, YCorner1, ZCorner1, XCorner2,
YCorner2, ZCorner2 ]

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
<param name="Items" value="Face_Object$$**$$ZGetInfoBox$$**$$ZGetInfoFace$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Face\Face__GetBox.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
