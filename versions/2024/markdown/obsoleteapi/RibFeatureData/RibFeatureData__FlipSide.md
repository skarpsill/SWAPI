---
title: "RibFeatureData::FlipSide"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/RibFeatureData/RibFeatureData__FlipSide.htm"
---

# RibFeatureData::FlipSide

This
property is obsolete and has been superseded by RibFeatureData2::FlipSide .

Description

This property controls whether the material is added to the reverse
side.

Syntax (OLE Automation)

FlipSide= RibFeatureData.FlipSide (VB
Get property)

RibFeatureData.FlipSide= FlipSide (VB
Set property)

FlipSide= RibFeatureData.GetFlipSide
( ) (C++ Get property)

RibFeatureData.SetFlipSide ( FlipSide) (C++
Set property)

(Table)=========================================================

| Property: | (BOOL) FlipSide | TRUE if the material is added to the reverse side |
| --- | --- | --- |

Syntax (COM)

status = RibFeatureData-> get_FlipSide(
&FlipSide)

status = RibFeatureData-> put_FlipSide(
FlipSide)

(Table)=========================================================

| Property: | (VARIANT_BOOL) FlipSide | TRUE if the material is added to the reverse side |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\RibFeatureData\RibFeatureData__FlipSide.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
