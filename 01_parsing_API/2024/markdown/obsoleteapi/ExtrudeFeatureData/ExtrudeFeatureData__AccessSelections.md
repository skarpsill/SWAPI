---
title: "ExtrudeFeatureData::AccessSelections"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData/ExtrudeFeatureData__AccessSelections.htm"
---

# ExtrudeFeatureData::AccessSelections

This
method is obsolete and has been superseded by ExtrudeFeatureData2::AccessSelections .

Description

This methodgains
access to the selections used to define the extrusion feature.

Syntax (OLE Automation)

accessGained= ExtrudeFeatureData.AccessSelections
(topDoc, component)

(Table)=========================================================

| Input: | (LPDISPATCH) topDoc | Top-level document |
| --- | --- | --- |
| Input: | (LPDISPATCH) component | Component in which the feature is to be modified |
| Return: | (BOOL) accessGained | TRUE if the selections were successfully accessed, FALSE if not |

Syntax (COM)

status = ExtrudeFeatureData->IAccessSelections
( topDoc, component, &accessGained )

(Table)=========================================================

| Input: | (LPMODELDOC) topDoc | Top-level document |
| --- | --- | --- |
| Input: | (LPCOMPONENT) component | Component in which the feature is to be modified |
| Output: | (VARIANT_BOOL) accessGained | TRUE if the selections were
successfully accessed, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful. |

Remarks

To modify a feature in a part, set the topDoc argument
to the ModelDoc for the part and the component argument to NULL.

To modify a feature in an assembly, set the topDoc
argument to the assembly ModelDoc object and the component argument to
the component object in which the feature is to be modified.

This method puts the model into a rollback state
to allow access to the selections that define the extrusion feature. Use[ExtrudeFeatureData::ReleaseSelectionAccess](ExtrudeFeatureData__ReleaseSelectionAccess.htm)to restore the rollback state, unless you call Feature::ModifyDefinition.

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
<param name="Items" value="ZReleaseNotes2000$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ExtrudeFeatureData\ExtrudeFeatureData__AccessSelections.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ExtrudeFeatureData\ExtrudeFeatureData__AccessSelections.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
