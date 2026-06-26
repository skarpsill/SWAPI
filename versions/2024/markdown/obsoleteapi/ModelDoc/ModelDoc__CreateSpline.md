---
title: "ModelDoc::CreateSpline"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateSpline.htm"
---

# ModelDoc::CreateSpline

This
method is obsolete and has been superseded by[ModelDoc2::CreateSpline](../ModelDoc2/ModelDoc2__CreateSpline.htm).

Description

This method creates a spline passing through
the given points.

Syntax (OLE Automation)

retval = ModelDoc.CreateSpline (pointData)

(Table)=========================================================

| Input: | (VARIANT) pointData | Set of X,Y,Z point coordinates to use in creating
the spline |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to the Dispatch object of the spline
that was created |

Syntax (COM)

status = ModelDoc->ICreateSpline ( pointCount,
pointData, &retval )

(Table)=========================================================

| Input: | (long) pointCount | Number of points in the pointData array |
| --- | --- | --- |
| Input: | (double*) pointData | Set of X,Y,Z point coordinates to use in creating
the spline, |
| Output: | (LPSKETCHSEGMENT) retval | Pointer to the spline that was created |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method creates a spline in the active 2D sketch.
If a sketch is not active, then a new sketch is created. You can check
for an active sketch using ModelDoc::GetActiveSketch2.

If you are creating a sketch spline from a macro, then you must use
ModelDoc::SketchSpline. You cannot use ModelDoc::CreateSpline because
it requires an array of points.

The pointData array is a set of, at least two X,
Y, Z values. The X value for the start point of the spline is pointData[0],
the Y value for the start point is pointData[1], and the Z value for the
start point is pointData[2]. The X value for the next point is pointData[3],
and so on. For the COM interface, the total number of points in the array
must be passed in. For the OLE interface, the total number of points is
determined automatically within SolidWorks, by taking the UBound of the
pointData VARIANT, and dividing by 3, so dimension that array correctly.

For COM applications, the object pointer returned
from this method can be used to call any of the SketchSegment functions.
The underlying SketchSpline object can be obtained using QueryInterface
on the returned SketchSegment object.

OLE applications can define a new SketchSegment
or SketchSpline object using the returned dispatch pointer. Visual Basic
applications interpret the pointer for you automatically, so you can use
the returned object to call SketchSegment or SketchEllipse functions.

This method does not work with ModelDoc::SetAddToDB
or ModelDoc::SetDisplayWhenAdded. It always adds the spline directly to
the database, as if ModelDoc::SetAddToDB(True) was in effect. You must
redraw your document window to see the entities that you added, as if
ModelDoc::SetDisplayWhenAdded(False) was in effect.

In 2D sketches, SolidWorks ignores the Z value
in pointData.

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
<param name="Items" value="ModelDoc_Object$$**$$ZCreateSketchEntity$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc\ModelDoc__CreateSpline.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
