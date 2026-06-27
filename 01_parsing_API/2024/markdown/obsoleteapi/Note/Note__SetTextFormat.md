---
title: "Note::SetTextFormat"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Note/Note__SetTextFormat.htm"
---

# Note::SetTextFormat

This method is obsolete and has been superseded
by[Annotation::SetTextFormat](sldworksAPI.chm::/Annotation/Annotation__SetTextFormat.htm).

Description

This method sets the text format
parameters.

Syntax (OLE Automation)

retval = Note.SetTextFormat ( useDocFormat,
textFormat )

(Table)=========================================================

| Input: | (long) useDocFormat | Controls whether the note uses the documents text format or the textFormat
argument values |
| --- | --- | --- |
| Input: | (LPDISPATCH) textFormat | Formatting values (see Remarks ) |
| Return: | (BOOL) retval | TRUE if successfully set, FALSE if not |

Syntax (COM)

status = Note->ISetTextFormat (
useDocFormat, textFormat, &retval )

(Table)=========================================================

| Input: | (long) useDocFormat | Controls whether the note uses the documents text format or the textFormat
argument values |
| --- | --- | --- |
| Input: | (LPTEXTFORMAT) textFormat | Formatting values (see Remarks ) |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully set, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The note's text format is set to the document's text format if useDocFormat
is 1 or to the format specified in the textFormat argument if useDocFormat
is 0.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\Note\Note__SetTextFormat.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
