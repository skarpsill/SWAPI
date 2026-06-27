---
title: "ModelDoc2::InsertSheetMetalMiterFlange"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertSheetMetalMiterFlange.htm"
---

# ModelDoc2::InsertSheetMetalMiterFlange

This method is obsolete and has been superseded
by[FeatureManager::InsertSheetMetalMiterFlange](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertSheetMetalMiterFlange.htm).

Description

This method inserts a sheet metal miter flange
into this model document.

Syntax (OLE Automation)

void ModelDoc2.InsertSheetMetalMiterFlange ( useReliefRatio,
useDefaultGap, useAutoRelief, globalRadius, ripGap, autoReliefRatio, autoReliefWidth,
autoReliefDepth, reliefType, ripLocation)

(Table)=========================================================

| Input: | (BOOL) useReliefRatio | TRUE to use the relief ratio value FALSE otherwise |
| --- | --- | --- |
| Input: | (BOOL) useDefaultGap | TRUE to use the default gap value FALSE otherwise |
| Input: | (BOOL) useAutoRelief | TRUE to use auto relief FALSE otherwise |
| Input: | (double) globalRadius | Value for the global radius |
| Input: | (double) ripGap | Value for the rip-gap |
| Input: | (double) autoReliefRatio | Value for the auto relief ratio |
| Input: | (double) autoReliefWidth | Value for the auto relief width |
| Input: | (double) autoReliefDepth | Value for the auto relief depth |
| Input: | (long) reliefType | relief type; currently only supports 0 = Tear
relief type |
| Input: | (long) ripLocation | Value for the rip location: 0 = Start 1 = End 2 = Start
and end |

Syntax (COM)

status = ModelDoc2->InsertSheetMetalMiterFlange
( useReliefRatio, useDefaultGap, useAutoRelief, globalRadius, ripGap,
autoReliefRatio, autoReliefWidth, autoReliefDepth, reliefType, ripLocation)

(Table)=========================================================

| Input: | (VARIANT_BOOL) useReliefRatio | TRUE to use the relief ratio value FALSE otherwise |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) useDefaultGap | TRUE to use the default gap value FALSE otherwise |
| Input: | (VARIANT_BOOL) useAutoRelief | TRUE to use auto relief FALSE otherwise |
| Input: | (double) globalRadius | Value for the global radius |
| Input: | (double) ripGap | Value for the rip-gap |
| Input: | (double) autoReliefRatio | Value for the auto relief ratio |
| Input: | (double) autoReliefWidth | Value for the auto relief width |
| Input: | (double) autoReliefDepth | Value for the auto relief depth |
| Input: | (long) reliefType | relief type; currently only supports 0 = Tear
relief type |
| Input: | (long) ripLocation | Value for the rip location: 0 = Start 1 = End 2 = Start
and end |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__InsertSheetMetalMiterFlange.htm" >
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__InsertSheetMetalMiterFlange.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
