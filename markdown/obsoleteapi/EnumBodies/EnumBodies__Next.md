---
title: "EnumBodies::Next"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/EnumBodies/EnumBodies__Next.htm"
---

# EnumBodies::Next

This method is obsolete and has been superseded by[EnumBodies2::Next](sldworksAPI.chm::/EnumBodies2/EnumBodies2__Next.htm).

Description

This method gets the next body.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = EnumBodies->Next ( celt,
&rgelt, pceltFetched )

(Table)=========================================================

| Input: | (long) celt | Number bodies desired for the enumerated list |
| --- | --- | --- |
| Output: | (LPBODY) rgelt | Pointer to the enumerated list of bodies |
| Output: | (long*) pceltFetched | Pointer to the number of bodies returned from the list; this value could
be less than celt if you asked for more bodies than exist, or it could
be NULL if no more bodies exist |
| Return: | (HRESULT) status | S_OK if successful |

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
<param name="Items" value="EnumBodies_Object$$**$$ZGetBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\sw2003\EnumBodies\EnumBodies__Next.htm" >
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
<param name="_CURRENTFILEPATH" value="D:\sw2003\EnumBodies\EnumBodies__Next.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
