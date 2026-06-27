---
title: "Face::RemoveFaceID"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__RemoveFaceID.htm"
---

# Face::RemoveFaceID

This
method is obsolete and has been superseded by[Face2::RemoveFaceID](sldworksAPI.chm::/Face2/Face2__RemoveFaceID.htm).

Description

This method removes the face ID on an imported body.

Syntax (OLE Automation)

(void)
Face.RemoveFaceID (int idIn)

(Table)=========================================================

| Return: | (int)
idIn | Face
ID |
| --- | --- | --- |

Syntax (COM)

status = Face-> RemoveFaceID ( idIn)

(Table)=========================================================

| Output: | (int) idIn | Face ID |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use[Face::SetFaceID](Face__SetFaceId.htm)to set the face ID.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\Face\Face__RemoveFaceID.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
