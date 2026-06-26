---
title: "DrawingDoc::ForceRebuild"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__ForceRebuild.htm"
---

# DrawingDoc::ForceRebuild

This
method is obsolete and has been superseded by[ModelDoc2::ForceRebuild3](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ForceRebuild3.htm).

Description

This method forces a rebuild of the drawing.

Syntax (OLE Automation)

void
DrawingDoc.ForceRebuild ( )

Syntax (COM)

status
= DrawingDoc->ForceRebuild ( )

(Table)=========================================================

| Return: | (HRESULT)
status | S_OK
if successful |
| --- | --- | --- |

Remarks

This method is equivalent to interactively pressing
theCtrlandQkeys.

This method rebuilds the entire model whether or
not it needs to be rebuilt, which can be very time consuming.

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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="DrawingDoc_Object$$**$$ZEditRebuild$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\sw2003\DrawingDoc\DrawingDoc__ForceRebuild.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
