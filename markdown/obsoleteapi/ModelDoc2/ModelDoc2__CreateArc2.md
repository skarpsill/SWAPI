---
title: "ModelDoc2::CreateArc2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateArc2.htm"
---

# ModelDoc2::CreateArc2

This method is obsolete and has been superseded
by[SketchManager::CreateArc](sldworksAPI.chm::/SketchManager/SketchManager__CreateArc.htm).

Description

This method creates an arc based on a center
point, a start, end point, and a direction.

Syntax (OLE Automation)

retval = ModelDoc2.CreateArc2 ( xc, yc, zc, xp1,
yp1, zp1, xp2, yp2, zp2, direction )

(Table)=========================================================

| Input: | (double) xc | X value of the circle center point in meters |
| --- | --- | --- |
| Input: | (double) yc | Y value of the circle center point in meters |
| Input: | (double) zc | Z value of the circle center point in meters |
| Input: | (double) xp1 | X value of the start point of the arc in meters |
| Input: | (double) yp1 | Y value of the start point of the arc in meters |
| Input: | (double) zp1 | Z value of the start point of the arc in meters |
| Input: | (double) xp2 | X value of the end point of the arc in meters |
| Input: | (double) yp2 | Y value of the end point of the arc in meters |
| Input: | (double) zp2 | Z value of the end point of the arc in meters |
| Input: | (short) direction | +1
: Go from the start point to the end point in a counter-clockwise direction -1
: Go from the start point to the end point in a clockwise direction |
| Return: | (LPDISPATCH) retval | Pointer to the dispatch object of the arc that
was created |

Syntax (COM)

status = ModelDoc2->ICreateArc2 ( xc, yc, zc,
xp1, yp1, zp1, xp2, yp2, zp2, direction, &retval )

(Table)=========================================================

| Input: | (double) xc | X value of the circle center point in meters |
| --- | --- | --- |
| Input: | (double) yc | Y value of the circle center point in meters |
| Input: | (double) zc | Z value of the circle center point in meters |
| Input: | (double) xp1 | X value of the start point of the arc in meters |
| Input: | (double) yp1 | Y value of the start point of the arc in meters |
| Input: | (double) zp1 | Z value of the start point of the arc in meters |
| Input: | (double) xp2 | X value of the end point of the arc in meters |
| Input: | (double) yp2 | Y value of the end point of the arc in meters |
| Input: | (double) zp2 | Z value of the end point of the arc in meters |
| Input: | (short) direction | +1
: Go from the start point to the end point in a counter-clockwise direction -1
: Go from the start point to the end point in a clockwise direction |
| Output: | (LPSKETCHSEGMENT) retval | Pointer to the newly created arc |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method creates a partial arc in the active
2D sketch. If a sketch is not active, then a new sketch iskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}created.
You can check for an active sketch using ModelDoc2::GetActiveSketch2.

For COM applications, the object pointer returned
from this method can be used to call any APIs on the SketchSegment interface.
The underlying SketchArc object can be obtained using QueryInterface on
the returned SketchSegment object.

OLE applications can define a new ISketchSegment
or ISketchArc object using the returned Dispatch pointer. Visual Basic
applications interpret the pointer for you automatically, so you can use
the returned object to call SketchSegment or SketchArc functions.

ModelDoc2::SetAddToDB and ModelDoc2::SetDisplayWhenAdded
increase performance during entity creation by adding entities directly
to the SolidWorks database.

ModelDoc2::SetAddToDB also avoids some of the peculiarities
involved with creating entities via the user interface, such as inferencing,
automatic relations, and snapping to the grid. Adding entities directly
to the database also increases the performance of this API. When you are
done creating entities, it is important to call ModelDoc2::SetAddToDB(False),
to restore SolidWorks to its normal operating mode.

This method also works with ModelDoc2::SetDisplayWhenAdded.
If you have called ModelDoc2::SetAddToDB(True), additional performance
can be gained by calling ModelDoc2::SetDisplayWhenAdded(False) to disable
immediate display of entities as they are added to the database. When
you are done creating all of your sketch entities, you must redraw your
document window (see ModelDoc2::GraphicsRedraw2) to see the entities that
you added. You should also restore the original display settings by calling
ModelDoc2::SetDisplayWhenAdded(True).

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__CreateArc2.htm" >
<param name="_ID" value="RelatedTopic2" >
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
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__CreateArc2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
