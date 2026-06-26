---
title: "DrawingDoc::CreateCustomSymbol"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateCustomSymbol.htm"
---

# DrawingDoc::CreateCustomSymbol

This method is obsolete and has been superseded
by[DrawingDoc::CreateBlockDefinition](DrawingDoc__CreateBlockDefinition.htm).

Description

This method makes a custom symbol from the
specified entities.

Syntax (OLE Automation)

retval = DrawingDoc.CreateCustomSymbol ( Segments,
Points, Notes )

(Table)=========================================================

| Input: | (VARIANT) Segments | VARIANT of type SafeArray of Dispatch objects of the sketch segments
to be part of this custom symbol |
| --- | --- | --- |
| Input: | (VARIANT) Points | VARIANT of type SafeArray of Dispatch objects of the sketch points to
be part of this custom symbol |
| Input: | (VARIANT) Notes | VARIANT of type SafeArray of Dispatch objects of the notes to be part
of this custom symbol |
| Output: | (LPDISPATCH) retval | Dispatch pointer to the new custom symbol |

Syntax (COM)

status = DrawingDoc->ICreateCustomSymbol ( SegmentCount,
Segments, PointCount, Points, NoteCount, Notes, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (long) SegmentCount | Number of segments in the Segments array |
| --- | --- | --- |
| Input: | (LPSKETCHSEGMENT*) Segments | Array of sketch segments to be part of this
custom symbol |
| Input: | (long) PointCount | Number of points in the Point array |
| Input: | (LPSKETCHPOINT*) Points | Array of sketch points to be part of this
custom symbol |
| Input: | (long) NoteCount | Number of notes in the Notes array |
| Input: | (LPNOTE*) Notes | Array of notes to be part of this custom
symbol |
| Output: | (LPCUSTOMSYMBOL) retval | Interface to the custom symbol |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is similar to[DrawingDoc::MakeCustomSymbol2](DrawingDoc__MakeCustomSymbol2.htm),
except that instead of creating a custom symbol from the selected entities,
this method creates a custom symbol from the specified entities.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
you already have the pointers to the entities that need to be part of
the custom symbol, directly running this method is much faster than selecting
all of the entities and then running DrawingDoc::MakeCustomSymbol2.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DrawingDoc\DrawingDoc__CreateCustomSymbol.htm" >
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
<param name="Items" value="DrawingDoc Method$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DrawingDoc\DrawingDoc__CreateCustomSymbol.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
