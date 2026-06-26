---
title: "Note::GetTextFormatAtIndex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Note/Note__GetTextFormatAtIndex.htm"
---

# Note::GetTextFormatAtIndex

This method is obsolete and has been superseded
by[Annotation::GetTextFormat](sldworksAPI.chm::/Annotation/Annotation__GetTextFormat.htm).

Description

This method gets the specified text item's format.

Syntax (OLE Automation)

retval = Note.GetTextFormatAtIndex
( index )

(Table)=========================================================

| Input: | (long) index | Index of text item |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Dispatch pointer to the TextFormat object |

Syntax (COM)

status = Note->IGetTextFormatAtIndex
( index, &retval )

(Table)=========================================================

| Input: | (long) index | Index of text item |
| --- | --- | --- |
| Output: | (LPTEXTFORMAT) retval | Pointer to TextFormat object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Note\Note__GetTextFormatAtIndex.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
