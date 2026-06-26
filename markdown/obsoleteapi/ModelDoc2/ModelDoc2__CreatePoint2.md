---
title: "ModelDoc2::CreatePoint2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreatePoint2.htm"
---

# ModelDoc2::CreatePoint2

This method is obsolete and superseded[SketchManager::CreatePoint](sldworksAPI.chm::/SketchManager/SketchManager__CreatePoint.htm).

Description

This method creates a sketch point in the active
2D or 3D sketch.

Syntax (OLE Automation)

retval = ModelDoc2.CreatePoint2 (x, y, z)

(Table)=========================================================

| Input: | (double) x | X location of the point |
| --- | --- | --- |
| Input: | (double) y | Y location of the point |
| Input: | (double) z | Z location of the point; ignored for 2D sketches |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created
sketch point; this value is NULL if the operation fails |

Syntax (COM)

status = ModelDoc2->ICreatePoint2 ( x, y, z, &retval
)

(Table)=========================================================

| Input: | (double) x | X location of the point |
| --- | --- | --- |
| Input: | (double) y | Y location of the point |
| Input: | (double) z | Z location of the point; ignored for 2D sketches |
| Output: | (LPSKETCHPOINT) retval | Pointer to a newly created sketch point; this
value is NULL if the operation fails |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method creates a point in the active 2D or
3D sketch. If a sketch is not active, the point is not created and NULL
is returned. Use ModelDoc2::GetActiveSketch2 to check to see if the sketch
is active.

ModelDoc2::SetAddToDB and ModelDoc2::SetDisplayWhenAdded
increase performance during entity creation by adding entities directly
to the SolidWorks database. ModelDoc2::SetAddToDB also avoids inferencing.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__CreatePoint2.htm" >
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
<param name="Items" value="ModelDoc2_Object$$**$$CreateLine2$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__CreatePoint2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic4
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
<param name="Items" value="EXGetAssemblyBoundingBox$$**$$EXCreateSketchLine$$**$$EXCreatePlane3Points$$**$$EXIntersectFaceEdge$$**$$EXClosestDistanceBetweenModelComponents$$**$$EXGetBox$$**$$EXGetSplineEllipticalEdge$$**$$EXCreateBlockDefinitionCSharp$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__CreatePoint2.htm" >
<param name="_ID" value="RelatedTopic4" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
