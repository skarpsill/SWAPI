---
title: "Face::CreateSheetBodyByFaceExtension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__CreateSheetBodyByFaceExtension.htm"
---

# Face::CreateSheetBodyByFaceExtension

This
method is obsolete and has been superseded by[Face2::CreateSheetBodyByFaceExtension](sldworksAPI.chm::/Face2/Face2__CreateSheetBodyByFaceExtension.htm).

Description

This method creates a sheet body by extending the face.

Syntax (OLE Automation)

retval
= Face.CreateSheetBodyByFaceExtension ( boxLowIn, boxHighIn)

(Table)=========================================================

| Input: | (VARIANT)
boxLowIn | VARIANT
of type SafeArray of 3 doubles (x,y,z) |
| --- | --- | --- |
| Input: | (VARIANT)
boxHighIn | VARIANT
of type SafeArray of 3 doubles (x,y,z) |
| Return: | (LPDISPATCH)
retval | Dispatch
pointer to the newly created body |

Syntax (COM)

status = Face->ICreateSheetBodyByFaceExtension
( boxLowIn, boxHighIn, &retval )

(Table)=========================================================

| Input: | (double*) boxLowIn | Pointer to an array of 3 doubles (x,y,z) |
| --- | --- | --- |
| Input: | (double*) boxHighIn | Pointer to an array of 3 doubles (x,y,z) |
| Output: | (LPBODY) retval | Pointer to the newly created body |
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
<param name="Items" value="Face_Object$$**$$ZAccessorByCreate$$**$$ZCreateBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Face\Face__CreateSheetBodyByFaceExtension.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
