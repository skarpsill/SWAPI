---
title: "View::GetDimensionIds"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDimensionIds.htm"
---

# View::GetDimensionIds

This
method is obsolete and has been superseded by[View::GetDimensionIds2](View__GetDimensionIds2.htm).

Description

This method returns a list of dimension names from the current drawing
view.

Syntax (OLE Automation)

retval = View.GetDimensionIds ()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray of strings; each string in the array represents
one dimension name from the current drawing view |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDimensionIds
( &retval )

(Table)=========================================================

| Output: | (BSTR) retval | Array of strings; each string in the array represents one dimension
name from the current drawing view |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The order of the dimension names returned aligns with the order of information
returned from View::GetDimensionInfo. This alignment of information is
valid as long as the calls to this methodkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}and
View::GetDimensionInfo are made consecutively.

One string is returned for each dimension in the view. See View::GetDimensionCount
to determine the number of dimensions in the view.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\View\View__GetDimensionIds.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
