---
title: "Gtol::GetTextFormat"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Gtol/Gtol__GetTextFormat.htm"
---

# Gtol::GetTextFormat

This method is obsolete and has been superseded
by[Annotation::GetTextFormat](sldworksAPI.chm::/Annotation/Annotation__GetTextFormat.htm).

Description

This method gets the TextFormat object for the Gtol.

Syntax (OLE Automation)

retval
= Gtol.GetTextFormat ( )

(Table)=========================================================

| Return: | (LPDISPATCH)
retval | Dispatch
object for the TextFormat object |
| --- | --- | --- |

Syntax (COM)

status = Gtol->IGetTextFormat (
&retval )

(Table)=========================================================

| Output: | (LPTEXTFORMAT) retval | Pointer to the TextFormat object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if Successful |

Remarks

This method returns the text formatting object for the Gtol. To modify
the formatting, change the properties, then call Gtol::SetTextFormat.

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
<param name="Items" value="Gtol_Object$$**$$ZGetTextFormat$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\Gtol\Gtol__GetTextFormat.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
