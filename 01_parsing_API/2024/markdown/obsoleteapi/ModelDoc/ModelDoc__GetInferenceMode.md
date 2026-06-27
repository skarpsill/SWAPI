---
title: "ModelDoc::GetInferenceMode"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetInferenceMode.htm"
---

# ModelDoc::GetInferenceMode

This
method is obsolete and has been superseded byModelDoc2::GetInferenceMode.

Description

This method determines whether the sketch inference
mode for this ModelDoc has been turned off or not. This affects sketch
entity snapping, or inferring constraints to other geometry, during creation.

Syntax (OLE Automation)

inferenceMode = ModelDoc.GetInferenceMode ( )

(Table)=========================================================

| Return: | (BOOL) inferenceMode | TRUE if sketch inference mode is enabled, FALSE
if it is disabled |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetInferenceMode ( &inferenceMode
)

(Table)=========================================================

| Input: | (VARIANT_BOOL) inferenceMode | TRUE if sketch inference mode is enabled, FALSE
if it is disabled |
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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZGetSetAddToDB$$**$$ZGetSetDisplayWhenAdded$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc\ModelDoc__GetInferenceMode.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
