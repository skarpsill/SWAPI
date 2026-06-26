---
title: "WizardHoleFeatureData::EndCondition"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__EndCondition.htm"
---

# WizardHoleFeatureData::EndCondition

This
property is obsolete and has been superseded by WizardHoleFeatureData2::EndCondition .

Description

This property gets or sets the hole wizard
feature end condition type.

Syntax (OLE Automation)

endCondition= WizardHoleFeatureData.EndCondition (VB
Get property)

WizardHoleFeatureData.EndCondition =EndCondition(VB Set property)

endCondition= WizardHoleFeatureData.GetEndCondition ( ) (C++
Get property)

WizardHoleFeatureData.SetEndCondition (endCondition )(C++ Set property)

(Table)=========================================================

| Property: | (int) endCondition | End condition type of the hole wizard feature |
| --- | --- | --- |

Syntax (COM)

status = WizardHoleFeatureData ->get_EndCondition
( &endCondition)

status = WizardHoleFeatureData ->put_EndCondition
(endCondition)

(Table)=========================================================

| Property: | (int) endCondition | End condition type of the hole wizard feature |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The end condition type is specified in swEndConditions_e. It should
have one of these values:

- swEndCondBlind
- swEndCondThroughAll
- swEndCondThroughNext
- swEndCondUpToVertex
- swEndCondUpToSurface
- swEndCondOffsetFromSurface
- swEndCondMidPlane

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\WizardHoleFeatureData\WizardHoleFeatureData__EndCondition.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
