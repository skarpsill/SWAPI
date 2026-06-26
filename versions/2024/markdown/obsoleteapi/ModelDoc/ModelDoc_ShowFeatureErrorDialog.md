---
title: "ModelDoc::ShowFeatureErrorDialog"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc_ShowFeatureErrorDialog.htm"
---

# ModelDoc::ShowFeatureErrorDialog

This property is obsolete and has been superseded
by[ModelDoc2::ShowFeatureErrorDialog](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ShowFeatureErrorDialog.htm).

Description

During feature creation operations, this property
gets or sets whether an error dialog is displayed.

Syntax (OLE Automation)

dialogState = ModelDoc. ShowFeatureErrorDialog (VB
Get property)

ModelDoc. ShowFeatureErrorDialog = dialogState (VB
Set property)

dialogState = ModelDoc.GetShowFeatureErrorDialog
( ) (C++ Get property)

ModelDoc.SetShowFeatureErrorDialog (dialogState) (C++
Set property)

(Table)=========================================================

| Property: | (BOOL) dialogState | True if error dialogs will be displayed during
feature creation |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->get_ShowFeatureErrorDialog
( &dialogState)

status = ModelDoc->put_ShowFeatureErrorDialog
(dialogState)

(Table)=========================================================

| Output: | (BOOL) retval | True if error dialogs will be displayed during
feature creation |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Currently, this property only handles errors for
the rebuild error dialog.

It is your responsibility to reset this value to
the SolidWorks default (TRUE), when your are finished.

To obtain the specific error value associated with
a feature, use Feature::GetErrorCode.

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
<param name="Items" value="Feature::GetErrorCode$$**$$ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc_ShowFeatureErrorDialog.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
