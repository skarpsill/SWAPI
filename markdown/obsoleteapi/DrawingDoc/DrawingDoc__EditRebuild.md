---
title: "DrawingDoc::EditRebuild"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__EditRebuild.htm"
---

# DrawingDoc::EditRebuild

This method is obsolete and has been superseded by[ModelDoc2::EditRebuild3](sldworksAPI.chm::/ModelDoc2/ModelDoc2__EditRebuild3.htm).

Description

This method rebuilds the drawing.

Syntax (OLE Automation)

void
DrawingDoc.EditRebuild ()

Syntax (COM)

status
= DrawingDoc->EditRebuild ( )

(Table)=========================================================

| Return: | (HRESULT)
status | S_OK
if successful |
| --- | --- | --- |

Remarks

There are certain situations in which SolidWorks blocks this command.
For example, if the user is interactively editing the properties of a
dimension, SolidWorks blocks this method because calling it invalidates
all of the pointers in the document. If DrawingDoc::EditRebuild is not
blocked, closing theDimension-Propertiesdialog box might cause problems because the dialog box looks for the original
dimension pointer.

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
<param name="_CURRENTFILEPATH" value="D:\sw2003\DrawingDoc\DrawingDoc__EditRebuild.htm" >
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
<param name="Items" value="Change_Dimension_Example$$**$$Plane_Creation_and_Naming_Example$$**$$Change_Note_Text_Example$$**$$Close_Document_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\sw2003\DrawingDoc\DrawingDoc__EditRebuild.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
