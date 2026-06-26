---
title: "DisplayDimension::SetPrecision"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/DisplayDimension__SetPrecision.htm"
---

# DisplayDimension::SetPrecision

This method is obsolete and has been superseded
by[DisplayDimension::SetPrecison2](sldworksAPI.chm::/DisplayDimension/DisplayDimension__SetPrecision2.htm).

Description

This method sets the displayed precisions of
this display dimension and its tolerance values.

Syntax (OLE Automation)

retval = DisplayDimension.SetPrecision
( useDoc, primary, alternate, primaryTol, alternateTol)

(Table)=========================================================

| Input: | (BOOL) useDoc | TRUE uses the document settings, FALSE uses the
settings on this display dimension (see below) |
| --- | --- | --- |
| Input: | (long) primary | Number of decimal places displayed in the dimension
value |
| Input: | (long) alternate | Number of decimal places displayed in the dual
dimension value |
| Input: | (long) primaryTol | Number of decimal places displayed in the tolerance
value |
| Input: | (long) alternateTol | Number of decimal places displayed in the dual
tolerance value |
| Return: | (long) retval | Return status (see below) |

Syntax (COM)

status = DisplayDimension->SetPrecision
( useDoc, primary, alternate, primaryTol, alternateTol, &retval )

(Table)=========================================================

| Input: | (BOOL) useDoc | TRUE uses the document settings, FALSE uses the
settings on this display dimension (see below) |
| --- | --- | --- |
| Input: | (long) primary | Number of decimal places displayed in the dimension
value |
| Input: | (long) alternate | Number of decimal places displayed in the dual
dimension value |
| Input: | (long) primaryTol | Number of decimal places displayed in the tolerance
value |
| Input: | (long) alternateTol | Number of decimal places displayed in the dual
tolerance value |
| Output: | (long) retval | Return status (see below) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The displayed precision of a dimension and its
tolerance values can be controlled by a value is stored in one of two
places: on the owning document or on the individual display dimension.
TheuseDocargument allows you
to control whether to use the default document settings or the values
specified in theprimary,alternate,primaryTol,
andalternateTolarguments.

IfuseDocis TRUE, then SolidWorks ignores theprimary,alternate,primaryTol,
andalternateTolarguments.

The specified precision values must be in the range
between 0 and 8. This indicates to SolidWorks how many decimal places
to display. You can also set the precision to -1, which maintains the
current setting. SolidWorks considers any other values invalid. If a precision
is invalid, SolidWorks uses the current setting and continues processing
he other precision values.

retvalindicates the success or failure of this method. In general, a value less
than 0 indicates that the command failed and SolidWorks did not set any
precision values. A value of 0 indicates success. A value greater than
0 indicates that a problem occurred, but the command did not fail.

(Table)=========================================================

| -1 | Command failed, no precision values were set |
| --- | --- |
| 0 | Command was successful, all precision values were set |
| 1 | Primary precision argument was invalid |
| 2 | Alternate precision argument was invalid |
| 3 | Primary tolerance precision argument was invalid |
| 4 | Alternate tolerance precision argument was invalid |

When you use this method, use ModelDoc2::GraphicsRedraw2
to redraw the graphics window and see your changes.

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
<param name="Items" value="DisplayDimension_Object$$**$$ZModifyDisplayDimension$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\DisplayDimension\DisplayDimension__SetPrecision.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
