---
title: "View::GetDimensionDisplayString3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDimensionDisplayString3.htm"
---

# View::GetDimensionDisplayString3

This method is obsolete and has been superseded
by[View::GetDimensionDisplayString4](sldworksAPI.chm::/View/View__GetDimensionDisplayString4.htm).

Description

This method gets all of the dimension strings in the current drawing
view.

Syntax (OLE Automation)

retval = View.GetDimensionDisplayString3
()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray of strings containing the dimension text |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDimensionDisplayString3
( retval )

(Table)=========================================================

| Output: | (BSTR*) retval | Array of strings containing the dimension text |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

For each dimension in the drawing view, this method returns 10 strings.
If any of the dimension strings are not used, then those strings are returned
as NULL strings.

[value1, tolMax1 tolMin1, value2, tolMax2,
tolMin2, prefix, suffix, callout1, callout2]

This set of data is returned for each dimension in the view. See View::GetDimensionCount3
to determine the number of dimensions in the view.

This method is identical to the now obsolete View::GetDimensionDisplayString2
except a dangling dimension was not output by that method. This version
of this method outputs dangling dimensions.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2000$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\View\View__GetDimensionDisplayString3.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\View\View__GetDimensionDisplayString3.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
