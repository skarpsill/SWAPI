---
title: "DisplayDimension::GetUseDocPrecision"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/DisplayDimension__GetUseDocPrecision.htm"
---

# DisplayDimension::GetUseDocPrecision

This method is obsolete and was not been superceded.

Description

This method determines if this display dimension
uses the document default setting for the displayed precision of the dimension
and tolerance values.

Syntax (OLE Automation)

retval = DisplayDimension.GetUseDocPrecision ( )

(Table)=========================================================

| Return: | (BOOL) retval | TRUE if this display dimension uses the document
setting, FALSE if it uses the local setting |
| --- | --- | --- |

Syntax (COM)

status = DisplayDimension->GetUseDocPrecision
( &retval )

(Table)=========================================================

| Output: | (VARIANT_BOOL) retval | TRUE if this display dimension uses the document
setting, FALSE if it uses the local setting |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The displayed precision of a dimension and its
tolerance values can be controlled by a value in one of two places: on
the owning document or on the individual display dimension. This method
determines whether this display dimension uses the document default setting
for precision.

Use[DisplayDimension::SetPrecision](DisplayDimension__SetPrecision.htm)to set this value.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\DisplayDimension\DisplayDimension__GetUseDocPrecision.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
