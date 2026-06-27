---
title: "DrawingDoc::InsertCustomSymbol2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__InsertCustomSymbol2.htm"
---

# DrawingDoc::InsertCustomSymbol2

This method is obsolete and has been superseded
byBlockDefinition::InsertInstanceorDrawingDoc::InsertBlock.

Description

This method inserts a new custom symbol at
the selected location without adding the custom symbol to the selection
list when the command is finished.

Syntax (OLE Automation)

retval = DrawingDoc.InsertCustomSymbol2 ( fileName
)

(Table)=========================================================

| Input: | (BSTR) fileName | File name of the custom symbol |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to the newly created custom symbol |

Syntax (COM)

status = DrawingDoc->IInsertCustomSymbol2 ( fileName,
&retval )

Parameters Table Start

(Table)=========================================================

| Input: | (BSTR) fileName | Filename of the custom symbol |
| --- | --- | --- |
| Output: | (LPCUSTOMSYMBOL) retval | Pointer to the newly created custom symbol |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method depends on something
being selected before it is called. If nothing is selected, SolidWorks
takes no action and returns NULL.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DrawingDoc\DrawingDoc__InsertCustomSymbol2.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DrawingDoc\DrawingDoc__InsertCustomSymbol2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
