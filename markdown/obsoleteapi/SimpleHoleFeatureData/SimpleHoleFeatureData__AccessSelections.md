---
title: "SimpleHoleFeatureData::AccessSelections"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SimpleHoleFeatureData/SimpleHoleFeatureData__AccessSelections.htm"
---

# SimpleHoleFeatureData::AccessSelections

This
method is obsolete and superseded by SimpleHoleFeatureData2::AccessSelections .

Description

This method gains access to the selections
used to define the simple hole feature.

Syntax (OLE Automation)

accessGained= SimpleHoleFeatureData.AccessSelections
(topDoc, component)

(Table)=========================================================

| Input: | (LPDISPATCH) topDoc | Top-level document |
| --- | --- | --- |
| Input: | (LPDISPATCH) component | Component in which the feature is to modify |
| Return: | (BOOL) accessGained | TRUE if the selections are
successfully accessed |

Syntax (COM)

status = SimpleHoleFeatureData ->IAccessSelections
( topDoc, component, &accessGained )

(Table)=========================================================

| Input: | (LPMODELDOC) topDoc | Top-evel document |
| --- | --- | --- |
| Input: | (LPCOMPONENT) component | Component in which the feature is to modify |
| Output: | (VARIANT_BOOL) accessGained | TRUE if the Selections are
successfully accessed |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To modify a feature in a part, the TopDoc argument
is the ModelDoc for the part and the Component argument should be NULL.

To modify a feature in an assembly, the TopDoc
argument should be the assembly's ModelDoc object and the Component argument
should be the Component object in which the feature is to be modified.

This method puts the model into a rollback state
to allow access to the selections that define the simple hole feature.
You must use SimpleHoleFeatureData::ReleaseSelectionAccess to restore
the rollback state unless you call Feature::ModifyDefinition.

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
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\SimpleHoleFeatureData\SimpleHoleFeatureData__AccessSelections.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
