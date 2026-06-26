---
title: "DisplayDimension::SetTextFormat"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/DisplayDimension__SetTextFormat.htm"
---

# DisplayDimension::SetTextFormat

This method is obsolete and has been superseded
by[Annotation::SetTextFormat](sldworksAPI.chm::/Annotation/Annotation__SetTextFormat.htm).

Description

This
method sets the text format parameters for this display dimension.

Syntax (OLE Automation)

retval
= DisplayDimension.SetTextFormat ( textFormatType, textFormat )

(Table)=========================================================

| Input: | (long)
textFormatType | Determines
whether the dimension uses the document text format or the textFormat argument values |
| --- | --- | --- |
| Input: | (LPDISPATCH)
textFormat | Formatting
values |
| Return: | (BOOL)
retval | TRUE
if successfully set, FALSE if not |

Syntax (COM)

status
= DisplayDimension->ISetTextFormat ( textFormatType, textFormat, &retval
)

(Table)=========================================================

| Input: | (long)
textFormatType | Determines
whether the dimension uses the document text format or the textFormat argument values |
| --- | --- | --- |
| Input: | (LPTEXTFORMAT)
textFormat | Formatting
values |
| Output: | (VARIANT_BOOL)
retval | TRUE if successfully set, FALSE if not |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

This method sets the text formatting for the dimension to the document
text formatting if useDocFormat is 1, or the formatting specified in thetextFormatargument if useDocFormat
is 0.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\DisplayDimension\DisplayDimension__SetTextFormat.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
