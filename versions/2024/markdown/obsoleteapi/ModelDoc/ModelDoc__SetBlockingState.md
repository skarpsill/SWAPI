---
title: "ModelDoc::SetBlockingState"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetBlockingState.htm"
---

# ModelDoc::SetBlockingState

This method is obsolete
and has been superseded by[ModelDoc2::SetBlockingState](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetBlockingState.htm).

Description

This method sets the blocking state for the SolidWorks menus.

Syntax (OLE Automation)

(void) ModelDoc.SetBlockingState (
stateIn )

(Table)=========================================================

| Input: | (long) stateIn | One of the swBlockingStates_e options |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->SetBlockingState
( stateIn )

(Table)=========================================================

| Input: | (long) stateIn | One of the swBlockingStates_e options |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Reset the state when operations are completed by calling ModelDoc::ResetBlockingState.

NOTE:There must be a corresponding call to ModelDoc::ResetBlockingState for
every call to ModelDoc::SetBlocking. It is not enough to call ModelDoc::ResetBlockingState
once at the end of a sequence of operations that have called ModelDoc::SetBlockingState
several times.

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
<param name="Items" value="ModelDoc_Object$$**$$ZModifyUserInterface$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SetBlockingState.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
