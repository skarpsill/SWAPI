---
title: "DrawingDoc::InsertNewNote"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__InsertNewNote.htm"
---

# DrawingDoc::InsertNewNote

This method is obsolete and has been superseded
by[DrawingDoc::InsertNewNote2](sldworksAPI.chm::/DrawingDoc/DrawingDoc__InsertNewNote2.htm).

Description

This method creates a new note in this drawing.

Syntax (OLE Automation)

void DrawingDoc.InsertNewNote ( text,
noLeader, balloonNote, bentLeader, arrowStyle, leaderSide)

(Table)=========================================================

| Input: | (BSTR) text | Text string to be put in the note |
| --- | --- | --- |
| Input: | (BOOL) noLeader | TRUE does not add a leader line, FALSE does |
| Input: | (BOOL) balloonNote | TRUE adds balloon, FALSE does not |
| Input: | (BOOL) bentLeader | TRUE adds a bent leader line, FALSE does not |
| Input: | (short) arrowStyle | Arrowhead type as defined in swArrowStyle_e |
| Input: | (short) leaderSide | Leader line side as defined in swLeaderSide_e |

Syntax (COM)

status = DrawingDoc->InsertNewNote
( text, noLeader, balloonNote, bentLeader, arrowStyle, leaderSide )

(Table)=========================================================

| Input: | (BSTR) text | Text string to be put in the note |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) noLeader | TRUE does not add a leader line, FALSE does |
| Input: | (VARIANT_BOOL) balloonNote | TRUE adds a balloon, FALSE does not |
| Input: | (VARIANT_BOOL) bentLeader | TRUE adds a bent leader line, FALSE does not |
| Input: | (short) arrowStyle | Arrowhead type as defined in swArrowStyle_e |
| Input: | (short) leaderSide | Leader line side as defined in swLeaderSide_e |
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="DrawingDoc_Object$$**$$ZCreateNote$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\DrawingDoc\DrawingDoc__InsertNewNote.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
