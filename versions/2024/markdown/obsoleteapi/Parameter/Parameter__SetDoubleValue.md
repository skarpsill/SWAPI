---
title: "Parameter::SetDoubleValue"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Parameter/Parameter__SetDoubleValue.htm"
---

# Parameter::SetDoubleValue

This method is obsolete and has been superseded by[Parameter::SetDoubleValue2](sldworksAPI.chm::/Parameter/Parameter__SetDoubleValue2.htm).

Description

This method sets the value of an attribute parameter. This method works
with values of types double and integer and is in system units. Integer
values cannot be negative.

Syntax (OLE Automation)

retval = Parameter.SetDoubleValue (
value)

(Table)=========================================================

| Input: | (double) value | Value to store in the attribute |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if successful, FALSE if not |

Syntax (COM)

status = Parameter->SetDoubleValue
( value, &retval )

(Table)=========================================================

| Input: | (double) value | Value to store in the attribute |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If you need to store a negative value, define the attribute parameter
as type double. Negative integer values are not allowed.

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
<param name="Items" value="Parameter_Object$$**$$ZGetInfoParameter$$**$$ZModifyParameter$$**$$ZGetParameter$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Parameter\Parameter__SetDoubleValue.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Find_Attribute_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Parameter\Parameter__SetDoubleValue.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
