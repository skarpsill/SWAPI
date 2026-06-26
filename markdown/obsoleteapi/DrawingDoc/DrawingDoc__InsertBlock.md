---
title: "DrawingDoc::InsertBlock"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__InsertBlock.htm"
---

# DrawingDoc::InsertBlock

This method is obsolete and has been superseded
by[SketchManager::InsertSketchBlockInstance](sldworksAPI.chm::/SketchManager/SketchManager__InsertSketchBlockInstance.htm).

Description

This method inserts a new
block instance into the drawing from a local block or block file (.sldblk).

NOTE:This method does not work for drawings opened in view-only mode.

Syntax (OLE Automation)

retval = DrawingDoc.InsertBlock ( blockName, X, Y,
Angle, Scale )

(Table)=========================================================

| Input: | (BSTR) blockName | Local block name or full path of the .sldblk file from which to insert
the block |
| --- | --- | --- |
| Input: | (double) X | X coordinate of the location of the origin of the block instance |
| Input: | (double) Y | Y coordinate of the location of the origin of the block instance |
| Input: | (double) Angle | Rotation angle of the block instance |
| Input: | (double) Scale | Scale of the block instance |
| Output: | (LPBLOCKINSTANCE) retval | Pointer to the block instance that is created |

Syntax (COM)

status = DrawingDoc->InsertBlock ( blockName,
X, Y, Angle, Scale, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (BSTR) blockName | Local block name or full path of the .sldblk file from which to insert
the block |
| --- | --- | --- |
| Input: | (double) X | X coordinate of the location of the origin of the block instance |
| Input: | (double) Y | Y coordinate of the location of the origin of the block instance |
| Input: | (double) Angle | Rotation angle of the block instance |
| Input: | (double) Scale | Scale of the block instance |
| Output: | (LPBLOCKINSTANCE) retval | Pointer to the block instance that is created |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method creates a block
definition if the block definition does not exist.

-kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}or
-

If the definition exists,
then this method uses that block definition to create the block instance.The name of the block instance
is the same as the filename of the block file, without the filename extension.

TIP:kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Instead
of using this method multiple times to insert the same block, use it once
to insert the first block instance. Next, use the return interface pointer
to get the block definition, BlockInstance::Definition, and then use the
BlockDefinition::InsertInstance method to insert the rest of the blocks.

To save a block instance and
its definition into a block file (.sldblk), use DrawingDoc::SaveBlock.

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
<param name="Items" value="ZReleaseNotes2003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DrawingDoc\DrawingDoc__InsertBlock.htm" >
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
<param name="Items" value="DrawingDoc_Object$$**$$BlockInstance_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DrawingDoc\DrawingDoc__InsertBlock.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic3
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
<param name="Items" value="EXGetBlockDefinitions$$**$$EXInsertDWGBlock$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DrawingDoc\DrawingDoc__InsertBlock.htm" >
<param name="_ID" value="RelatedTopic3" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
