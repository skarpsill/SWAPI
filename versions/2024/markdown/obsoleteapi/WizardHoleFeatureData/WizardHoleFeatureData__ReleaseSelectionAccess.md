---
title: "WizardHoleFeatureData::ReleaseSelectionAccess"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/WizardHoleFeatureData/WizardHoleFeatureData__ReleaseSelectionAccess.htm"
---

# WizardHoleFeatureData::ReleaseSelectionAccess

This method is obsolete and has been superseded
by[WizardHoleFeatureData2::ReleaseSelectionAccess](sldworksAPI.chm::/WizardHoleFeatureData2/WizardHoleFeatureData2__ReleaseSelectionAccess.htm).

Description

This method releases access
to the selections used to define the hole wizard feature.

Syntax (OLE Automation)

void WizardHoleFeatureData.ReleaseSelectionAccess
( )

Syntax (COM)

status = WizardHoleFeatureData ->ReleaseSelectionAccess
( )

(Table)=========================================================

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

WizardHoleFeatureData::AccessSelections puts the
model into a rollback state to allow access to the selections that define
the hole wizard feature. You must use WizardHoleFeatureData::ReleaseSelectionAccess
to restore the rollback state unless you call Feature::ModifyDefinition.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZFeatureDefinition$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\sw2003\WizardHoleFeatureData\WizardHoleFeatureData__ReleaseSelectionAccess.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
