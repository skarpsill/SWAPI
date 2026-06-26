---
title: "ModelDoc::CreateEllipticalArc2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateEllipticalArc2.htm"
---

# ModelDoc::CreateEllipticalArc2

This
method is obsolete and has been superseded by[ModelDoc2::CreateEllipticalArc2](../ModelDoc2/ModelDoc2__CreateEllipticalArc2.htm).

Description

This method creates a partial ellipse given
a center point, two points that specify the major and minor axis and two
points that define the elliptical start and end points.

Syntax (OLE Automation)

retval = ModelDoc.CreateEllipticalArc2 ( centerX,
centerY, centerZ, majorX, majorY, majorZ, minorX, minorY, minorZ, startX,
startY, startZ, endX, endY, endZ)

(Table)=========================================================

| Input: | (double) centerX | X value for the ellipse center point |
| --- | --- | --- |
| Input: | (double) centerY | Y value for the ellipse center point |
| Input: | (double) centerZ | Z value for the ellipse center point |
| Input: | (double) majorX | X value for a point on the ellipse and on the major axis |
| Input: | (double) majorY | Y value for a point on the ellipse and on the major axis |
| Input: | (double) majorZ | Z value for a point on the ellipse and on the major axis |
| Input: | (double) minorX | X value for a point on the ellipse and on the minor axis |
| Input: | (double) minorY | Y value for a point on the ellipse and on the minor axis |
| Input: | (double) minorZ | Z value for a point on the ellipse and on the minor axis |
| Input: | (double) startX | X value for counter clockwise elliptical arc start point |
| Input: | (double) startY | Y value for counter clockwise elliptical arc start point |
| Input: | (double) startZ | Z value for counter clockwise elliptical arc start point |
| Input: | (double) endX | X value for counter clockwise elliptical arc end point |
| Input: | (double) endY | Y value for counter clockwise elliptical arc end point |
| Input: | (double) endZ | Z value for counter clockwise elliptical arc end point |
| Return: | (LPDISPATCH) retval | Pointer to theDispatch object of the ellipse that was created |

Syntax (COM)

status = ModelDoc->ICreateEllipticalArc2 ( centerX,
centerY, centerZ, majorX, majorY, majorZ, minorX, minorY, minorZ, startX,
startY, startZ, endX, endY, endZ, &retval )

(Table)=========================================================

| Input: | (double) centerX | X value for the ellipse center point |
| --- | --- | --- |
| Input: | (double) centerY | Y value for the ellipse center
point |
| Input: | (double) centerZ | Z value for the ellipse center
point |
| Input: | (double) majorX | X value for a point on the ellipse and on the
major axis |
| Input: | (double) majorY | Y value for a point on the
ellipse and on the major axis |
| Input: | (double) majorZ | Z value for a point on the
ellipse and on the major axis |
| Input: | (double) minorX | X value for a point on the ellipse and on the
minor axis |
| Input: | (double) minorY | Y value for a point on the
ellipse and on the minor axis |
| Input: | (double) minorZ | Z value for a point on the
ellipse and on the minor axis |
| Input: | (double) startX | X value for counter clockwise elliptical arc
start point |
| Input: | (double) startY | Y value for counter clockwise
elliptical arc start point |
| Input: | (double) startZ | Z value for counter clockwise
elliptical arc start point |
| Input: | (double) endX | X value for counter clockwise elliptical arc
end point |
| Input: | (double) endY | Y value for counter clockwise
elliptical arc end point |
| Input: | (double) endZ | Z value for counter clockwise
elliptical arc end point |
| Output: | (LPSKETCHSEGMENT) retval | Pointer to the ellipse that was created |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method creates a partial ellipse in the active
2D sketch. If a sketch is not active, then a new sketch will be created.
You can check for an active sketch using the ModelDoc::GetActiveSketch2
function.

For COM applications, the object pointer returned
from this function can be used to call any APIs on the SketchSegment interface.
The underlying SketchEllipse object can be obtained using QueryInterface
on the returned SketchSegment object.

OLE applications can define a new ISketchSegment
or ISketchEllipse object using the returned dispatch pointer. Visual Basic
applications will interpret the pointer for you automatically, so you
can use the returned object to call SketchSegment or SketchEllipse functions.

ModelDoc::SetAddToDB and ModelDoc::SetDisplayWhenAdded
increase performance during entity creation by adding entities directly
to the SolidWorks database.

ModelDoc::SetAddToDB will also allow you to avoid
some of the peculiarities involved with creating entities via the user
interface, such as inferencing, automatic relations, and snapping to the
grid. Adding entities directly to the database will also significantly
increase the performance of this API. When you are done creating entities,
it is important to callkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ModelDoc::SetAddToDB(False),
to restore SolidWorks to its normal operating mode.

This API also works in conjunction with ModelDoc::SetDisplayWhenAdded.
If you have called ModelDoc::SetAddToDB(True), additional performance
can be gained by calling ModelDoc::SetDisplayWhenAdded(False) to disable
immediate display of entities as they are added to the database. When
you are done creating all of your sketch entities, you will need to redraw
your document window (refer to ModelDoc::GraphicsRedraw2) to see the entities
you've added. You should also restore the original display settings by
calling ModelDoc::SetDisplayWhenAdded(True).

To create a complete ellipse, see ModelDoc::CreateEllipse2.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc\ModelDoc__CreateEllipticalArc2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
