---
title: "Frame::AddMenuItem"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Frame/Frame__AddMenuItem.htm"
---

# Frame::AddMenuItem

This method is obsolete and has been superseded
by[Frame::AddMenuItem2](sldworksAPI.chm::/Frame/Frame__AddMenuItem2.htm).

Description

This
method adds a menu item or a separator to an existing pull-down menu.

Syntax (OLE Automation)

retval
= Frame.AddMenuItem ( Menu, Item, Position, CallbackFcnAndModule)

(Table)=========================================================

| Input: | (BSTR)
Menu | Name
of the menu to which to add item. |
| --- | --- | --- |
| Input: | (BSTR)
Item | Name
of item (including accelerator key "&"). If Item is NULL
or empty, this method adds a separator. |
| Input: | (long)
Position | Specifies
the position at which to add the new menu item. The first item is at position
0. If Position is –1, the new menu item is added to the bottom of the
list. |
| Input: | (BSTR)
CallbackFcnAndModule | Information
about which functions SolidWorks calls (see below). |
| Return: | (BOOL)
retval | TRUE
if menu item was successfully added, FALSE if not. |

Syntax (COM)

status
= Frame->AddMenuItem ( Menu, Item, Position, CallbackFcnAndModule,
&retval )

(Table)=========================================================

| Input: | (BSTR)
Menu | Name
of the menu to which to add item. |
| --- | --- | --- |
| Input: | (BSTR)
Item | Name
of item (including accelerator key "&"). If Item is NULL
or empty, this method adds a separator. |
| Input: | (long)
Position | Specifies
the position at which to add the new menu item. The first item is at position
0. If Position is –1, the new menu item is added to the bottom of the
list. |
| Input: | (BSTR)
CallbackFcnAndModule | Information
about which functions SolidWorks calls (see below). |
| Output: | (VARIANT_BOOL)
retval | TRUE
if menu item was successfully added, FALSE if not. |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

If you want to create a pull-down menu, use Frame::AddMenu.

This capability only operates when your application
is implemented as a DLL, not as an EXE. In addition, any function exposed
as a callback from a menu item must be declared as an EXPORT or included
in your .def file.

You can add a new menu to any one of the four SolidWorks
frames (Main frame, Part frame, Assembly frame or Drawing frame). To do
this, you need to get the Frame object when the desired frame is active.
For example, if you want your menu to be available when a Part document
is active, then call SoldWorks::Frame when a part is first loaded or created,
and use that Frame object to call this method. Once you add your menu
to the Part frame, you do not need to do it again during the current SolidWorks
session.

The CallbackFcnAndModule argument specifies which
function to call when this menu item is selected by the user, the syntax
is as follows:

"dllname@function@updatefunction,hintstring"

where:

(Table)=========================================================

| dllname | Name of your library as specified in the project .def file. The actual
dll filename and the definition in the .def file must be the same. |
| --- | --- |
| function | Name of the function that gets called when the user presses the button.
This function must also be declared as an EXPORT in your .def file. |
| updatefunction | Optional argument that controls
the state of the button. If specified, SolidWorks calls this button before
the button is displayed. Define your updatefunction to return an int and
declare it as an EXPORT or included in your .def file. The display of
the button is controlled by the return value of the function as follows: return 0 - Menu item is unchecked and
disabled. return 1 - Menu item is unchecked and
enabled. This is the default menu state with if no update function is
specified. return 2 - Menu item is checked and
disabled. return 3 - Menu item is checked and
enabled. |
| hintstring | Optional argument that contains a text hint displayed in the SolidWorks
status bar when the user moves their mouse over this menu option. If a
hintstring is specified, it must be preceded by a comma. For Example: "Userdll@AddBox@checkForUserSelects,Add
a box" |

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Frame_Object$$**$$ZModifyUserInterface$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\Frame\Frame__AddMenuItem.htm" >
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Add_Menu_Item_Example$$**$$Add_Rename_and_Remove_Menu_Items_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\Frame\Frame__AddMenuItem.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
