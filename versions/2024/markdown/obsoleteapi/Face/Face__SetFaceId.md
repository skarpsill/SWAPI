---
title: "Face::SetFaceId"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__SetFaceId.htm"
---

# Face::SetFaceId

This
method is obsolete and has been superseded by[Face2::SetFaceId](sldworksAPI.chm::/Face2/Face2__SetFaceId.htm).

Description

This method sets the face ID on an imported body.

Syntax (OLE Automation)

(void)
Face.SetFaceId (int idIn)

(Table)=========================================================

| Input: | (int)
idIn | Face ID |
| --- | --- | --- |

Syntax (COM)

status
= Face-> SetFaceId ( idIn)

(Table)=========================================================

| Input: | (int)
idIn | Face ID |
| --- | --- | --- |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

SolidWorks uses this ID to track the specific faces
of imported bodies (for example, IGES imports).

The face ID is a persistent and is saved with the
document. The face ID can be changed by any third party application. The
intent is that you assign an ID to a particular face so that you can refer
to that face within your application. Each ID must be unique, so it is
best to let SolidWorks assign IDs for you when an imported body or surface
is created.

To store data
with a face, use the Attribute object.

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
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Face\Face__SetFaceId.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
