---
title: "SldWorks::GetToolbarState"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__GetToolbarState.htm"
---

# SldWorks::GetToolbarState

This method is obsolete and has been superseded
by[SldWorks::GetToolbarState2](sldworksAPI.chm::/SldWorks/SldWorks__GetToolbarState2.htm).

Description

This method returns the state of a toolbar.

Syntax (OLE Automation)

retval = SldWorks.GetToolbarState (
Module, toolbarID, toolbarState )

(Table)=========================================================

| Input: | (BSTR) Module | Name of the module (for example, USERDLL) |
| --- | --- | --- |
| Input: | (long) toolbarID | Toolbar ID |
| Input: | (long) toolbarState | Toolbar state as defined in swToolbarStates_e |
| Return: | (Boolean)retval | TRUE or FALSE based on toolbarState |

Syntax (COM)

status = SldWorks->GetToolbarState
( Module, toolbarID, toolbarState, &retval )

(Table)=========================================================

| Input: | (BSTR)Module | Name of the module (for example, USERDLL) |
| --- | --- | --- |
| Input: | (long)toolbarID | Toolbar ID |
| Input: | (long)toolbarState | Toolbar state as defined in swToolbarStates_e |
| Output: | (VARIANT_BOOL)retval | TRUE or FALSE based on toolbarState |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can determine if a toolbar is hidden by passing swToolbarHidden
in toolbarState.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="SldWorks_Object$$**$$ZModifyUserInterface$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\SldWorks\SldWorks__GetToolbarState.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
