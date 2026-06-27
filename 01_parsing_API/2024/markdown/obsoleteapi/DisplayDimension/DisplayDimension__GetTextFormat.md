---
title: "DisplayDimension::GetTextFormat"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/DisplayDimension__GetTextFormat.htm"
---

# DisplayDimension::GetTextFormat

This method is obsolete and has been superseded
by[Annotation::GetTextFormat](sldworksAPI.chm::/Annotation/Annotation__GetTextFormat.htm).

Description

This method gets the TextFormat object for this display dimension.

Syntax (OLE Automation)

retval
= DisplayDimension.GetTextFormat ( )

(Table)=========================================================

| Return: | (LPDISPATCH)
retval | Dispatch
object for the TextFormat object |
| --- | --- | --- |

Syntax (COM)

status
= DisplayDimension->IGetTextFormat ( &retval )

(Table)=========================================================

| Output: | (LPTEXTFORMAT)
retval | Pointer
to the TextFormat object |
| --- | --- | --- |
| Return: | (HRESULT)
status | S_OK
if Successful |

Remarks

To modify the formatting, change the properties and call DisplayDimension::SetTextFormat
to implement your changes.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="DisplayDimension_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\DisplayDimension\DisplayDimension__GetTextFormat.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
