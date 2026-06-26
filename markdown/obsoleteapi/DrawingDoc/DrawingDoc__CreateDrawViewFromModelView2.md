---
title: "DrawingDoc::CreateDrawViewFromModelView2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateDrawViewFromModelView2.htm"
---

# DrawingDoc::CreateDrawViewFromModelView2

This method is obsolete and has been superseded
by[DrawingDoc::CreateDrawViewFromModelView3](sldworksAPI.chm::/DrawingDoc/DrawingDoc__CreateDrawViewFromModelView3.htm).

Description

This method creates a drawing
view on the current drawing sheet using the specified model view.

Syntax (OLE Automation)

retval = DrawingDoc.CreateDrawViewFromModelView2
( modelName, viewName, locX, locY, locZ)

(Table)=========================================================

| Input: | (BSTR) modelName | Name of the document from which
to create the view (including the .sldprt or .sldasm filename extension) |
| --- | --- | --- |
| Input: | (BSTR) viewName | Name of the model view from which to create the
view (see Remarks ) |
| Input: | (double) locX | x location of drawing view center
in meters |
| Input: | (double) locY | y location of drawing view center in meters |
| Input: | (double) locZ | z location of drawing view center in meters |
| Output: | (LPVIEW) retval | Pointer to the newly create View object |

Syntax (COM)

status = DrawingDoc->CreateDrawViewFromModelView2
( modelName, viewName, locX, locY, locZ, &retval)

Parameters Table Start

(Table)=========================================================

| Input: | (BSTR) modelName | Name of the document from which to create the
view (including the .sldprt or .sldasm filename extension) |
| --- | --- | --- |
| Input: | (BSTR) viewName | Name of the model view from which
to create the view (see Remarks ) |
| Input: | (double) locX | x location of
drawing view center in meters |
| Input: | (double) locY | y location of
drawing view center in meters |
| Input: | (double) locZ | z location of
drawing view center in meters |
| Output: | (LPVIEW) retval | Pointer to the newly create View
object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method places the center of the view at the
specified location.

The modelName must be an open document in the current
SolidWorks session. The viewName must exactly match the name of the model
view. For example, the names of the standard views begin with an asterisk.
This asterisk is part of the view name and must be included (for example,
"*Front").

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
<param name="Items" value="ZReleaseNotes005$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\DrawingDoc\DrawingDoc__CreateDrawViewFromModelView2.htm" >
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
<param name="Items" value="DrawingDoc_Object$$**$$ZCreateDwgView$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\DrawingDoc\DrawingDoc__CreateDrawViewFromModelView2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
