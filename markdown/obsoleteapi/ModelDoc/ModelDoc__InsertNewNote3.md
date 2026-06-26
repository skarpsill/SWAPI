---
title: "ModelDoc::InsertNewNote3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertNewNote3.htm"
---

# ModelDoc::InsertNewNote3

This
method is obsolete and has been superseded by[ModelDoc2::InsertNewNote3](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertNewNote3.htm).

Description

This method creates a new note.

Syntax (OLE Automation)

void ModelDoc.InsertNewNote3
( upperText, noLeader, bentLeader, arrowStyle, leaderSide, angle, balloonStyle,
balloonFit, smartArrow )

(Table)=========================================================

| Input: | (BSTR) upperText | Upper-text string to be put in the note |
| --- | --- | --- |
| Input: | (BOOL) noLeader | TRUE for no leader line, FALSE otherwise |
| Input: | (BOOL) bentLeader | TRUE for a bent leader line, FALSE otherwise |
| Input: | (short) arrowStyle | Arrowhead type as defined in swArrowStyle_e |
| Input: | (short) leaderSide | Leader-line side as defined in swLeaderSide_e |
| Input: | (double) angle | Text angle |
| Input: | (short) balloonStyle | Balloon style type as defied in swBalloonStyle_e |
| Input: | (short) balloonFit | Balloon fit type as defined in swBalloonFit_e |
| Input: | (BOOL) smartArrow | If TRUE, then the arrow style specified in Options,
Detailing is used for the arrows, if FALSE then the arrowStyle
argument is used |

Syntax (COM)

status = ModelDoc->InsertNewNote3
( upperText, noLeader, bentLeader, arrowStyle, leaderSide, angle, balloonStyle,
balloonFit, smartArrow )

(Table)=========================================================

| Input: | (BSTR) upperText | Uppe- text string to be put in the note |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) noLeader | TRUE for no leade rline, FALSE otherwise |
| Input: | (VARIANT_BOOL) bentLeader | TRUE for a bent leader line, FALSE otherwise |
| Input: | (short) arrowStyle | Arrowhead type as defined in swArrowStyle_e |
| Input: | (short) leaderSide | Leade-line side as defined in swLeaderSide_e |
| Input: | (double) angle | Text angle |
| Input: | (short) balloonStyle | Balloon style type as defined in swBalloonStyle_e |
| Input: | (short) balloonFit | Balloon fit type as defined in swBalloonFit_e |
| Input: | (VARIANT_BOOL) smartArrow | If TRUE, then the arrow style specified in Options,
Detailing is used for the arrows, if FALSE then the arrowStyle
argument is used |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
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
<param name="Items" value="ModelDoc_Object$$**$$ZCreateNote$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__InsertNewNote3.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
