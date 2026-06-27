---
title: "Note::GetTextPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Note/Note__GetTextPoint.htm"
---

# Note::GetTextPoint

This method is obsolete and has been superseded
by[Note::GetTextPoint2](sldworksAPI.chm::/Note/Note__GetTextPoint2.htm).

Description

This method returns the note's text reference point (the note origin).
This is the upper-left corner of the bounding rectangle.

Syntax (OLE Automation)

retval = Note.GetTextPoint ()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = Note->IGetTextPoint ( retval
)

(Table)=========================================================

| Output: | (double*) retval | Pointer to array of doubles (see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Format of return information is the following array of doubles:

- retval[0]
  = x coordinate of text reference point
- retval[1]
  = y coordinatekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}of
  text reference point
- retval[2]
  = z coordinatekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}of
  text reference point

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
<param name="Items" value="Note_Object$$**$$ZGetInfoNote$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\Note\Note__GetTextPoint.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
