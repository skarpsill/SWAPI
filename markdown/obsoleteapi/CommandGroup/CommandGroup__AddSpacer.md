---
title: "CommandGroup::AddSpacer"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CommandGroup/CommandGroup__AddSpacer.htm"
---

# CommandGroup::AddSpacer

This method is obsolete and has been superseded
by[CommandGroup::AddSpace2](sldworksAPI.chm::/CommandGroup/CommandGroup__AddSpacer2.htm).

Description

This method adds a spacer
between items in a CommandGroup.

Syntax (OLE Automation)

*CmdIndex = CommandGroup.AddSpacer ( Position)

(Table)=========================================================

| Input: | (long) Position | Position of the spacer within
the CommandGroup NOTE: Specify 0 to add this a spacer to the beginning of the CommandGroup, or
specify -1 to add it to the end of the CommandGroup. This argument specifies
the position of the spacer in relation to its immediate parent item. |
| --- | --- | --- |
| Output: | (long ) *CmdIndex | Index of the item within the
CommandGroup as assigned by SolidWorks |

Syntax (COM)

status = CommandGroup->AddSpacer ( Position, &CmdIndex)

Parameters Table Start

(Table)=========================================================

| Input: | (long) Position | Position of the spacer within
the CommandGroup NOTE: Specify 0 to add this a spacer to the beginning of the CommandGroup, or
specify -1 to add it to the end of the CommandGroup. This argument specifies
the position of the spacer in relation to its immediate parent item. |
| --- | --- | --- |
| Output: | (long ) *CmdIndex | Index of the item within the CommandGroup as
assigned by SolidWorks |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\CommandGroup\CommandGroup__AddSpacer.htm" >
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
<param name="Items" value="CommandGroup_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\CommandGroup\CommandGroup__AddSpacer.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
