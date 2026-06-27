---
title: "Note::SetTextFormatAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Note/Note__SetTextFormatAtIndex.htm"
---

# Note::SetTextFormatAtIndex

This method is obsolete and has been superseded
by[Annotation::SetTextFormat](sldworksAPI.chm::/Annotation/Annotation__SetTextFormat.htm).

Description

This method sets the specified
text item's format.

Syntax (OLE Automation)

void Note.SetTextFormatAtIndex ( index,
textFormat )

(Table)=========================================================

| Input: | (long) index | Index position of the text |
| --- | --- | --- |
| Input: | (LPDISPATCH) textFormat | Dispatch pointer to the TextFormat object containing the desired settings |

Syntax (COM)

status = Note->ISetTextFormatAtIndex
( index, textFormat )

(Table)=========================================================

| Input: | (long ) index | Index position of the text |
| --- | --- | --- |
| Input: | (LPTEXTFORMAT )textFormat | Pointer to the TextFormat object containing the desired settings |
| Return: | (HRESULT )status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Note_Object$$**$$ZGetTextFormat$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\Note\Note__SetTextFormatAtIndex.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
