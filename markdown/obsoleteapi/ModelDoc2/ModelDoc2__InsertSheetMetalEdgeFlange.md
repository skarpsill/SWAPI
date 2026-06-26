---
title: "ModelDoc2::InsertSheetMetalEdgeFlange"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertSheetMetalEdgeFlange.htm"
---

# ModelDoc2::InsertSheetMetalEdgeFlange

This
method is obsolete and has been superseded byFeatureManager::InsertSheetMetalEdgeFlange .

Description

This method inserts a sheet metal edge flange
in this model document.

Syntax (OLE Automation)

void ModelDoc2.InsertSheetMetalEdgeFlange ( flangeEdge,
sketchFeat, booleanOptions, dAngle, dRadius, bendPosition, dOffsetDist,
reliefType, dReliefRatio, dReliefWidth, dReliefDepth, &retval )

(Table)=========================================================

| Input: | (LPDISPATCH) flangeEdge | Edge to which to apply flange |
| --- | --- | --- |
| Input: | (LPDISPATCH) sketchFeat | Sketch to use for flange |
| Input: | (long) booleanOptions | Flange options as defined in swInsertEdgeFlangeOptions_e |
| Input: | (double) dAngle | Flange angle |
| Input: | (double) dRadius | Bend radius |
| Input: | (long) bendPosition | Flange position as defined in swFlangePositionTypes_e |
| Input: | (double) dOffsetDist | Flange length |
| Input: | (long) reliefType | Relief type as defined in swSheetMetalReliefTypes |
| Input: | (double) dReliefRatio | Relief ratio |
| Input: | (double) dReliefWidth | Relief width |
| Input: | (double) dReliefDepth | Relief depth |
| Output: | (LPDISPATCH) retval | Pointer to the new edge flange |

Syntax (COM)

status = ModelDoc2->IInsertSheetMetalEdgeFlange
( flangeEdge, sketchFeat, booleanOptions, dAngle, dRadius, bendPosition,
dOffsetDist, reliefType, dReliefRatio, dReliefWidth, dReliefDepth, &retval
)

Parameters Table Start

(Table)=========================================================

| Input: | (LPEDGE) flangeEdge | Edge to which to apply flange |
| --- | --- | --- |
| Input: | (LPFEATURE) sketchFeat | Sketch to use for flange |
| Input: | (long) booleanOptions | Flange options as defined in swInsertEdgeFlangeOptions_e |
| Input: | (double) dAngle | Flange angle |
| Input: | (double) dRadius | Bend radius |
| Input: | (long) bendPosition | Flange position as defined in swFlangePositionTypes_e |
| Input: | (double) dOffsetDist | Flange length |
| Input: | (long) reliefType | Relief type as defined in swSheetMetalReliefTypes |
| Input: | (double) dReliefRatio | Relief ratio |
| Input: | (double) dReliefWidth | Relief width |
| Input: | (double) dReliefDepth | Relief depth |
| Output: | (LPFEATURE) retval | Pointer to the new edge flange |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use ModelDoc2::InsertSketchForEdgeFlange
to create a sketch for this method.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDoc2\ModelDoc2__InsertSheetMetalEdgeFlange.htm" >
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
<param name="Items" value="ModelDoc2 Method$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDoc2\ModelDoc2__InsertSheetMetalEdgeFlange.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
