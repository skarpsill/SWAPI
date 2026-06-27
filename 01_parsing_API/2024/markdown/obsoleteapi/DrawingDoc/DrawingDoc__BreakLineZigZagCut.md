---
title: "DrawingDoc::BreakLineZigZagCut"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__BreakLineZigZagCut.htm"
---

# DrawingDoc::BreakLineZigZagCut

This
method is obsolete and has been superseded by BreakLine::Style .

Description

This method toggles the break line style to zig-zag or changes the selected
break line to zig-zag style.

Syntax (OLE Automation)

void DrawingDoc.BreakLineZigZagCut
()

Syntax (COM)

status = DrawingDoc->BreakLineZigZagCut
( )

(Table)=========================================================

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

To insert break lines to a drawing view, use DrawingDoc::InsertBreakHorizontal
or DrawingDoc::InsertBreakVertical. You can then customize the break by
dragging and repositioning the break lines. Use the DrawingDoc::BreakView
method to actually create the broken drawing view.

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
<param name="Items" value="DrawingDoc_Object$$**$$ZModifyView$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\DrawingDoc\DrawingDoc__BreakLineZigZagCut.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
