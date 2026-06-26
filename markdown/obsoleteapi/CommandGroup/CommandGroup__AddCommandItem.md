---
title: "CommandGroup::AddCommandItem"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CommandGroup/CommandGroup__AddCommandItem.htm"
---

# CommandGroup::AddCommandItem

This method is obsolete and has been superseded
by[CommandGroup::AddCommandItem2](sldworksAPI.chm::/CommandGroup/CommandGroup__AddCommandItem2.htm).

Description

This method adds a combination
menu and toolbar item to a CommandGroup.

Syntax (OLE Automation)

*CmdIndex = CommandGroup.AddCommandItem ( Name, Position,
HintString, ToolTip, ImageListIndex, CallbackFunction, EnableMethod, userID)

(Table)=========================================================

| Input: | (BSTR) Name | Name of the item to add to the
CommandGroup |
| --- | --- | --- |
| Input: | (long) Position | Position of the item within the
CommandGroup NOTE: Specify 0 to add this item to the beginning of the CommandGroup,
or specify -1 to add it to the end of the CommandGroup. This argument
specifies the position of the item in relation to its immediate parent
item. |
| Input: | (BSTR) HintString | Text displayed in the SolidWorks status bar when
the pointer is on the item |
| Input: | (BSTR) ToolTip | ToolTip displayed when the pointer is on the
item |
| Input: | (long) ImageListIndex | Index number of the image for
the item in the parent CommandGroup (see Remarks ) |
| Input: | (BSTR) CallbackFunction | Function to call when this item is selected |
| Input: | (BSTR) EnableMethod | Optional function that controls
the state of the item; if specified, then SolidWorks calls this function
before displaying the item If your method returns... Then the SolidWorks software... 0 Deselects and disables the item 1 Deselects and enables the item; this is the default state if no update
function is specified 2 Selects and disables the item 3 Selects and enables the item |
| If your method returns... | Then the SolidWorks software... |  |
| 0 | Deselects and disables the item |  |
| 1 | Deselects and enables the item; this is the default state if no update
function is specified |  |
| 2 | Selects and disables the item |  |
| 3 | Selects and enables the item |  |
| Input: | (long) userID | User-defined command ID or 0 if not used |
| Output: | (long ) *CmdIndex | Index of the item within the CommandGroup as
assigned by SolidWorks |

Syntax (COM)

status = CommandGroup->AddCommandItem ( Name,
Position, HintString, ToolTip, ImageListIndex, CallbackFunction, EnableMethod,
userID, &CmdIndex)

Parameters Table Start

(Table)=========================================================

| Input: | (BSTR) Name | Name of the item to add to the
CommandGroup |
| --- | --- | --- |
| Input: | (long) Position | Position of the item within the
CommandGroup NOTE: Specify 0 to add this item to the beginning of the CommandGroup,
or specify -1 to add this item to the end of the CommandGroup. This argument
specifies the position of the item in relation to its immediate parent
item. |
| Input: | (BSTR) HintString | Text displayed in the SolidWorks
status bar when the pointer is on the item |
| Input: | (BSTR) ToolTip | ToolTip displayed when the pointer
is on the item |
| Input: | (long) ImageListIndex | Index number of the image for the item in the
parent CommandGroup (see Remarks ) |
| Input: | (BSTR) CallbackFunction | Function to call when this item
is selected |
| Input: | (BSTR) EnableMethod | Optional function that controls
the state of the item; if specified, then SolidWorks calls this function
before displaying the item If your method returns... Then the SolidWorks software... 0 Deselects and disables the item 1 Deselects and enables the item; this is the default state if no update
function is specified 2 Selects and disables the item 3 Selects and enables the item |
| If your method returns... | Then the SolidWorks software... |  |
| 0 | Deselects and disables the item |  |
| 1 | Deselects and enables the item; this is the default state if no update
function is specified |  |
| 2 | Selects and disables the item |  |
| 3 | Selects and enables the item |  |
| Input: | (long) userID | User-defined command ID or 0 if not used |
| Output: | (long ) *CmdIndex | Index of the item within the
CommandGroup as assigned by SolidWorks |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

ImageListIndex is 0-based.
The size of the index is equal to number of the images in the large or
small bitmap file for that CommandGroup. See CommandGroup::LargeIcontList
and CommandGroup::SmallIconList for details.

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
<param name="Items" value="ZReleaseNotes006$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\CommandGroup\CommandGroup__AddCommandItem.htm" >
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
<param name="Items" value="CommandGroup_Object$$**$$CommandGroupImages$$**$$CommandGroupItems$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\CommandGroup\CommandGroup__AddCommandItem.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
