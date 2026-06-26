---
title: "DrawingDoc::MakeBlockDefinition"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__MakeBlockDefinition.htm"
---

# DrawingDoc::MakeBlockDefinition

This
method is obsolete and has been superseded by SkethcManager::MakeSketchBlockFromFile , SketchManager::MakeSketchBlockSelected ,
and SketchManager::MakeSketchBlockFromSketch .

Description

This method makes a block definition from the
selected entities.

Syntax (OLE Automation)

retval = DrawingDoc.MakeBlockDefinition ( Name, XRefFileName,
Instance )

(Table)=========================================================

| Input: | (BSTR) Name | Block definition name |
| --- | --- | --- |
| Input: | (BSTR) XRefFileName | Name of the file that the block definition references |
| Input: | (VARIANT_BOOL) Instance | TRUE creates an instance, FALSE does not |
| Output: | (LPBLOCKDEFINITION) retval | Pointer to the new block definition |

Syntax (COM)

status = DrawingDoc->MakeBlockDefinition ( Name,
XRefFileName, Instance, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (BSTR) Name | Block definition name |
| --- | --- | --- |
| Input: | (BSTR) XRefFileName | Name of the file that the block definition references |
| Input: | (VARIANT_BOOL) Instance | TRUE creates an instance, FALSE does not |
| Output: | (LPBLOCKDEFINITION) retval | Pointer to the new block definition |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is similar to
the DrawingDoc::CreateBlockDefinition method except that instead of creating
a block definition from the specified entities, DrawingDoc::MakeBlockDefinition
creates a block definition from the selected entities.

If you have the pointers to
the entities for the block definition, running DrawingDoc::CreateBlockDefinition
should be faster than selecting all of the entities and then running DrawingDoc::MakeBlockDefinition
because of the time spent having to select the entities.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DrawingDoc\DrawingDoc__MakeBlockDefinition.htm" >
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
<param name="Items" value="DrawingDoc$$**$$BlockDefinition_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DrawingDoc\DrawingDoc__MakeBlockDefinition.htm" >
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
<param name="Items" value="EXMakeBlockDefinition$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DrawingDoc\DrawingDoc__MakeBlockDefinition.htm" >
<param name="_ID" value="RelatedTopic5" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
