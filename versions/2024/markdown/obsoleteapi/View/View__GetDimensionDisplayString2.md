---
title: "View::GetDimensionDisplayString2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDimensionDisplayString2.htm"
---

# View::GetDimensionDisplayString2

This method is obsolete and has been superseded
by[View::GetDimensionDisplayString3](View__GetDimensionDisplayString3.htm).

Description

This method gets all of the dimension strings in the current drawing
view.

Syntax (OLE Automation)

retval = View.GetDimensionDisplayString2
()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray of strings containing the dimension text |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDimensionDisplayString2
( retval )

(Table)=========================================================

| Output: | (BSTR*) retval | Array of strings containing the dimension text |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

For each dimension in the drawing view, this method returns return 10
strings. If any of the dimension strings are not used, then those strings
are returned as NULL strings.

[value1, tolMax1 tolMin1, value2, tolMax2,
tolMin2, prefix, suffix, callout1, callout2]

This set of data is returned for each dimension in the view. See View::GetDimensionCount2
to determine the number of dimensions in the view.

This method is identical to View::GetDimensionDisplayString except when
a base ordinate is not visible, then the subordinates were not output,
regardless of whether they were visible or not. With this method, the
output of each subordinate, if it is visible, occurs regardless of whether
or not its base ordinate is visible.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\View\View__GetDimensionDisplayString2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
