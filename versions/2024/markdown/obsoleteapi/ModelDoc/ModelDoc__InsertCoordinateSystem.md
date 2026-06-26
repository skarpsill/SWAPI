---
title: "ModelDoc::InsertCoordinateSystem"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertCoordinateSystem.htm"
---

# ModelDoc::InsertCoordinateSystem

This
method is obsolete and has been superseded by[ModelDoc2::InsertCoordinateSystem](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertCoordinateSystem.htm).

Description

This method inserts a coordinate system based
on selections.

Syntax (OLE Automation)

void ModelDoc.InsertCoordinateSystem
( xFlipped, yFlipped, zFlipped )

(Table)=========================================================

| Input: | (BOOL) xFlipped | TRUE to flip the x direction |
| --- | --- | --- |
| Input: | (BOOL) yFlipped | TRUE to flip the y direction |
| Input: | (BOOL) zFlipped | TRUE to flip the z direction |

Syntax (COM)

status = ModelDoc->InsertCoordinateSystem
( xFlipped, yFlipped, zFlipped )

(Table)=========================================================

| Input: | (VARIANT_BOOL) xFlipped | TRUE to flip the x direction |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) yFlipped | TRUE to flip the y direction |
| Input: | (VARIANT_BOOL) zFlipped | TRUE to flip the z direction |
| Return: | (HRESULT) status | S_OK if successful. |

Remarks

Programmatic selections should be made with a SelectByMark method. Use
the following marks with your SelectByMark selections:

- 1 Origin
- 2 X Axis
- 4 Y Axis
- 8 Z Axis

This method does not require all three axis to be selected. The behavior
is the same as interactively creating a coordinate system by selectingInsert, Reference
Geometry, Coordinate System.
SeeSolidWorks Help for more information.

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
<param name="Items" value="ModelDoc_Object$$**$$ZInsertFeature$$**$$ZCoordinateSystem$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__InsertCoordinateSystem.htm" >
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
<param name="Items" value="InsertCoordinateSystem_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__InsertCoordinateSystem.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
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
<param name="Items" value="Entity::SelectByMark$$**$$ModelDoc::SelectByMark$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__InsertCoordinateSystem.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
