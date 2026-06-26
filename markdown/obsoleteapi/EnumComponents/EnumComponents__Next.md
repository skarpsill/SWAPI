---
title: "EnumComponents::Next"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/EnumComponents/EnumComponents__Next.htm"
---

# EnumComponents::Next

This
method is obsolete and has been superseded by[EnumComponents2::Next](sldworksAPI.chm::/EnumComponents2/EnumComponents2__Next.htm).

Description

This method gets the next component.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = EnumComponents->Next ( celt, rgelt, &pceltFetched
)

(Table)=========================================================

| Input: | (long) celt | Number of component objects desired for the enumerated
list |
| --- | --- | --- |
| Output: | (LPCOMPONENT)* rgelt | Pointer to an array of size celt of component
objects |
| Output: | (long) pceltFetched | Pointer to the number of component objects returned
from the list; this value can be less than celt if you ask for more component
objects than exist, or it can be NULL if no more component objects exist |
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
<param name="Items" value="ZViewEnumerations$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\sw2003\EnumComponents\EnumComponents__Next.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
