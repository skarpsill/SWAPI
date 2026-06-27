---
title: "SldWorks::AddMenuItem2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__AddMenuItem2.htm"
---

# SldWorks::AddMenuItem2

This method is obsolete and has been superseded
by[SldWorks::AddMenuItem3](sldworksAPI.chm::/SldWorks/SldWorks__AddMenuItem3.htm).

Description

This method adds a menu item to the SolidWorks
interface.

Syntax (OLE Automation)

IsMenuItemAdded = SldWorks.AddMenuItem2 ( DocumentType,
Cookie, MenuItem, Position, MenuCallback, MenuEnableMethod, HintString
)

(Table)=========================================================

| Input: | (long) DocumentType | Document type to which to add the menu item |
| --- | --- | --- |
| Input: | (long) Cookie | Identifier of the menu as defined in swMenuIdentifiers_e; this is the
same Cookie that you specified in SwAddin::ConnectToSW |
| Input: | (BSTR) MenuItem | Menu string ("menuItem@subMenuString@menuString"); SolidWorks
creates menus and submenus only if they do not already exist. |
| Input: | (long) Position | Position at which to add the new menu item The first item is at position 0; if Position is –1, the new menu item
is added to the bottom of the list; this argument specifies the position
of the menu item in relation to its immediate parent menu |
| Input: | (BSTR) MenuCallback | Function to call when this menu item is selected |
| Input: | (BSTR) MenuEnableMethod | Optional function that controls the state of the menu item If specified, SolidWorks: Calls this function before displaying the menu Display of the menu item is controlled by the
return value of MenuEnableMethod If your method returns... Then the SolidWorks softeware... 0 Deselects and disables the menu item 1 Deselects and enables the menu item; this is the default menu state
with if no update function is specified 2 Selects and disables the menu item 3 Selects and enables the menu item |
| If your method returns... | Then the SolidWorks softeware... |  |
| 0 | Deselects and disables the menu item |  |
| 1 | Deselects and enables the menu item; this is the default menu state
with if no update function is specified |  |
| 2 | Selects and disables the menu item |  |
| 3 | Selects and enables the menu item |  |
| Input: | (BSTR) HintString | Text to show in the SolidWorks status bar when the user moves their
mouse over this menu item; if you specify a HintString, it must be preceded
by a comma |
| Output: | (VARIANT_BOOL) IsMenuItemAdded | 1 if menu item was successfully added, 0 if failure |

Syntax (COM)

status = SldWorks->AddMenuItem2 ( DocumentType,
Cookie, MenuItem, Position, MenuCallback, MenuEnableMethod, HintString,
&IsMenuItemAdded )

Parameters Table Start

(Table)=========================================================

| Input: | (long) DocumentType | Document type to which to add the menu item |
| --- | --- | --- |
| Input: | (long) Cookie | Identifier of the menu as defined in swMenuIdentifiers_e; this is the
same Cookie that you specified in SwAddin::ConnectToSW |
| Input: | (BSTR) MenuItem | Menu string ("menuItem@subMenuString@menuString"); SolidWorks
creates menus and submenus only if they do not already exist |
| Input: | (long) Position | Position at which to add the new menu item The first item is at position 0; if Position is –1, the new menu item
is added to the bottom of the list; this argument specifies the position
of the menu-item in relation to its immediate parent menu |
| Input: | (BSTR) MenuCallback | Function to call when this menu item is selected |
| Input: | (BSTR) MenuEnableMethod | Optional function that controls the state of the menu item If specified, SolidWorks: Calls this function before displaying the menu Display of the menu item is controlled by the
return value of MenuEnableMethod If your method returns... Then SolidWorks... 0 Deselects and disables the menu item. 1 Deselects and enables the menu item; This
is the default menu state with if no update function is specified 2 Selects and disables the menu item 3 Selects and enables the menu item |
| If your method returns... | Then SolidWorks... |  |
| 0 | Deselects and disables the menu item. |  |
| 1 | Deselects and enables the menu item; This
is the default menu state with if no update function is specified |  |
| 2 | Selects and disables the menu item |  |
| 3 | Selects and enables the menu item |  |
| Input: | (BSTR) HintString | Text to show in the SolidWorks status bar when the user moves their
mouse over this menu item; if you specify a HintString, it must be preceded
by a comma |
| Output: | (VARIANT_BOOL) IsMenuItemAdded | 1 if menu item was successfully added, 0 if failure |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For information about using this method with the
SwAddin object, see Using SwAddin to Create a SolidWorks Add-in.

You can add a new menu to any one of the four SolidWorks
frames (main, part, assembly, or drawing). To do this, call this method
with the appropriate argument in the DocumentType parameter. For example,
if you want your menu to be available when a part document is active,
then call this method and pass swDocPARTas the first argument. After you have added your menu to the part
frame, you do not need to do it again during the current SolidWorks session.
Once a part document is activated by the user, SolidWorks automatically
displays your menu option.

To add a menu separator, specify an empty string
for HintString:

' Adds a menu separator

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= iSldWorks.AddMenuItem2(swDocNONE, iCookie, "@Sample", -1,
"DocNONE_Item", "", "")

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\SldWorks\SldWorks__AddMenuItem2.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
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
<param name="Items" value="SldWorks_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\SldWorks\SldWorks__AddMenuItem2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
