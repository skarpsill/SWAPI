---
title: "ModelDoc::InsertProjectedSketch2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc_InsertProjectedSketch2.htm"
---

# ModelDoc::InsertProjectedSketch2

This method is obsolete and has been superseded
by[ModelDoc2::InsertProjectedSketch2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertProjectedSketch2.htm).

Description

This method projects a closed set of entities
from the selected sketch onto the selected planar object.

Syntax (OLE Automation)

retval = ModelDoc.InsertProjectedSketch2 (reverse)

(Table)=========================================================

| Input: | (long) reverse | Pass 1 to reverse the projected direction |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created
Feature object or NULL
if the operation fails |

Syntax (COM)

status = ModelDoc->IInsertProjectedSketch2 (reverse, &retval )

(Table)=========================================================

| Input: | (long) reverse | Pass 1 to reverse the projected direction |
| --- | --- | --- |
| Output: | (LPFEATURE) retval | Pointer to the newly created Feature object or
NULL if the operation fails |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can reverse the direction in which the curve
is projected. This is only necessary when the selected face wraps around
the plane of the curve. For example, if the sketch that is being projected
is surrounded by a cylindrical face, then two possible projections exist.
Use the reverse argument to toggle the direction based on the normal vector
of the sketch. The default direction is along the sketch normal.

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
<param name="Items" value="ModelDoc_Object$$**$$ZCreateSketchEntity$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc_InsertProjectedSketch2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
