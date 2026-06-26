---
title: "Sketch::ModelToSketchXform"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sketch/Sketch__ModelToSketchXform.htm"
---

# Sketch::ModelToSketchXform

This property is obsolete and has been superseded
by[Sketch::ModelToSketchTransform](sldworksAPI.chm::/Sketch/Sketch__ModelToSketchTransform.htm).

Description

This property contains the model-to-sketch transform for the sketch
member. As indicated by its name, this method allows you to go from the
model to the sketch. For example, if you have a point located in model
space coordinates, then you can multiply (Point x Matrix) to give you
its coordinates in terms of this sketch.

Syntax (OLE Automation)

xform = Sketch.ModelToSketchXform (VB
Get property)

xform = Sketch.GetModelToSketchXform
( ) (C++ Get property)

(Table)=========================================================

| Property: | (VARIANT) xform | VARIANT of type SafeArray of 13 doubles |
| --- | --- | --- |

Syntax (Com)

status = Sketch->get_IModelToSketchXform(
xform )

(Table)=========================================================

| Property: | (double*) xform | Pointer to an array of 13 doubles |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The transform is returned as an array
of 13 doubles. The first 9 are elements of 3x3 matrix, the next three
define translation, and the last one is scaling.

This transformation matrix is returned in column-major order. For a
description of a column-major type of matrix, see ModelView::Orientation2,
which describes the layout of a 4x4 column-major matrix.

The portion of this matrix representing the translation
vector should be interpreted in terms of sketch space. In other words,
the translation is in relation to the XYZ coordinate system of the sketch.

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
<param name="Items" value="Sketch_Object$$**$$ZGetInfoSketch$$**$$ZXform$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Sketch\Sketch__ModelToSketchXform.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
