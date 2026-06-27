---
title: "Face::GetClosestPointOn"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetClosestPointOn.htm"
---

# Face::GetClosestPointOn

This
method is obsolete and has been superseded by[Face2::GetClosestPointOn](sldworksAPI.chm::/Face2/Face2__IGetClosestPointOn.htm).

Description

This method uses the X,Y,Z input point and return the closest point
on the face.

Syntax (OLE Automation)

retval
= Face.GetClosestPointOn ( x, y, z)

(Table)=========================================================

| Input: | (double)
x | X
value of the input point |
| --- | --- | --- |
| Input: | (double)
y | Y
value of the input point |
| Input: | (double)
z | Z
value of the input point |
| Return: | (VARIANT)
retval | SafeArray
of five doubles representing the X, Y, Z point on the sace followed by
the U, V parameter on the face that is closest to the input point |

Syntax (COM)

status
= Face->IGetClosestPointOn ( x, y, z, retval )

(Table)=========================================================

| Input: | (double)
x | X
value of the input point |
| --- | --- | --- |
| Input: | (double)
y | Y
value of the input point |
| Input: | (double)
z | Z
value of the input point |
| Output: | (double*)
retval | Pointer
to an array of five doubles representing the X, Y, Z point on the face
followed by the U, V parameter on the face that is closest to the input
point |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

This method returns only one point, regardless of how many points achieve
the minimum distance.

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
<param name="Items" value="Face_Object$$**$$ZGetInfoPoint$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="D:\sjesse\sw2001Plus\Face\Face__GetClosestPointOn.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Get Closest Point Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="D:\sjesse\sw2001Plus\Face\Face__GetClosestPointOn.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
