---
title: "VariableFilletFeatureData::ReleaseSelectionAccess"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/VariableFilletFeatureData/VariableFilletFeatureData__ReleaseSelectionAccess.htm"
---

# VariableFilletFeatureData::ReleaseSelectionAccess

This
method is obsolete and has been superseded by VariableFilletFeatureData2::ReleaseSelectionAccess .

Description

This method releases access to the selections
used to define the variable fillet feature.

Syntax (OLE Automation)

void VariableFilletFeatureData.ReleaseSelectionAccess
( )

Syntax (COM)

status = VariableFilletFeatureData ->ReleaseSelectionAccess
( )

(Table)=========================================================

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

VariableFilletFeatureData::AccessSelections pust
the model into a rollback state to allow access to the selections that
define the variable fillet Feature. You must use VariableFilletFeatureData::ReleaseSelectionAccess
to restore the rollback state unless you call Feature::ModifyDefinition.

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\VariableFilletFeatureData\VariableFilletFeatureData__ReleaseSelectionAccess.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
