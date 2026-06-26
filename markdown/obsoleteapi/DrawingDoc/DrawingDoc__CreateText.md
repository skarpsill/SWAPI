---
title: "DrawingDoc::CreateText"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateText.htm"
---

# DrawingDoc::CreateText

This
method is obsolete and has been superseded by DrawingDoc::CreateText2.

Description

This
method inserts text at the specified location in the current drawing.

Syntax (OLE Automation)

retval
= DrawingDoc.CreateText ( textString, textX, textY, textZ, textHeight,
textAngle)

(Table)=========================================================

| Input: | (BSTR)
textString | User
input text |
| --- | --- | --- |
| Input: | (double)
textX | X
text location in meters |
| Input: | (double)
textY | Y
text location in meters |
| Input: | (double)
textZ | Z
text location in meters |
| Input: | (double)
textHeight | Text
height in meters |
| Input: | (double)
textAngle | Text
angle for rotated text (in radians) |
| Return: | (BOOL)
retval | TRUE
if successful, FALSE if not |

Syntax (COM)

status
= DrawingDoc->CreateText ( textString, textX, textY, textZ, textHeight,
textAngle, &retval )

(Table)=========================================================

| Input: | (BSTR) textString | User input text |
| --- | --- | --- |
| Input: | (double) textX | X text location in meters |
| Input: | (double) textY | Y text location in meters |
| Input: | (double) textZ | Z text location in meters |
| Input: | (double) textHeight | Text height in meters |
| Input: | (double) textAngle | Text angle for rotated text (in radians) |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The location specifies the position of the upper-left
corner of the box containing the text with respect to the lower-left corner
of the drawing.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="DrawingDoc_Object$$**$$ZCreateNote$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\DrawingDoc\DrawingDoc__CreateText.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Note_Creation_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\DrawingDoc\DrawingDoc__CreateText.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
