---
title: "ModelDoc::CreatePoint2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreatePoint2.htm"
---

# ModelDoc::CreatePoint2

This
method is obsolete and has been superseded by[ModelDoc2::CreatePoint2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__CreatePoint2.htm).

Description

This method creates a sketch point in the active
2D or 3D sketch.

Syntax (OLE Automation)

retval = ModelDoc.CreatePoint2 (x,
y, z)

(Table)=========================================================

| Input: | (double) x | X location of the point |
| --- | --- | --- |
| Input: | (double) y | Y location of the point |
| Input: | (double) z | Z location of the point; ignored for 2D sketches |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created
SketchPoint object; this value is NULL if the operation fails |

Syntax (COM)

status = ModelDoc->ICreatePoint2 ( x, y, z, &retval
)

(Table)=========================================================

| Input: | (double) x | X location of the point |
| --- | --- | --- |
| Input: | (double) y | Y location of the point |
| Input: | (double) z | Z location of the point; ignored for 2D sketches |
| Output: | (LPSKETCHPOINT) retval | Pointer the newly created SketchPoint object;
this value is NULL if the operation fails |
| Return: | (HRESULT) status | S_OK if successful; S_FALSE otherwise |

Remarks

This method creates a point in the active 2D or
3D sketch. If a sketch is not active, the point is not created and NULL
is returned. You can check for an active sketch using ModelDoc::GetActiveSketch2.

ModelDoc::SetAddToDB and ModelDoc::SetDisplayWhenAdded
increases performance during entity creation by adding entities directly
to the SolidWorks database. ModelDoc::SetAddToDB also avoids inferencing.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZCreateSketchEntity$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\ModelDoc\ModelDoc__CreatePoint2.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\ModelDoc\ModelDoc__CreatePoint2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
