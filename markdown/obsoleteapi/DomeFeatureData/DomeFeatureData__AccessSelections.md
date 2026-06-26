---
title: "DomeFeatureData::AccessSelections"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DomeFeatureData/DomeFeatureData__AccessSelections.htm"
---

# DomeFeatureData::AccessSelections

This method is obsolete and has been superseded
by DomeFeatureData2::AccessSelections .

Description

This method gains access to the selections used to define this dome
feature.

Syntax (OLE Automation)

retval
= DomeFeatureData.AccessSelections( TopDoc, Component )

(Table)=========================================================

| Input: | (LPDISPATCH)
TopDoc | Top-level
document (see Remarks ) |
| --- | --- | --- |
| Input: | (LPDISPATCH)
Component | Component
for the feature (see Remarks ) |
| Return: | (BOOL)
retval | TRUE
if the selections where successfully accessed, FALSE if not |

Syntax (COM)

status
= DomeFeatureData->IAccessSelections( TopDoc, Component, &retval
)

(Table)=========================================================

| Input: | (LPMODELDOC)
TopDoc | Top-level
document (see Remarks ) |
| --- | --- | --- |
| Input: | (LPCOMPONENT)
Component | Component
for the feature (see Remarks ) |
| Output: | (VARIANT_BOOL)
retval | TRUE
if the selections where successfully accessed, FALSE if not |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

To modify a feature in a part, set the TopDoc argument to the ModelDoc
for the part and the Component argument to NULL.

To modify a feature in an assembly, set the TopDoc to the ModelDoc for
the assembly and the Component argument to the component in which the
feature is to be modified.

Because the face on which the dome was defined is not accessible once
the dome has been created, this method puts the model into a rollback
state to allow access to the selections that define the dome. You must
use DomeFeatureData::ReleaseSelectionAccess to restore the rollback state,
unless you call Feature::ModifyDefinition.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\DomeFeatureData\DomeFeatureData__AccessSelections.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
