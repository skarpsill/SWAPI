---
title: "View::GetDimensionString"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDimensionString.htm"
---

# View::GetDimensionString

This
method is obsolete and has been superseded by[View::GetDimensionString2](View__GetDimensionString2.htm).

Description

This method returns an array of strings containing the text associated
with each dimension in the view. See View::GetDimensionCount to determine
the number of strings to be returned.

Syntax (OLE Automation)

retval = View.GetDimensionString ()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray containing the text associated with each dimension |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDimensionString
( retval )

(Table)=========================================================

| Output: | (BSTR*) retval | Text associated with each dimension |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="View_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\sw2003\View\View__GetDimensionString.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
