---
title: "DrawingDoc::InsertMultiJogLeader2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__InsertMultiJogLeader2.htm"
---

# DrawingDoc::InsertMultiJogLeader2

This method is obsolete and has been superseded
by[Drawingdoc::InsertMultiJogLeader3](sldworksAPI.chm::/DrawingDoc/DrawingDoc__InsertMultiJogLeader3.htm).

Description

This method inserts a multi-jog
leader in this drawing at the specified points.

Syntax (OLE Automation)

lpLeaderDisp = DrawingDoc.InsertMultiJogLeader2 (
points)

(Table)=========================================================

| Input: | (VARIANT) points | VARIANT of type SafeArray of
points |
| --- | --- | --- |
| Output: | (LPDISPATCH) lpLeaderDisp | Dispatch pointer to the Leader object |

Syntax (COM)

status = DrawingDoc->IInsertMultiJogLeader2 (
pointsCount, points, &lpLeader)

Parameters Table Start

(Table)=========================================================

| Input: | (long) pointsCount | Number of points |
| --- | --- | --- |
| Property: | (LPMATHPOINT) points | Pointer to the MathPoint object of size pointsCount |
| Output: | (LPLEADER) lpLeader | Pointer to the Leader object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="Items" value="ZReleaseNotes004Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\DrawingDoc\DrawingDoc__InsertMultiJogLeader2.htm" >
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
<param name="Items" value="DrawingDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\DrawingDoc\DrawingDoc__InsertMultiJogLeader2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
