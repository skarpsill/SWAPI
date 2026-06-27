---
title: "DrawingDoc::CreateFlatPatternViewFromModelView"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateFlatPatternViewFromModelView.htm"
---

# DrawingDoc::CreateFlatPatternViewFromModelView

This method is obsolete and has been superseded
by[DrawingDoc::CreateFlatPatternViewFromModelView2](DrawingDoc__CreateFlatPatternViewFromModelView2.htm).

Description

This method creates a flat pattern view from
a model view at the specified location.

Syntax (OLE Automation)

retval = DrawingDoc.CreateFlatPatternViewFromModelView
( modelName, configName, locX, locY, locZ )

(Table)=========================================================

| Input: | (BSTR) modelName | Name of the model in the flat pattern view |
| --- | --- | --- |
| Input: | (BSTR) configName | Name of the configuration |
| Input: | (double) locX | X location of view |
| Input: | (double) locY | Y location of view |
| Input: | (double) locZ | Z location of view |
| Return: | (BOOL) retval | TRUE if the view was successfully created, FALSE
if not |

Syntax (COM)

status = DrawingDoc->CreateFlatPatternViewFromModelView
( modelName, configName, locX, locY, locZ, &retval )

(Table)=========================================================

| Input: | (BSTR) modelName | Name of the model in the flat pattern view |
| --- | --- | --- |
| Input: | (BSTR) configName | Name of the configuration |
| Input: | (double) locX | X location of view |
| Input: | (double) locY | Y location of view |
| Input: | (double) locZ | Z location of view |
| Output: | (VARIANT_BOOL) retval | TRUE if the view was successfully created, FALSE
if not |
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\DrawingDoc\DrawingDoc__CreateFlatPatternViewFromModelView.htm" >
<param name="_ID" value="RelatedTopic0" >
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="DrawingDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\DrawingDoc\DrawingDoc__CreateFlatPatternViewFromModelView.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
