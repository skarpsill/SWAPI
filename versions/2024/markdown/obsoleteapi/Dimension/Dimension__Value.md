---
title: "Dimension::Value"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Dimension/Dimension__Value.htm"
---

# Dimension::Value

This
property is obsolete and has been superseded by[Dimension::GetValue2](Dimension__GetValue2.htm)and[Dimension::SetValue2](Dimension__SetValue2.htm).

Description

This property gets or sets the value of the current dimension. The value
returned is in user units, which are taken from the document where the
dimension was created.

Syntax (OLE Automation)

Value
= Dimension.Value (VB Get property)

Dimension.Value
= Value (VB Set property)

Value
= Dimension.GetValue ( ) (C++ Get property)

Dimension.SetValue
( Value ) (C++ Set property)

(Table)=========================================================

| Property: | (double)
Value | Value
of the dimension |
| --- | --- | --- |

Syntax (COM)

status
= Dimension->get_Value( &value )

status
= Dimension->put_Value( Value )

(Table)=========================================================

| Property: | (double)
Value | Value
of the dimension |
| --- | --- | --- |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

This property always returns a dimension value created in a part in
terms of the units of the original part. If the part is in millimeters,
then this property always returns the dimension value in millimeters.
If that part is brought into a drawing that is in inches and that model
dimension is inserted into one of the drawing views, then this property
returns the dimension value in millimeters. If the original part is changed
to inches, then this property returns the dimension value in inches.

This property allows you to change the value
of a read-only dimension. Use Dimension::ReadOnly to determine if a dimension
is read-only.Metadata type="DesignerControl" startspan
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
<param name="Items" value="Dimension_Object$$**$$ZGetDimension$$**$$ZModifyDimension$$**$$ZGetInfoDimension$$**$$ModelDoc::GetUnits$$**$$ZGetParameter$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\Dimension\Dimension__Value.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
