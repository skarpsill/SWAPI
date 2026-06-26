---
title: "DrawingDoc::CreateBlockDefinition"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateBlockDefinition.htm"
---

# DrawingDoc::CreateBlockDefinition

This method is obsolete and has been superseded
by[SkethcManager::MakeSketchBlockFromFile](sldworksAPI.chm::/SketchManager/SketchManager__MakeSketchBlockFromFile.htm),[SketchManager::MakeSketchBlockSelected](sldworksAPI.chm::/SketchManager/SketchManager__MakeSketchBlockFromSelected.htm),
and[SketchManager::MakeSketchBlockFromSketch](sldworksAPI.chm::/SketchManager/SketchManager__MakeSketchBlockFromSketch.htm).

Description

This method creates a block definition from
the specified entities.

Syntax (OLE Automation)

retval = DrawingDoc.CreateBlockDefinition ( Name,
XRefFileName, Instance, Segments, Points, Notes, Dimensions, Blocks )

(Table)=========================================================

| Input: | (BSTR) Name | Name of the block definition |
| --- | --- | --- |
| Input: | (BSTR) XRefFileName | Name of the file that the block definition references |
| Input: | (VARIANT_BOOL) Instance | TRUE if the block instance should be created in the same place from
the definition, FALSE if not |
| Input: | (VARIANT) Segments | VARIANT of type SafeArray of Dispatch objects of the sketch segments
that should be part of the block definition |
| Input: | (VARIANT) Points | VARIANT of type SafeArray of Dispatch objects of the sketch points that
should be part of the block definition |
| Input: | (VARIANT) Notes | VARIANT of type SafeArray of Dispatch objects of the notes that should
be part of the block definition |
| Input: | (VARIANT) Dimensions | VARIANT of type SafeArray of Dispatch objects of the display dimensions
that should be part of the block definition |
| Input: | (VARIANT) Blocks | VARIANT of type SafeArray of Dispatch objects of the block instances
that should be part of the block definition |
| Output: | (LPDISPATCH) retval | Dispatch pointer to the block definition |

Syntax (COM)

status = DrawingDoc->ICreateBlockDefinition (
Name, XRefFileName, Instance, SegmentCount, Segments, PointCount, Points,
NoteCount, Notes, DimensionCount, Dimensions, BlockCount, Blocks, &retval
)

Parameters Table Start

(Table)=========================================================

| Input: | (BSTR) Name | Name of the block definition |
| --- | --- | --- |
| Input: | (BSTR) XRefFileName | Name of the file that the block definition references |
| Input: | (VARIANT_BOOL) Instance | TRUE if the block instance should be created in the same place from
this definition, FALSE if not |
| Input: | (long) SegmentCount | Number of sketch segments |
| Input: | (LPSKETCHSEGMENT*) Segments | Array of sketch segments of size SegmentCount |
| Input: | (long) PointCount | Number of sketch points |
| Input: | (LPSKETCHPOINT*) Points | Array of sketch points of size PointCount |
| Input: | (long) NoteCount | Number of notes |
| Input: | (LPNOTE*) Notes | Array of notes of size NoteCount |
| Input: | (long) DimensionCount | Number of display dimensions |
| Input: | (LPDISPLAYDIMENSION*) Dimensions | Array of display dimensions of size DimensionCount |
| Input: | (long) BlockCount | Number of block instances |
| Input: | (LPBLOCKINSTANCE*) Blocks | Array of block instances of size BlockCount |
| Output: | (LPBLOCKDEFINITION) retval | Interface to the block definition |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The DrawingDoc::CreateBlockDefinition
method is similar to the DrawingDoc::MakeBlockDefinition method except
that instead of creating a block definition from the selected entities,
DrawingDoc::CreateBlockDefinition creates a block definition from the
specified entities.

If you have the pointers to
the entities for the block definition, running DrawingDoc::CreateBlockDefinition
should be faster than selecting all of the entities and then running DrawingDoc::MakeBlockDefinition
because of the time spent having to select the entities.

DrawingDoc::CreateBlockDefinition
deletes all of the entities that are input because these entities become
part of each block definition. To create a block instance from these entities,
exactly in the same place as the entities were before running DrawingDoc::CreateBlockDefinition,
set the Instance argument to TRUE.

Use the BlockDefinition::InsertInstance
method to create block instances of this definition.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DrawingDoc\DrawingDoc__CreateBlockDefinition.htm" >
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
<param name="Items" value="DrawingDoc_Object$$**$$SketchSegment_Object$$**$$SketchPoint_Object$$**$$Note_Object$$**$$DisplayDimension_Object$$**$$BlockInstance_Object$$**$$BlockDefinition_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DrawingDoc\DrawingDoc__CreateBlockDefinition.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic5
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
<param name="Items" value="EXCreateBlockDefinition$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DrawingDoc\DrawingDoc__CreateBlockDefinition.htm" >
<param name="_ID" value="RelatedTopic5" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
