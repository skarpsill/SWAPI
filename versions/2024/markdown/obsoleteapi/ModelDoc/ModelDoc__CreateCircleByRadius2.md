---
title: "ModelDoc::CreateCircleByRadius2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateCircleByRadius2.htm"
---

# ModelDoc::CreateCircleByRadius2

## ModelDoc ::CreateCircleByRadius2

This
method is obsolete and has been superseded by[ModelDoc2::CreateCircleByRadius2](../ModelDoc2/ModelDoc2__CreateCircleByRadius2.htm).

Description

This method creates a circle based on a center
point and a specified radius.

Syntax (kadov_tag{{<ignored>}}OLEkadov_tag{{</ignored>}}Automation)

kadov_tag{{<ignored>}}retvalkadov_tag{{</ignored>}}= ModelDoc.CreateCircleByRadius2 (kadov_tag{{<ignored>}}xckadov_tag{{</ignored>}},kadov_tag{{<ignored>}}yckadov_tag{{</ignored>}},kadov_tag{{<ignored>}}zckadov_tag{{</ignored>}},
radius )

(Table)=========================================================

| Input: | (double) xc | X value of the circle center point, in meters |
| --- | --- | --- |
| Input: | (double) yc | Y value of the circle center point, in meters |
| Input: | (double) zc | Z value of the circle center point, in meters |
| Input: | (double) radius | Radius of the circle, in meters |
| Return: | ( LPDISPATCH ) retval | Pointer to the Dispatch object of the circle
that was created |

Syntax (kadov_tag{{<ignored>}}COMkadov_tag{{</ignored>}})

status =kadov_tag{{<ignored>}}ModelDoc-kadov_tag{{</ignored>}}>ICreateCircleByRadius2
(kadov_tag{{<ignored>}}xckadov_tag{{</ignored>}},kadov_tag{{<ignored>}}yckadov_tag{{</ignored>}},kadov_tag{{<ignored>}}zckadov_tag{{</ignored>}}, radius,
&kadov_tag{{<ignored>}}retvalkadov_tag{{</ignored>}})

(Table)=========================================================

| Input: | (double) xc | X value of the circle center point, in meters |
| --- | --- | --- |
| Input: | (double) yc | Y value of the circle center point, in meters |
| Input: | (double) zc | Z value of the circle center point, in meters |
| Input: | (double) radius | Radius of the circle, in meters |
| Output: | ( LPSKETCHSEGMENT ) retval | Pointer to the circle that was created |
| Return: | ( HRESULT )
status | S_OK if successful |

Remarks

This method creates a full circle in the active
2D sketch. If a sketch is not active, then a new sketch will be created.
You can check for an active sketch using thekadov_tag{{<ignored>}}ModelDockadov_tag{{</ignored>}}::GetActiveSketch2
function.

Forkadov_tag{{<ignored>}}COMkadov_tag{{</ignored>}}applications, the object pointer returned from this method can be used
to call anykadov_tag{{<ignored>}}APIskadov_tag{{</ignored>}}on thekadov_tag{{<ignored>}}SketchSegmentkadov_tag{{</ignored>}}interface. The underlyingkadov_tag{{<ignored>}}SketchArckadov_tag{{</ignored>}}object can be obtained usingkadov_tag{{<ignored>}}QueryInterfacekadov_tag{{</ignored>}}on the returnedkadov_tag{{<ignored>}}SketchSegmentkadov_tag{{</ignored>}}object.

kadov_tag{{<ignored>}}OLEkadov_tag{{</ignored>}}applications can simply define a newkadov_tag{{<ignored>}}SketchSegmentkadov_tag{{</ignored>}}orkadov_tag{{<ignored>}}SketchArckadov_tag{{</ignored>}}object using the returned dispatch pointer. Visual Basic applications
will interpret the pointer for you automatically, so you can use the returned
object to callkadov_tag{{<ignored>}}SketchSegmentkadov_tag{{</ignored>}}orkadov_tag{{<ignored>}}SketchArckadov_tag{{</ignored>}}functions.

kadov_tag{{<ignored>}}ModelDockadov_tag{{</ignored>}}::kadov_tag{{<ignored>}}SetAddToDBkadov_tag{{</ignored>}}andkadov_tag{{<ignored>}}ModelDockadov_tag{{</ignored>}}::kadov_tag{{<ignored>}}SetDisplayWhenAddedkadov_tag{{</ignored>}}increase performance during entity creation by adding entities directly
to thekadov_tag{{<ignored>}}SolidWorkskadov_tag{{</ignored>}}database.

kadov_tag{{<ignored>}}ModelDockadov_tag{{</ignored>}}::kadov_tag{{<ignored>}}SetAddToDBkadov_tag{{</ignored>}}avoids some of the peculiarities involved with creating entities via the
user interface, such as inferencing, automatic relations, and snapping
to the grid. Adding entities directly to the database also significantly
increases the performance of this API. When you are done creating entities,
it is important to callkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ModelDoc::SetAddToDB(False),
to restore SolidWorks to its normal operating mode.

This API also works in conjunction with[ModelDoc::SetDisplayWhenAdded](ModelDoc__SetDisplayWhenAdded.htm).
If you have called[ModelDoc::SetAddToDB](ModelDoc__SetAddToDB.htm)(True),
additional performance can be gained by calling[ModelDoc::SetDisplayWhenAdded](ModelDoc__SetDisplayWhenAdded.htm)(False)
to disable immediate display of entities as they are added to the database.
When you are done creating all of your sketch entities, you will need
to redraw your document window (refer to[ModelDoc::GraphicsRedraw2](ModelDoc__GraphicsRedraw2.htm))
to see the entities you've added. You should also restore the original
display settings by calling[ModelDoc::SetDisplayWhenAdded](ModelDoc__SetDisplayWhenAdded.htm)(True).

The create a circle using a center point and a
point on the circle, refer to[ModelDoc::CreateCircle2](ModelDoc__CreateCircle2.htm).
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc\ModelDoc__CreateCircleByRadius2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
