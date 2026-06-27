---
title: "Face::IsSame"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__IsSame.htm"
---

# Face::IsSame

This
method is obsolete and has been superseded by[Face2::IsSame](sldworksAPI.chm::/Face2/Face2__IsSame.htm).

Description

This method returns TRUE if the two faces are the same.

Syntax (OLE Automation)

retval
= Face.IsSame ( faceIn)

(Table)=========================================================

| Input: | (LPDISPATCH)
faceIn | Dispatch
pointer to the face object to be compared |
| --- | --- | --- |
| Return: | (BOOL)
retval | TRUE
if the two faces are the same, FALSE if they are different |

Syntax (COM)

status = Face->IIsSame ( faceIn,
&retval )

(Table)=========================================================

| Input: | (LPFACE) faceIn | Pointer to face to be compared |
| --- | --- | --- |
| Output: | (VARIANT_BOOL*) retval | TRUE if the two faces are the same, FALSE if they are different |
| Return: | (HRESULT)status | S_OK if successful |

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
<param name="Items" value="Face_Object$$**$$ZGetInfoFace$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Face\Face__IsSame.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
