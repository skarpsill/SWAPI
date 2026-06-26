---
title: "FeatureManager::InsertFilletBeadFeature"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__InsertFilletBeadFeature.htm"
---

# FeatureManager::InsertFilletBeadFeature

This method is obsolete and has been superseded
by[FeatureManager::InsertFilletBeadFeature2](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertFilletBeadFeature2.htm).

Description

This method inserts a fillet
weld bead feature.

Syntax (OLE Automation)

retval = FeatureManager.InsertFilletBeadFeature (
type1, size1, length1, pitch, type2, size2, length2, flag, edgeNum1, deSelEdge1,
edgeNum2, deSelEdge2)

(Table)=========================================================

| Input: | (short) type1 | First side: 0 = Full
length 1 = Intermittent 2 = Staggered |
| --- | --- | --- |
| Input: | (double) size1 | Size of fillet on first side |
| Input: | (double) length1 | Length of fillet on first side |
| Input: | (double) pitch | Pitch, if Intermittent or Staggered on both sides |
| Input: | (short) type2 | Second side: 0= Full
length 1 = Intermittent 2= Staggered |
| Input: | (double) size2 | Size of fillet on second side |
| Input: | (double) length2 | Length of fillet on second side |
| Input: | (long) flag | 0 = One-sided and no tangent propagation 1 = Two-sided 2 = Tangent propagation 3 = Two-sided and tangent propagation |
| Input: | (long) edgeNum1 | Number of intersecting edges
on first side |
| Input: | (VARIANT) deSelEdge1 | Array indicating if intersecting edges are selected
(0) or deselected (1) on first side |
| Input: | (long) edgeNum2 | Number of intersecting edges
on second side |
| Input: | (VARIANT) deSelEdge2 | Array indicating if intersecting
edges are selected (0) or deselected (1) on second side |
| Output: | (LPFEATURE) retval | Pointer to the Feature object |

Syntax (COM)

status = FeatureManager->InsertFilletBeadFeature
( type1, size1, length1, pitch, type2, size2, length2, flag, edgeNum1,
deSelEdge1, edgeNum2, deSelEdge2, &retval)

Parameters Table Start

(Table)=========================================================

| Input: | (short) type1 | First side: 0 = Full
length 1 = Intermittent 2 = Staggered |
| --- | --- | --- |
| Input: | (double) size1 | Size of fillet on first side |
| Input: | (double) length1 | Length of fillet on first side |
| Input: | (double) pitch | Pitch, if Intermittent
or Staggered on both sides |
| Input: | (short) type2 | Second side: 0 = Full
length 2 = Intermittent 3 = Staggered |
| Input: | (double) size2 | Size of fillet on second side |
| Input: | (double) length2 | Length of fillet on second side |
| Input: | (long) flag | 0 = One-sided and no tangent propagation 1 = Two-sided 2 = Tangent propagation 3 = Two-sided and tangent propagation |
| Input: | (long) edgeNum1 | Number of intersecting edges
on first side |
| Input: | (VARIANT) deSelEdge1 | Array indicating if intersecting
edges are selected (0) or deselected (1) on first side |
| Input: | (long) edgeNum2 | Number of intersecting
edges on second side |
| Input: | (VARIANT) deSelEdge2 | Array indicating if intersecting
edges are selected (0) or deselected (1) on second side |
| Output: | (LPFEATURE) retval | Pointer to the Feature object |
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
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes004$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\FeatureManager\FeatureManager__InsertFilletBeadFeature.htm" >
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
<param name="Items" value="FeatureManager_Object$$**$$ZGetWeldments$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\FeatureManager\FeatureManager__InsertFilletBeadFeature.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
