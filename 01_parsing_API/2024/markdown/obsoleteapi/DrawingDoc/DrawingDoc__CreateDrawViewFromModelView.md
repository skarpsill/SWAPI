---
title: "DrawingDoc::CreateDrawViewFromModelView"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateDrawViewFromModelView.htm"
---

# DrawingDoc::CreateDrawViewFromModelView

This method is obsolete and has been superseded
by[DrawingDoc::CreateDrawViewFromModelView2](DrawingDoc__CreateDrawViewFromModelView2.htm).

Description

This
method creates a drawing view on the current drawing sheet using the specified
model view.

Syntax (OLE Automation)

retval
= DrawingDoc.CreateDrawViewFromModelView ( modelName, viewName, locX,
locY, locZ)

(Table)=========================================================

| Input: | (BSTR)
modelName | Name
of the document to create the view from (including the .sldprt or .sldasm
extension) |
| --- | --- | --- |
| Input: | (BSTR)
viewName | Name
of the model view to create the view from (see Remarks ) |
| Input: | (double)
locX | X-location
of drawing view center in meters |
| Input: | (double)
locY | Y-location
of drawing view center in meters |
| Input: | (double)
locZ | Z-location
of drawing view center in meters |
| Return: | (BOOL)
retval | TRUE
if successful, FALSE if not |

Syntax (COM)

status = DrawingDoc->CreateDrawViewFromModelView
( modelName, viewName, locX, locY, locZ, &retval )

(Table)=========================================================

| Input: | (BSTR) modelName | Name of the document to create the view from (including the .sldprt
or .sldasm extension) |
| --- | --- | --- |
| Input: | (BSTR) viewName | Name of the model view to create the view from (see Remarks ) |
| Input: | (double) locX | X-location of drawing view center in meters |
| Input: | (double) locY | Y-location of drawing view center in meters |
| Input: | (double) locZ | Z-location of drawing view center in meters |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |
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
<param name="Items" value="DrawingDoc_Object$$**$$ZCreateDwgView$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\DrawingDoc\DrawingDoc__CreateDrawViewFromModelView.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
