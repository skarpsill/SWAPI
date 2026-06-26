---
title: "ModelDoc::InsertRadiateSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertRadiateSurface.htm"
---

# ModelDoc::InsertRadiateSurface

This method is obsolete
and has been superseded by[ModelDoc2::InsertRadiateSurface](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertRadiateSurface.htm).

Description

This method creates a radiate surface based on the selections.

Syntax (OLE Automation)

void ModelDoc.InsertRadiateSurface(
distance, flipDir, tangentPropagate )

(Table)=========================================================

| Input: | (double) distance | Distance to extend the surface |
| --- | --- | --- |
| Input: | (BOOL) flipDir | TRUE to flip the direction; by default the direction is out from the
center of the face |
| Input: | (BOOL) tangentPropagate | TRUE to propagate the surface along tangent faces, FALSE limits the
surface to the selected face. |

Syntax (COM)

status = ModelDoc->InsertRadiateSurface(
distance, flipDir, tangentPropagate )

(Table)=========================================================

| Input: | (double) distance | Distance to extend the surface |
| --- | --- | --- |
| Input: | (BOOL) flipDir | TRUE to flip the direction; by default the direction is out from the
center of the face |
| Input: | (BOOL) tangentPropagate | TRUE to propagate the surface along tangent faces, FALSE limits the
surface to the selected face. |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is the same as interactively creating a Radiate Surface
by selectingInsert,
Reference Geometry, Radiate Surface.
See SolidWorks Help for more information about what entities are
valid for selection.

To use this method, make the selections usingSelectByMark
with mark of 2.

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
<param name="Items" value="ModelDoc_Object$$**$$ZCreateRefSurface$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__InsertRadiateSurface.htm" >
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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Entity::SelectByMark$$**$$ModelDoc::SelectByMark$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__InsertRadiateSurface.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
