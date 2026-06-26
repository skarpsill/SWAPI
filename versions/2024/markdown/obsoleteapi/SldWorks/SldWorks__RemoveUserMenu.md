---
title: "SldWorks::RemoveUserMenu"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__RemoveUserMenu.htm"
---

# SldWorks::RemoveUserMenu

This
method is obsolete and has been superseded by[SldWorks::RemoveMenu](sldworksAPI.chm::/SldWorks/SldWorks__RemoveMenu.htm).

Description

This method removes the menu item or shortcut menu associated with the
specified unique menu ID. By specifying the menu ID, you can remove a
blank menu item.

Syntax (OLE Automation)

retval = SldWorks.RemoveUserMenu (
docType, menuIdIn, moduleName )

(Table)=========================================================

| Input: | (long) docType | Type of document to which this menu item had been added |
| --- | --- | --- |
| Input: | (long) menuIdIn | The ID of the menu item to remove; this menu ID is the same ID returned
from your call to SldWorks::AddMenuItem2 or SldWorks::AddMenuPopupItem |
| Input: | (BSTR) moduleName | Name of the module (for example, USERDLL) |
| Return: | (VARIANT_BOOLEAN) retval | TRUE if successful, FALSE if unsuccessful |

Syntax (COM)

status = SldWorks->RemoveUserMenu
( docType, menuIdIn, moduleName, &retval )

(Table)=========================================================

| Input: | (long) docType | Type of document to which this menu item had been added |
| --- | --- | --- |
| Input: | (long) menuIdIn | The ID of the menu item to remove; this menu ID is the same ID returned
from your call to SldWorks::AddMenuItem2 or SldWorks::AddMenuPopupItem |
| Input: | (BSTR) moduleName | Name of the module (for example, USERDLL) |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if unsuccessful |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\SldWorks\SldWorks__RemoveUserMenu.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
