---
title: "SldWorks::RemoveMenuPopupItem"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__RemoveMenuPopupItem.htm"
---

# SldWorks::RemoveMenuPopupItem

This method is obsolete and has been superseded
by[SldWorks::RemoveMenuPopupItem2](sldworksAPI.chm::/SldWorks/SldWorks__RemoveMenuPopupItem2.htm).

Description

This method removes the specified menu pop-up item. The arguments passed
should match the arguments given when this pop-up menu item was created.

Syntax (OLE Automation)

retval = SldWorks.RemoveMenuPopupItem
( DocType, SelectType, Item, CallbackFcnAndModule, CustomNames, Unused)

(Table)=========================================================

| Input: | (long) DocType | Document type from which the pop-up menu item is to be removed as defined
in swDocumentTypes_e |
| --- | --- | --- |
| Input: | (long) SelectType | Selection type used by the menu item being removed |
| Input: | (BSTR) Item | Description that appears on the pop-up menu being removed |
| Input: | (BSTR) CallbackFcnAndModule | Callback function and module for this menu item as specified when the
menu item was added; see Frame::AddMenuPopupItem for details |
| Input: | (BSTR) CustomNames | Semi-colon separated list containing the names of the custom feature
types as specified when the menu item was added |
| Input: | (long) Unused | Reserved for future use; pass 0 |
| Return: | (BOOL) retval | TRUE if the menu item is removed successfully, FALSE otherwise |

Syntax (COM)

status = SldWorks->RemoveMenuPopupItem
( DocType, SelectType, Item, CallbackFcnAndModule, CustomNames, Unused,
&retval )

(Table)=========================================================

| Input: | (long) DocType | Document type from which the pop-up menu item is to be removed as defined
in swDocumentTypes_e |
| --- | --- | --- |
| Input: | (long) SelectType | Selection type used by the menu item being removed |
| Input: | (BSTR) Item | Description that appears on the pop-up menu being removed |
| Input: | (BSTR) CallbackFcnAndModule | Callback function and module for this menu item as specified when the
menu item was added; see Frame::AddMenuPopupItem for details |
| Input: | (BSTR) CustomNames | Semi-colon separated list containing the names of the custom feature
types as specified when the menu item was added |
| Input: | (long) Unused | Reserved for future use; pass 0 |
| Output: | (VARIANT_BOOL) retval | TRUE if the menu item is removed successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The enueration swDocNONE is not valid for DocType.

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\SldWorks\SldWorks__RemoveMenuPopupItem.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
