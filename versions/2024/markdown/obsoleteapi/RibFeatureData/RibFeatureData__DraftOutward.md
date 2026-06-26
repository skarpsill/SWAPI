---
title: "RibFeatureData::DraftOutward"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/RibFeatureData/RibFeatureData__DraftOutward.htm"
---

# RibFeatureData::DraftOutward

This
property is obsolete and has been superseded by RibFeatureData2::DraftOutward .

Description

This property controls whether the rib has an associated draft. Additional
draft control can be done with RibFeatureData::DraftAngle and RibFeatureData::EnableDraft.

Syntax (OLE Automation)

DraftOutward= RibFeatureData.DraftOutward (VB
Get property)

RibFeatureData.DraftOutward= DraftOutward (VB
Set property)

DraftOutward= RibFeatureData.GetDraftOutward
( ) (C++ Get property)

RibFeatureData.SetDraftOutward ( DraftOutward) (C++
Set property)

(Table)=========================================================

| Property: | (BOOL) DraftOutward | TRUE if the draft is outward |
| --- | --- | --- |

Syntax (COM)

status = RibFeatureData-> get_DraftOutward(
&DraftOutward)

status = RibFeatureData-> put_DraftOutward(
DraftOutward)

(Table)=========================================================

| Property: | (VARIANT_BOOL) DraftOutward | TRUE if the draft is outward |
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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\RibFeatureData\RibFeatureData__DraftOutward.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
