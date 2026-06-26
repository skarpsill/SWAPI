---
title: "SldWorks::RemoveToolbar"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__RemoveToolbar.htm"
---

# SldWorks::RemoveToolbar

This method is obsolete and has been superseded
by[SldWorks::RemoveToolbar2](sldworksAPI.chm::/SldWorks/SLDWORKS__REMOVETOOLBAR2.HTM).

Description

This method removes a toolbar
that was created with SldWorks::AddToolbar.

Syntax (OLE Automation)

retval = SldWorks.RemoveToolbar ( Module,
toolbarId )

(Table)=========================================================

| Input: | (BSTR) Module | Name of the module (that is, USERDLL) |
| --- | --- | --- |
| Input: | (long) toolbarId | Toolbar ID |
| Return: | (Boolean)retval | TRUE if successful, FALSE if unsuccessful |

Syntax (COM)

status = SldWorks->RemoveToolbar
( Module, toolbarId, &retval )

(Table)=========================================================

| Input: | (BSTR)Module | Name of the module (that is, USERDLL) |
| --- | --- | --- |
| Input: | (long)toolbarId | Toolbar ID |
| Output: | (VARIANT_BOOL)retval | TRUE if successful, FALSE if unsuccessful |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

If the SolidWorks application is exiting and your application is still
added-in, then you should not call this method. You should, however, clean
up all other items such as the Cbitmap objects. Doing so allows your toolbar
to get reloaded in the same position when the SolidWorks application is
restarted.

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\SldWorks\SldWorks__RemoveToolbar.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
