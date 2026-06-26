---
title: "VariableFilletFeatureData::PropagateToTangentFaces"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/VariableFilletFeatureData/VariableFilletFeatureData__PropagateToTangentFaces.htm"
---

# VariableFilletFeatureData::PropagateToTangentFaces

This
property is obsolete and has been superseded by VariableFilletFeatureData2::PropagateToTangentFaces .

Description

This property gets or sets whether to extend
fillet to all faces tangent to the selected face or edge.

Syntax (OLE Automation)

propTgtFaces= VariableFilletFeatureData.PropagateToTangentFaces (VB
Get property)

VariableFilletFeatureData.PropagateToTangentFaces
=propTgtFaces(VB Set property)

propTgtFaces= VariableFilletFeatureData.GetPropagateToTangentFaces
( ) (C++ Get property)

VariableFilletFeatureData.SetPropagateToTangentFaces
(propTgtFaces) (C++ Set property)

(Table)=========================================================

| Property: | ( BOOL ) propTgtFaces | TRUE if variable fillet feature should extend
fillet to all faces tangent to the selected face or edge, FALSE if not | The default fillet radius of the Simple Fillet
feature. |
| --- | --- | --- | --- |

Syntax (COM)

status = VariableFilletFeatureData ->get_PropagateToTangentFaces
( &propTgtFaces)

status = VariableFilletFeatureData ->put_PropagateToTangentFaces
(propTgtFaces)

(Table)=========================================================

| Property: | ( VARIANT_BOOL ) propTgtFaces | TRUE if variable fillet feature should extend
fillet to all faces tangent to the selected face or edge, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\VariableFilletFeatureData\VariableFilletFeatureData__PropagateToTangentFaces.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
