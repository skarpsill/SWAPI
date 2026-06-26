---
title: "ModelDoc2::FeatureChamferType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__FeatureChamferType.htm"
---

# ModelDoc2::FeatureChamferType

This method is obsolete and has been superseded
by[FeatureManager::InsertFeatureChamfer](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertFeatureChamfer.htm).

Description

This method creates a chamfer feature according to the type specified
(angle-distance, distance-distance, or vertex chamfer).

Syntax (OLE Automation)

(void) ModelDoc2.FeatureChamferType
( chamferType, width, angle, flip, otherDist, vertexChamDist1, vertexChamDist2,
vertexChamDist3 )

(Table)=========================================================

| Input: | (short) chamferType | Chamfer type as defined in swChamferType_e |
| --- | --- | --- |
| Input: | (double) width | Width for angle-distance chamfers or one distance for distance-distance
chamfers |
| Input: | (double) angle | Angle for angle-distance chamfers |
| Input: | (BOOL) flip | TRUE to flip the direction of the chamfer, FALSE to not |
| Input: | (double) otherDist | Other distance for distance-distance chamfers |
| Input: | (double) vertexChamDist1 | First distance for vertex chamfers |
| Input: | (double) vertexChamDist2 | Second distance for vertex chamfers |
| Input: | (double) vertexChamDist3 | Last distance for vertex chamfers |

Syntax (COM)

status = ModelDoc2->FeatureChamferType
( chamferType, width, angle, flip, otherDist, vertexChamDist1, vertexChamDist2,
vertexChamDist3 )

(Table)=========================================================

| Input: | (short) chamferType | Chamfer type as defined in swChamferType_e |
| --- | --- | --- |
| Input: | (double) width | Width for angle-distance chamfers or one distance for distance-distance
chamfers |
| Input: | (double) angle | Angle for angle-distance chamfers |
| Input: | (VARIANT_BOOL) flip | TRUE to flip the direction of the chamfer, FALSE to not |
| Input: | (double) otherDist | Other distance for distance-distance chamfers |
| Input: | (double) vertexChamDist1 | First distance for vertex chamfers |
| Input: | (double) vertexChamDist2 | Second distance for vertex chamfers |
| Input: | (double) vertexChamDist3 | Last distance for vertex chamfers |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Both angle-distance and distance-distance chamfers are edge chamfers.
This means that all measurements are from edges. An angle-distance chamfer
requires an angle and a distance; a distance-distance chamfer requires
two distances for both sides of the chamfered edges.

A vertex chamfer only works on a vertex with three adjacent edges of
the same convexity. The distance values specified measure from the vertex
along three adjacent edges. For non-linear edges, this value is an arc
length value; it is not a chordal value.

See Vertex::EnumEdgesOriented to determine the edge order used by this
method.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__FeatureChamferType.htm" >
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__FeatureChamferType.htm" >
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
<param name="Items" value="EXCreateChamfer$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__FeatureChamferType.htm" >
<param name="_ID" value="RelatedTopic4" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
