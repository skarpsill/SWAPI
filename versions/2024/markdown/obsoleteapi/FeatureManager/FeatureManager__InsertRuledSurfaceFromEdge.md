---
title: "FeatureManager::InsertRuledSurfaceFromEdge"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__InsertRuledSurfaceFromEdge.htm"
---

# FeatureManager::InsertRuledSurfaceFromEdge

This method is obsolete and has been superseded
by[FeatureManager::InsertRuledSurfaceFromEdge2](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertRuledSurfaceFromEdge2.htm).

Description

This method inserts a surface
from the selected edge on this feature.

Syntax (OLE Automation)

retval = FeatureManager.InsertRuledSurfaceFromEdge
( type, length, flipPullDir, flipDir, trimAndSew, angle, coordInput, x,
y, z )

(Table)=========================================================

| Input: | (long) type | 0
= Tangent to Surface 1
= Normal to Surface 2
= Tapered to Vector 3
= Perpendicular to Vector 4
= Sweep |
| --- | --- | --- |
| Input: | (double) length | Distance at which to create the surface; valid for Tangent to Surface,
Tapered to Vector, Perpendicular to Vector, and Sweep types only |
| Input: | (VARIANT_BOOL) flipPullDir | TRUE to flip the pull direction, FALSE to not; valid for Normal to Surface
and Tapered to Vector types only |
| Input: | (VARIANT_BOOL) flipDir | TRUE to flip the direction, FALSE to not; valid for Perpendicular to
Vector type only |
| Input: | (VARIANT_BOOL) trimAndSew | Trim and knit the surface, FALSE to not |
| Input: | (double) angle | Angle for Tapered to Vector type only |
| Input: | (VARIANT_BOOL) coordInput | TRUE to enable coordinate input, FALSE if not; for Sweep type only |
| Input: | (double) x | x coordinate |
| Input: | (double) y | y coordinate |
| Input: | (double) z | z coordinate |
| Output: | (LPFEATURE) retval | Pointer to the Feature object |

Syntax (COM)

status = FeatureManager->InsertRuledSurfaceFromEdge
( type, length, flipPullDir, flipDir, trimAndSew, angle, coordInput, x,
y, z, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (long) type | 0
= Tangent to Surface 1
= Normal to Surface 2
= Tapered to Vector 3
= Perpendicular to Vector 4
= Sweep |
| --- | --- | --- |
| Input: | (double) length | Distance at which to create the surface; valid for Tangent to Surface,
Tapered to Vector, Perpendicular to Vector, and Sweep types only |
| Input: | (VARIANT_BOOL) flipPullDir | TRUE to flip the pull direction, FALSE to not; valid for Normal to Surface
and Tapered to Vector types only |
| Input: | (VARIANT_BOOL) flipDir | TRUE to flip the direction, FALSE to not; valid for Perpendicular to
Vector type only |
| Input: | (VARIANT_BOOL) trimAndSew | Trim and knit the surface, FALSE to not |
| Input: | (double) angle | Angle for Tapered to Vector type only |
| Input: | (VARIANT_BOOL) coordInput | TRUE to enable coordinate input, FALSE if not; for Sweep type only |
| Input: | (double) x | x coordinate |
| Input: | (double) y | y coordinate |
| Input: | (double) z | z coordinate |
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
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2004$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\FeatureManager\FeatureManager__InsertRuledSurfaceFromEdge.htm" >
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
<param name="Items" value="FeatureManager_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\FeatureManager\FeatureManager__InsertRuledSurfaceFromEdge.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
