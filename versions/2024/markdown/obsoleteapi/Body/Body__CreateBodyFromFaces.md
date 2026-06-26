---
title: "Body::CreateBodyFromFaces"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__CreateBodyFromFaces.htm"
---

# Body::CreateBodyFromFaces

This method is obsolete and has been superseded by[Body2::CreateBodyFromFaces](sldworksAPI.chm::/Body2/Body2__CreateBodyFromFaces.htm).

Description

This method creates a temporary body object from the given faces.

Syntax (OLE Automation)

retval
= Body.CreateBodyFromFaces ( NumOfFaces, FaceList)

(Table)=========================================================

| Input: | (long)
NumOfFaces | Number
of faces to use for body creation |
| --- | --- | --- |
| Input: | (VARIANT)
FaceList | VARIANT
containing the faces to use for body creation |
| Return: | (LPDISPATCH)
retval | Pointer
to dispatch object, the body |

Syntax (COM)

status
= Body->ICreateBodyFromFaces ( NumOfFaces, FaceList, &retval )

(Table)=========================================================

| Input: | (long)
NumOfFaces | Number
of faces to use for body creation |
| --- | --- | --- |
| Input: | (VARIANT)
FaceList | VARIANT
containing the faces to use for body creation |
| Output: | (LPBODY)
retval | Pointer
to the body |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

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
<param name="Items" value="Body_Object$$**$$ZAccessorByCreate$$**$$ZCreateTemporaryBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Body\Body__CreateBodyFromFaces.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
