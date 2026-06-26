---
title: "FeatureManager::InsertSheetMetalEdgeFlange"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__InsertSheetMetalEdgeFlange.htm"
---

# FeatureManager::InsertSheetMetalEdgeFlange

This method is obsolete and has been superseded
by[FeatureManager::InsertSheetMetalEdgeFlange2](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertSheetMetalEdgeFlange2.htm).

Description

This method inserts an edge
flange in this sheet metal part.

Syntax (OLE Automation)

pFeat = FeatureManager.InsertSheetMetalEdgeFlange
( flangeEdge, sketchFeat, booleanOptions, dAngle, dRadius, bendPosition,
dOffsetDist, reliefType, dReliefRatio, dReliefWidth, dReliefDepth, flangeSharpType,
pCBA)

(Table)=========================================================

| Input: | (LPEDGE) flangeEdge | Edge to which to apply a flange |
| --- | --- | --- |
| Input: | (LPFEATURE) sketchFeat | Sketch to use for the flange |
| Input: | (long) booleanOptions | Flange options as defined by swInsertEdgeFlangeOptions_e |
| Input: | (double) dAngle | Flange angle |
| Input: | (double) dRadius | Bend radius |
| Input: | (long) bendPosition | Flange bend position as defined by swFlangePositionTypes_e |
| Input: | (double) dOffsetDist | Length of flange |
| Input: | (long) reliefType | Relief type as defined by swSheetMetalReliefTypes |
| Input: | (double) dReliefRatio | Relief ratio |
| Input: | (double) dReliefWidth | Relief width |
| Input: | (double) dReliefDepth | Relief depth |
| Input: | (long) flangeSharpType | Flange virtual sharp type as
defined by swFlangeDimType_e |
| Input: | (LPCUSTOMBENDALLOWANCE) pCBA | If... Then... non-NULL Pointer to CustomBendAllowance object for which required values have
been set NULL Parent bend's bend allowance is used |
| If... | Then... |  |
| non-NULL | Pointer to CustomBendAllowance object for which required values have
been set |  |
| NULL | Parent bend's bend allowance is used |  |
| Output: | (LPFEATURE) pFeat | Pointer to the Feature object |

Syntax (COM)

status = FeatureManager->InsertSheetMetalEdgeFlange
( flangeEdge, sketchFeat, booleanOptions, dAngle, dRadius, bendPosition,
dOffsetDist, reliefType, dReliefRatio, dReliefWidth, dReliefDepth, flangeSharpType,
pCBA, &pFeat)

Parameters Table Start

(Table)=========================================================

| Input: | (LPEDGE) flangeEdge | Edge to which to apply a flange |
| --- | --- | --- |
| Input: | (LPFEATURE) sketchFeat | Sketch to use for the flange |
| Input: | (long) booleanOptions | Flange options as defined by swInsertEdgeFlangeOptions_e |
| Input: | (double) dAngle | Flange angle |
| Input: | (double) dRadius | Bend radius |
| Input: | (long) bendPosition | Flange bend position as defined
by swFlangePositionTypes_e |
| Input: | (double) dOffsetDist | Length of flange |
| Input: | (long) reliefType | Relief type as defined by swSheetMetalReliefTypes |
| Input: | (double) dReliefRatio | Relief ratio |
| Input: | (double) dReliefWidth | Relief width |
| Input: | (double) dReliefDepth | Relief depth |
| Input: | (long) flangeSharpType | Flange virtual sharp type as
defined by swFlangeDimType_e |
| Input: | (LPCUSTOMBENDALLOWANCE) pCBA | If... Then... non-NULL Pointer to CustomBendAllowance object for which required values have
been set NULL Parent bend's bend allowance is used |
| If... | Then... |  |
| non-NULL | Pointer to CustomBendAllowance object for which required values have
been set |  |
| NULL | Parent bend's bend allowance is used |  |
| Output: | (LPFEATURE) pFeat | Pointer to the Feature object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Before calling this method, call ModelDoc2::InsertSketchForEdgeFlange
and create a profile for the flange. After creating the profile, call
this method to create the flange.

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
<param name="Items" value="ZReleaseNotes005$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\FeatureManager\FeatureManager__InsertSheetMetalEdgeFlange.htm" >
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
<param name="Items" value="FeatureManager_Object$$**$$ZSheetMetalEdgeFlange$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\FeatureManager\FeatureManager__InsertSheetMetalEdgeFlange.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
