---
title: "ModelDoc::SetInferenceMode"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetInferenceMode.htm"
---

# ModelDoc::SetInferenceMode

This
method is obsolete and has been superseded by[ModelDoc2::SetInferenceMode](../ModelDoc2/ModelDoc2__SetInferenceMode.htm).

Description

This method sets whether the sketch inference
mode for this ModelDoc is turned off or not. This affects sketch entity
snapping or infering constraints to other geometry during creation.

Syntax (OLE Automation)

void ModelDoc.SetInferenceMode (inferenceMode)

(Table)=========================================================

| Input: | (BOOL) inferenceMode | TRUE to enable sketch inference mode, FALSE to
disable it |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->SetInferenceMode ( inferenceMode
)

(Table)=========================================================

| Input: | (VARIANT_BOOL) inferenceMode | TRUE to enable sketch inference mode, FALSE to
disable it |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Setting the inference mode to FALSE allows faster
sketching without inferencing, similar to ModelDoc::SetAddToDB, except
that using this method does not disable Undo operations.

Setting the inference mode to TRUE allows inferencing
during sketch operations, subject to other settings that may disable inferencing,
such as ModelDoc::AutoInferToggle, ModelDoc::SetAddToDB, and DrawingDoc::StartDrawing.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc\ModelDoc__SetInferenceMode.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
