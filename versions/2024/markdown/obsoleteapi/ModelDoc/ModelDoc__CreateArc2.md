---
title: "ModelDoc::CreateArc2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateArc2.htm"
---

# ModelDoc::CreateArc2

This
method is obsolete and has been superseded by[ModelDoc2::CreateArc2](../ModelDoc2/ModelDoc2__CreateArc2.htm).

Description

This method creates an arc based on a center
point, a start point,kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}an
end point, and a direction.

Syntax (OLE Automation)

retval = ModelDoc.CreateArc2 ( xc, yc, zc, xp1, yp1,
zp1, xp2, yp2, zp2, direction )

(Table)=========================================================

| Input: | (double) xc | X value of the circle center point, in meters |
| --- | --- | --- |
| Input: | (double) yc | Y value of the circle center point, in meters |
| Input: | (double) zc | Z value of the circle center point, in meters |
| Input: | (double) xp1 | X value of the start point of the arc, in meters |
| Input: | (double) yp1 | Y value of the start point of the arc, in meters |
| Input: | (double) zp1 | Z value of the start point of the arc, in meters |
| Input: | (double) xp2 | X value of the end point of the arc, in meters |
| Input: | (double) yp2 | Y value of the end point of the arc, in meters |
| Input: | (double) zp2 | Z value of the end point of the arc, in meters |
| Input: | (short) direction | +1 : Go from the start point to the end point
in a counter-clockwise direction. -1 : Go from the start point to the end point
in a clockwise direction |
| Return: | (LPDISPATCH) retval | Pointer to the dispatch object of the arc that
was created |

Syntax (COM)

status = ModelDoc->ICreateArc2 ( xc, yc, zc, xp1,
yp1, zp1, xp2, yp2, zp2, direction, &retval )

(Table)=========================================================

| Input: | (double) xc | X value of the circle center point, in meters |
| --- | --- | --- |
| Input: | (double) yc | Y value of the circle center point, in meters |
| Input: | (double) zc | Z value of the circle center point, in meters |
| Input: | (double) xp1 | X value of the start point of the arc, in meters |
| Input: | (double) yp1 | Y value of the start point of the arc, in meters |
| Input: | (double) zp1 | Z value of the start point of the arc, in meters |
| Input: | (double) xp2 | X value of the end point of the arc, in meters |
| Input: | (double) yp2 | Y value of the end point of the arc, in meters |
| Input: | (double) zp2 | Z value of the end point of the arc, in meters |
| Input: | (short) direction | +1 : Go from the start point to the end point
in a counter-clockwise direction. -1 : Go from the start point to the end point
in a clockwise direction |
| Output: | (LPSKETCHSEGMENT) retval | Pointer to the arc that was created |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method creates a partial arc in the active
2D sketch. If a sketch is not active, then a new sketch is created. You
can check for an active sketch using the ModelDoc::GetActiveSketch2 function.

For COM applications, the object pointer returned
from this method can be used to call any of thekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SketchSegment
functions. The underlying SketchArc object can be obtained using QueryInterface
on the returned SketchSegment object.

OLE applications can define a new SketchSegment
or SketchArc object using the returned dispatch pointer. Visual Basic
applications interpret the pointer for you automatically, so you can use
the returned object to call SketchSegment or SketchArc functions.

ModelDoc::SetAddToDB and ModelDoc::SetDisplayWhenAdded
increase performance during entity creation by adding entities directly
to the SolidWorks database.

ModelDoc::SetAddToDB also avoids some of the peculoarities
involved with creating entities via the user interface, such as inferencing,
automatic relations, and snapping to the grid. Adding entities directly
to the database significantly increase the performance of this method.
When you are done creating entities, it is important to set ModelDoc::SetAddToDB(False)
to restore SolidWorks to its normal operating mode.

This method also works with ModelDoc::SetDisplayWhenAdded.
If you have called ModelDoc::SetAddToDB(True), additional performance
can be gained by calling ModelDoc::SetDisplayWhenAdded(False) to disable
immediate display of entities as they are added to the database. When
you are done creating all of your sketch entities, you must redraw your
document window (see ModelDoc::GraphicsRedraw2) to see the entities you
have added. You should also restore the original display settings by calling
ModelDoc::SetDisplayWhenAdded(True).

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc\ModelDoc__CreateArc2.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc\ModelDoc__CreateArc2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
