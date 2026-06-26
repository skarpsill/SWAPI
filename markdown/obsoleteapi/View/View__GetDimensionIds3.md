---
title: "View::GetDimensionIds3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDimensionIds3.htm"
---

# View::GetDimensionIds3

This method is obsolete and has been superseded
by[View::GetDimensionIds4](sldworksAPI.chm::/View/View__GetDimensionIds4.htm).

Description

This method returns a list of dimension names from the current drawing
view.

Syntax (OLE Automation)

retval = View.GetDimensionIds3 ()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray of strings; each string represents one dimension
name from the current drawing view |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDimensionIds3
( &retval )

(Table)=========================================================

| Output: | (BSTR) retval | Array of strings; each string represents one dimension name from the
current drawing view |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The order of the dimension names returned align with the order of information
returned from View::GetDimensionInfo5. This alignment of information is
valid as long as the calls to this method and View::GetDimensionInfo5
are made consecutively.

One string is returned for each dimension in the view. See View::GetDimensionCount3
to determine the number of dimensions in the view.

This method is identical to the now obsolete View::GetDimensionIds2
except View::GetDimensionIds2 did not output dangling dimensions. This
method does.

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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2000$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\View\View__GetDimensionIds3.htm" >
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
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="View_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\View\View__GetDimensionIds3.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
