---
title: "ModelDoc::InsertSheetMetalBaseFlange"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertSheetMetalBaseFlange.htm"
---

# ModelDoc::InsertSheetMetalBaseFlange

This
method is obsolete and has been superseded by[ModelDoc2::InsertSheetMetalBaseFlange](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertSheetMetalBaseFlange.htm).

Description

Given a selected sketch or active sketch, this
method inserts a sheet metal base flange feature.

Syntax (OLE Automation)

voidModelDoc.InsertSheetMetalBaseFlange ( thickness,
thickenDir, radius, extrudeDist1, extrudeDist2, flipExtruDir, endCondition1,
endCondition2, dirToUse)

(Table)=========================================================

| Input: | (double) thickness | Wall thickness of the sheet metal feature |
| --- | --- | --- |
| Input: | (BOOL) thickenDir | Direction to thicken the sheet metal |
| Input: | (double) radius | Global bend radius to insert at the corners |
| Input: | (double) extrudeDist1 | Distance of the sheet metal extrusion for the
Direction1 |
| Input: | (double) extrudeDist2 | Distance of the sheet metal extrusion for the
Direction2 |
| Input: | (BOOL) flipExtruDir | Reverse extrude direction |
| Input: | (long) endCondition1 | End condition for first extrude distance |
| Input: | (long) endCondition2 | End condition for second extrude distance |
| Input: | (long) dirToUse | Type of end condition |

Syntax (COM)

status = ModelDoc->InsertSheetMetalBaseFlange
( thickness, thickenDir, radius, extrudeDist1, extrudeDist2, flipExtruDir,
endCondition1, endCondition2, dirToUse)

(Table)=========================================================

| Input: | (double) thickness | Wall thickness of the sheet metal feature |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) thickenDir | Direction to thicken the sheet metal |
| Input: | (double) radius | Global bend radius to insert at the corners |
| Input: | (double) extrudeDist1 | Distance of the sheet metal extrusion for the
Direction1 |
| Input: | (double) extrudeDist2 | Distance of the sheet metal extrusion for the
Direction2 |
| Input: | (VARIANT_BOOL) flipExtruDir | Reverse extrude direction |
| Input: | (long) endCondition1 | End condition for first extrude distance |
| Input: | (long) endCondition2 | End condition for second extrude distance |
| Input: | (long) dirToUse | Type of end condition |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

(Table)=========================================================

| Argument | Description |
| --- | --- |
| thickenDir | Refers to the direction that the profile will be offset and thus the
thickness of the resulting sheet metal flange. TRUE will thicken to the
inside, FALSE will thicken to the outside. |
| flipExtruDir | Refers to the direction the extrude distance will go from the sketch
plane. If this value is TRUE, the direction will be reversed from the
default direction. |
| endCondition1 and endCondition2 | Can have values of: 0 – use the distance, 1 – extrude up to a point,
or 2 – extrude up to a surface. For a midplane distance, endCondition1
and endCondition2 should be equal and each half the desired distance. |
| dirToUse | Refers to which direction to use:0 – use both directions, 1 – use the
first direction, or 2 – use the second direction. |

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

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
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__InsertSheetMetalBaseFlange.htm" >
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__InsertSheetMetalBaseFlange.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
