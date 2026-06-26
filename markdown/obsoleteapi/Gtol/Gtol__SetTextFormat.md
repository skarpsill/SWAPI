---
title: "Gtol::SetTextFormat"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Gtol/Gtol__SetTextFormat.htm"
---

# Gtol::SetTextFormat

This method is obsolete and has been superseded
by[Annotation::SetTextFormat](sldworksAPI.chm::/Annotation/Annotation__SetTextFormat.htm).

Description

This
method sets the text format parameters.

Syntax (OLE Automation)

retval
= Gtol.SetTextFormat ( useDocFormat, textFormat )

(Table)=========================================================

| Input: | (long)
useDocFormat | Controls
whether the Gtol uses the document text format or the textFormat argument
values |
| --- | --- | --- |
| Input: | (LPDISPATCH)
textFormat | Formatting
values |
| Return: | (BOOL)
retval | TRUE
if successfully set, FALSE if not |

Syntax (COM)

status
= Gtol->ISetTextFormat ( useDocFormat, textFormat, &retval )

(Table)=========================================================

| Input: | (long)useDocFormat | Controls
whether the Gtol uses the document text format or the textFormat argument
values |
| --- | --- | --- |
| Input: | (LPTEXTFORMAT)textFormat | Formatting
values |
| Output: | (VARIANT_BOOL)retval | TRUE if successfully set, FALSE if not |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

This method sets the text formatting for this Gtol to the document text
formatting if useDocFormat is 1, or to the formatting specified in the
textFormat argument if useDocFormat is 0.

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
<param name="Items" value="Gtol_Object$$**$$ZGetTextFormat$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\Gtol\Gtol__SetTextFormat.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
