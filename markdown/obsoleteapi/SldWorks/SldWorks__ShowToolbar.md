---
title: "SldWorks::ShowToolbar"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__ShowToolbar.htm"
---

# SldWorks::ShowToolbar

This method is obsolete. SolidWorks manages
the display of the toolbars based on the user's action; therefore, this
method is not needed. There are no alternative methods available to use.

Description

This method displays a toolbar that was created with SldWorks::AddToolbar.

Syntax (OLE Automation)

retval = SldWorks.ShowToolbar ( moduleName,
toolbarId )

(Table)=========================================================

| Input: | (BSTR) moduleName | Name of the module (that is, USERDLL) |
| --- | --- | --- |
| Input: | (long) toolbarId | Toolbar ID |
| Return: | (VARIANT_BOOL)retval | TRUE if successful, FALSE if unsuccessful |

Syntax (COM)

status = SldWorks->ShowToolbar (
moduleName, toolbarId, &retval )

(Table)=========================================================

| Input: | (BSTR)moduleName | Name of the module (that is, USERDLL) |
| --- | --- | --- |
| Input: | (long)toolbarId | Toolbar ID |
| Output: | (VARIANT_BOOL)retval | TRUE if successful, FALSE if unsuccessful |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\SldWorks\SldWorks__ShowToolbar.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Toolbar_Creation_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\SldWorks\SldWorks__ShowToolbar.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
