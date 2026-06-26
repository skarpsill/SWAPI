---
title: "ModelDoc::CreateCircle2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateCircle2.htm"
---

# ModelDoc::CreateCircle2

This
method is obsolete and has been superseded by[ModelDoc2::CreateCircle2](../ModelDoc2/ModelDoc2__CreateCircle2.htm).

Description

This method creates a circle based on a center
point and a point on the circle.

Syntax (OLE Automation)

retval = ModelDoc.CreateCircle2 ( xc, yc, zc, xp,
yp, zp)

(Table)=========================================================

| Input: | (double) xc | X value of the circle center point, in meters |
| --- | --- | --- |
| Input: | (double) yc | Y value of the circle center point, in meters |
| Input: | (double) zc | Z value of the circle center point, in meters |
| Input: | (double) xp | X value of the point on the circle, in meters |
| Input: | (double) yp | Y value of the point on the circle, in meters |
| Input: | (double) zp | Z value of the point on the circle, in meters |
| Return: | (LPDISPATCH) retval | Pointer to the dispatch object of the circle
that was created |

Syntax (COM)

status = ModelDoc->ICreateCircle2 ( xc, yc, zc,
xp, yp, zp, &retval )

(Table)=========================================================

| Input: | (double) xc | X value of the circle center point, in meters |
| --- | --- | --- |
| Input: | (double) yc | Y value of the circle center point, in meters |
| Input: | (double) zc | Z value of the circle center point, in meters |
| Input: | (double) xp | X value of the point on the circle, in meters |
| Input: | (double) yp | Y value of the point on the circle, in meters |
| Input: | (double) zp | Z value of the point on the circle, in meters |
| Output: | (LPSKETCHSEGMENT) retval | Pointer to the circle that was created |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method creates a full circle in the active
2D sketch. If a sketch is not active, then a new sketch is created. You
can check for an active sketch using the ModelDoc::GetActiveSketch2 function.

For COM applications, the object pointer returned
from this function can be used to call any APIs on the SketchSegment interface.
The underlying SketchArc object can be obtained using QueryInterface on
the returned SketchSegment object.

OLE applications can simply define a new SketchSegment
or SketchArc object using the returned dispatch pointer. Visual Basic
applications will interpret the pointer for you automatically, so you
can use the returned object to call SketchSegment or SketchArc functions.

ModelDoc::SetAddToDB and ModelDoc::SetDisplayWhenAdded
increase performance during entity creation by adding entities directly
to the SolidWorks database.

[SetAddToDB](ModelDoc__SetAddToDB.htm)will also allow you to avoid some of the pecularities involved with creating
entities via the UI, such as inferencing, automatic relations, and snapping
to the grid. Adding entities directly to the database will also significantly
increase the performance of this API. When you are done creating entities,
it is important to[ModelDoc::SetAddToDB](ModelDoc__SetAddToDB.htm)(False),
to restore SolidWorks to its normal operating mode.

This API also works in conjunction with[ModelDoc::SetDisplayWhenAdded](ModelDoc__SetDisplayWhenAdded.htm).
If you have called[ModelDoc::SetAddToDB](ModelDoc__SetAddToDB.htm)(True),
additional performance can be gained by calling[ModelDoc::SetDisplayWhenAdded](ModelDoc__SetDisplayWhenAdded.htm)(False)
to disable immediate display of entities as they are added to the database.
When you are done creating all of your sketch entities, you will need
to redraw your document window (refer to[ModelDoc::GraphicsRedraw2](ModelDoc__GraphicsRedraw2.htm))
to see the entities you've added. You should also restore the original
display settings by calling[ModelDoc::SetDisplayWhenAdded](ModelDoc__SetDisplayWhenAdded.htm)(True).

To create a circle using a center point and radius,
refer to[ModelDoc::CreateCircleByRadius2](ModelDoc__CreateCircleByRadius2.htm).
To create a partial arc, refer to ModelDoc::CreateArc2.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc\ModelDoc__CreateCircle2.htm" >
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
<param name="Items" value="Create_Sketch_Line_With_Visual_Properties_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc\ModelDoc__CreateCircle2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
