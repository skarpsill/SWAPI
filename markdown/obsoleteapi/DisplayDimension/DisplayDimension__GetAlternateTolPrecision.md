---
title: "DisplayDimension::GetAlternateTolPrecision"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/DisplayDimension__GetAlternateTolPrecision.htm"
---

# DisplayDimension::GetAlternateTolPrecision

This method is obsolete and has been superseded
by[DisplayDimension::GetAlternateTolPrecision2](sldworksAPI.chm::/DisplayDimension/DisplayDimension__GetAlternateTolPrecision2.htm).

Description

This method gets the precision displayed for
the dual tolerance of this display dimension.

Syntax (OLE Automation)

retval = DisplayDimension.GetAlternateTolPrecision
( )

(Table)=========================================================

| Return: | (long) retval | Number of decimal places to be displayed (see below) |
| --- | --- | --- |

Syntax (COM)

status = DisplayDimension->GetAlternateTolPrecision
( &retval )

(Table)=========================================================

| Output: | (long) retval | Number of decimal places to be displayed (see
below) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method returns the precision used in the alternate
units of the dimension tolerance.

You can use[DisplayDimension::GetPrimaryPrecision](DisplayDimension__GetPrimaryPrecision.htm)to determine the primary dimension precision.

The displayed precision of a dimension and its
tolerance values are controlled by a value that SolidWorks stores in one
of two places; on the owning document or on the individual display dimension.
Use[DisplayDimension::GetUseDocPrecision](DisplayDimension__GetUseDocPrecision.htm)to determine whether this display dimension is using the default document
values.

This method gets the alternate precision value
stored on this display dimension. If this display dimension is set to
use the document settings for display dimension precision, then the value
returned by this method might be different than what is currently displayed
by SolidWorks.

Use[DisplayDimension::SetPrecision](DisplayDimension__SetPrecision.htm)to set precision values on this display dimension.

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
<param name="Items" value="DisplayDimension_Object$$**$$ZGetInfoDisplayDimension$$**$$ZGetInfoDimension$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\sjesse\sw2001Plus\DisplayDimension\DisplayDimension__GetAlternateTolPrecision.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
