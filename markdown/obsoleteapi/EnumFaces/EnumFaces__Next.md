---
title: "EnumFaces::Next"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/EnumFaces/EnumFaces__Next.htm"
---

# EnumFaces::Next

This method is obsolete and has been superseded by[EnumFaces2::Next](sldworksAPI.chm::/EnumFaces2/EnumFaces2__Next.htm).

Description

This method gets the next face.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = EnumFaces->Next ( celt,
rgelt, &pceltFetched )

(Table)=========================================================

| Input: | (long) celt | Number of faces desired for the enumerated list |
| --- | --- | --- |
| Output: | (LPFACE)* rgelt | Pointer to the list of face |
| Output: | (long) pceltFetched | Pointer to the number of faces returned from the list; this value can
be less than celt if you ask for more faces than exist, or it can be NULL
if no more faces exist |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="Items" value="EnumFaces_Object$$**$$ZGetFace$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\EnumFaces\EnumFaces__Next.htm" >
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
<param name="Items" value="Enumerate_Bodies_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\EnumFaces\EnumFaces__Next.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
