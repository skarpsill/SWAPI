---
title: "Face::GetFaceId"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetFaceId.htm"
---

# Face::GetFaceId

This
method is obsolete and has been superseded by[Face2::GetFaceId](sldworksAPI.chm::/Face2/Face2__GetFaceId.htm).

Description

This method gets the face ID on an imported body.

Syntax (OLE Automation)

retval
= Face.GetFaceId ()

(Table)=========================================================

| Return: | (int)
retval | Face
ID |
| --- | --- | --- |

Syntax (COM)

status
= Face-> GetFaceId ( &retval)

(Table)=========================================================

| Output: | (int)
retval | Face
ID |
| --- | --- | --- |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

This face ID is used to track the specific
faces of imported bodies (for example, IGES imports).

The face ID is a persistent ID that is
not saved with the document. The face ID can be changed by any third party
application. The intent is that you will assign an ID value to a particular
face so that you can refer to that face within your application. Each
ID value must be unique so it's best to let SolidWorks assign the ID value
for you when an imported body or surfaces is created.

If you are interested
in storing data with a face, refer to the Attribute object.

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
<param name="Items" value="Face_Object$$**$$ZCreateTemporaryBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="D:\sjesse\sw2001Plus\Face\Face__GetFaceId.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
