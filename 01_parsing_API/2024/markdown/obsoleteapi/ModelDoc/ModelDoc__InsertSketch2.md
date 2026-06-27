---
title: "ModelDoc::InsertSketch2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertSketch2.htm"
---

# ModelDoc::InsertSketch2

This method is obsolete and has been superseded by[ModelDoc2::InsertSketch2](../ModelDoc2/ModelDoc2__InsertSketch2.htm).

Description

This method creates or exits a sketch. If a
sketch is not currently active, then this method will create a sketch
on the selected planar entity (for example, face, plane, and so on). If
a sketch is currently active, then calling this method will exit you from
the sketch.

Syntax (OLE Automation)

void ModelDoc.InsertSketch2
( updateEditRebuild )

(Table)=========================================================

| Input: | (VARIANT_BOOL) updateEditRebuild | TRUE to update the model, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->InsertSketch2
( updateEditRebuild )

(Table)=========================================================

| Input: | (VARIANT_BOOL) updateEditRebuild | TRUE to update the model, FALSE otherwise |
| --- | --- | --- |
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
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDoc\ModelDoc__InsertSketch2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
