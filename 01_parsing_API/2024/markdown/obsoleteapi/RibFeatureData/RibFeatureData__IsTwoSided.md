---
title: "RibFeatureData::IsTwoSided"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/RibFeatureData/RibFeatureData__IsTwoSided.htm"
---

# RibFeatureData::IsTwoSided

This
property is obsolete and has been superseded by RibFeatureData2::IsTwoSided .

Description

This property controls whether the rib is created on two sides of the
Mid Plane, or in a single direction (see RibFeatureData::ReverseThicknessDir).

Syntax (OLE Automation)

IsTwoSided= RibFeatureData.IsTwoSided (VB
Get property)

RibFeatureData.IsTwoSided= IsTwoSided (VB
Set property)

IsTwoSided= RibFeatureData.GetIsTwoSided
( ) (C++ Get property)

RibFeatureData.SetIsTwoSided ( IsTwoSided) (C++
Set property)

(Table)=========================================================

| Property: | (BOOL) IsTwoSided | TRUE if the rib is extruded either side of the midplane, FALSE if it
is single sided |
| --- | --- | --- |

Syntax (COM)

status = RibFeatureData-> get_IsTwoSided(
&IsTwoSided)

status = RibFeatureData-> put_IsTwoSided(
IsTwoSided)

(Table)=========================================================

| Property: | (VARIANT_BOOL) IsTwoSided | TRUE if the rib is extruded either side of the midplane, FALSE if it
is single sided |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Changing the value of this property does not affect geometry until Feature::ModifyDefinition
is called.

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
<param name="Items" value="ZFeatureDefinition$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\RibFeatureData\RibFeatureData__IsTwoSided.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
