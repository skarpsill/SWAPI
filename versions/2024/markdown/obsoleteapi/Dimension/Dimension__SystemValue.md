---
title: "Dimension::SystemValue"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Dimension/Dimension__SystemValue.htm"
---

# Dimension::SystemValue

This
property is obsolete and has been superseded by[Dimension:GetSystemValue2](Dimension__GetSystemValue2.htm)and[Dimension::SetSystemValue2](Dimension__SetSystemValue2.htm).

Description

This property gets or sets the system value of the current dimension
in meters.

Syntax (OLE Automation)

Value
= Dimension.SystemValue (VB Get property)

Dimension.SystemValue = Value (VB Set
property)

Value
= Dimension.GetSystemValue ( ) (C++ Get property)

Dimension.SetSystemValue ( Value ) (C++
Set property)

(Table)=========================================================

| Property: | (double)
Value | Value
of the dimension in meters |
| --- | --- | --- |

Syntax (COM)

status
= Dimension->get_SystemValue(&Value)

status = Dimension->put_SystemValue ( Value
)

(Table)=========================================================

| Property: | (double)
Value | Value
of the dimension in meters |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

This property allows you to change the value of a read-only dimension.
Use Dimension::ReadOnly to determine if a dimension is read-only.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Dimension_Object$$**$$ZGetInfoDimension$$**$$ZModifyDimension$$**$$ZGetDimension$$**$$ZGetParameter$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\Dimension\Dimension__SystemValue.htm" >
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Change_Dimension_Example$$**$$Traverse_Feature_Dimensions_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\Dimension\Dimension__SystemValue.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
