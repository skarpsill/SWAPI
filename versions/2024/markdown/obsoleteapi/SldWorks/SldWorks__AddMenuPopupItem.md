---
title: "SldWorks::AddMenuPopupItem"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__AddMenuPopupItem.htm"
---

# SldWorks::AddMenuPopupItem

This method is obsolete and has been superseded
by[SldWorks::AddMneuPopupItem2](sldworksAPI.chm::/SldWorks/SldWorks__AddMenuPopupItem2.htm).

Description

This mehod adds a menu item or a separator to a shortcut menu (right-mouse
buttonkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}menu).
This capability only operates when the application is implemented as a
DLL and not as an executable (.exe).

Syntax (OLE Automation)

retval = SldWorks.AddMenuPopupItem
( docType, selType, Item, CallbackFcnAndModule, CustomNames )

(Table)=========================================================

| Input: | (long) DocType | Document type to which to add the menu item |
| --- | --- | --- |
| Input: | (long) selType | Selection type to which to add the menu item |
| Input: | (BSTR) Item | Description that appears on the shortcut menu |
| Input: | (BSTR) CallbackFcnAndModule | Function to call when end-user clicks your menu item (see SldWorks::AddMenuItem) |
| Input: | (BSTR) CustomNames | Names of custom feature types |
| Return: | (BOOL) retval | TRUE if menu item is successfully added, FALSE otherwise |

Syntax (COM)

status = SldWorks->AddMenuPopupItem
( docType, selType, Item, CallbackFcnAndModule, CustomNames, &retval
)

(Table)=========================================================

| Input: | (long) DocType | Document type to which to add the menu item |
| --- | --- | --- |
| Input: | (long) selType | Selection type to which to add the menu item |
| Input: | (BSTR) Item | Description that appears on the shortcut menu |
| Input: | (BSTR) CallbackFcnAndModule | Function to call when end-user clicks your menu item (see SldWorks::AddMenuItem) |
| Input: | (BSTR) CustomNames | Names of custom feature types |
| Output: | (long)retval | TRUE if menu item is successfully added, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To add a separator the Item argument , set
to NULL or an empty string.

If the select type is a custom feature (for
example, swSelATTRIBUTES), the menu item appears on the shortcut menu
only if the custom feature name is included in CustomNames.

If the select type is swSelEVERYTHING, the
menu item appears on the shortcut menu of any standard SolidWorks objects.
This does not include the shortuct menu of custom features such as attributes.

The CustomNames argument contains a semi-colon
separated list containing the names of the custom feature types. This
argument is only applicable if SelType is a custom feature type (for example,
swSelATTRIBUTES). If swSelATTRIBUTES,
thenthis field should be the name of the attribute definition.

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
<param name="Items" value="SldWorks_Object$$**$$ZModifyUserInterface$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\SldWorks\SldWorks__AddMenuPopupItem.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
