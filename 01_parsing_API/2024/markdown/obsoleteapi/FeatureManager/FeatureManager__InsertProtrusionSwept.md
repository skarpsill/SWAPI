---
title: "FeatureManager::InsertProtrusionSwept"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__InsertProtrusionSwept.htm"
---

# FeatureManager::InsertProtrusionSwept

This method is obsolete and has been superseded
by[FeatureManager::InsertProtrusionSwept2](FeatureManager__InsertProtrusionSwept2.htm).

Description

This method inserts a swept
protrusion.

Syntax (OLE Automation)

retval = FeatureManager.InsertProtrusionSwept ( propagate,
alignment, twistCtrlOption, keepTangency, forceNonRational, startMatchingType,
endMatchingType, isThinBody, thickness1, thickness2, thinType, merge,
useFeatScope, useAutoSelect )

(Table)=========================================================

| Input: | (BOOL) propagate | TRUE propagates the loft to the next tangent edge, FALSE does not |
| --- | --- | --- |
| Input: | (BOOL) alignment | TRUE causes the sweep to cut completely through the end faces of the
cut if the curve used to sweep goes from one face to another or from one
edge to another; FALSE causes the swept cut to begin and end perpendicular
to the sweep curve and it cannot break through the two end faces of the
cut body |
| Input: | (short) twistCtrlOption | 0
= Follow path 1
= Keep constant normal 2
= Follow path and first guide curve 3
= Follow first and second guide curve |
| Input: | (BOOL) keepTangency | TRUE maintains the tangency as in the section curves, FALSE does not If the section curves are tangent, then you can specify whether the
resulting faces are also tangent. When generating tangent faces, SolidWorks
maintains planar and cylindrical face shapes if the section curves exhibit
these characteristics. |
| Input: | (BOOL) forceNonRational | TRUE forces the resulting surface to be non-rational, FALSE does not |
| Input: | (short) startMatchingType | 0
= None 1
= Tangent to the normal of the profile 2
= Tangent to a selected vector 3
= Tangency to all the adjacent faces sharing an edge with the start profile 4
= Tangent to some of the selected faces sharing an edge with the start
profile (not available) |
| Input: | (short) endMatchingType | 0
= None 1
= Tangent to the normal of the profile 2
= Tangent to a selected vector 3
= Tangency to all the adjacent faces sharing an edge with the start profile 4
= Tangent to some of the selected faces sharing an edge with the start
profile (not available) |
| Input: | (BOOL) isThinBody | TRUE if this feature is a thin body, FALSE if it is not |
| Input: | (double) thickness1 | Thickness value for the first direction |
| Input: | (double) thickness2 | Thickness value for the second direction |
| Input: | (short) thinType | Thin wall type: 0 = One direction 1 = One direction reverse 2 = Mid-plane 3 = Two direction |
| Input: | (BOOL) merge | TRUE to merge the results in the multibody part, FALSE to not |
| Input: | (VARIANT_BOOL) useFeatScope | TRUE if the feature only affects selected bodies, FALSE if the feature
affects all bodies |
| Input: | VARIANT_BOOL) useAutoSelect | TRUE to automatically select all bodies and have the feature affect
those bodies, FALSE to select the bodies the feature affects |
| Output: | (LPFEATURE) *retval | Pointer to the feature object |

Syntax (COM)

status = FeatureManager->InsertProtrusionSwept
( propagate, alignment, twistCtrlOption, keepTangency, forceNonRational,
startMatchingType, endMatchingType, isThinBody, thickness1, thickness2,
thinType, merge, useFeatScope, useAutoSelect, retval )

Parameters Table Start

(Table)=========================================================

| Input: | (BOOL) propagate | TRUE propagates the loft to the next tangent edge, FALSE does not |
| --- | --- | --- |
| Input: | (BOOL) alignment | TRUE causes the sweep to cut completely through the end faces of the
cut if the curve used to sweep goes from one face to another or from one
edge to another; FALSE causes the swept cut to begin and end perpendicular
to the sweep curve and it cannot break through the two end faces of the
cut body |
| Input: | (short) twistCtrlOption | 0
= Follow path 1
= Keep constant normal 2
= Follow path and first guide curve 3
= Follow first and second guide curve |
| Input: | (BOOL) keepTangency | TRUE maintains the tangency as in the section curves, FALSE does not If the section curves are tangent, then you can specify whether the
resulting faces are also tangent. When generating tangent faces, SolidWorks
maintains planar and cylindrical face shapes if the section curves exhibit
these characteristics. |
| Input: | (BOOL) forceNonRational | TRUE forces the resulting surface to be non-rational, FALSE does not |
| Input: | (short) startMatchingType | 0
= None 1
= Tangent to the normal of the profile 2
= Tangent to a selected vector 3
= Tangency to all the adjacent faces sharing an edge with the start profile 4
= Tangent to some of the selected faces sharing an edge with the start
profile (not available) |
| Input: | (short) endMatchingType | 0
= None 1
= Tangent to the normal of the profile 2
= Tangent to a selected vector 3
= Tangency to all the adjacent faces sharing an edge with the start profile 4
= Tangent to some of the selected faces sharing an edge with the start
profile (not available) |
| Input: | (BOOL) isThinBody | TRUE if this feature is a thin body, FALSE if it is not |
| Input: | (double) thickness1 | Thickness value for the first direction |
| Input: | (double) thickness2 | Thickness value for the second direction |
| Input: | (short) thinType | Thin wall type: 0 = One direction 1 = One direction reverse 2 = Mid-plane 3 = Two direction |
| Input: | (BOOL) merge | TRUE to merge the results in the multibody part, FALSE to not |
| Input: | (VARIANT_BOOL) useFeatScope | TRUE if the feature only affects selected bodies, FALSE if the feature
affects all bodies |
| Input: | VARIANT_BOOL) useAutoSelect | TRUE to automatically select all bodies and have the feature affect
those bodies, FALSE to select the bodies the feature affects |
| Output: | (LPFEATURE) *retval | Pointer to the feature object |
| Return: | (HRESULT) status | S_OK is successful |

Remarks

Use ModelDocExtension::SelectByID to select the profile and sweep curves.
Set the mark for:

- 1 = profile selection to 1
- 4 = sweep path
- 2 = guide curve selection, if provided

When useAutoSelect is FALSE,
the user must select the bodies that the feature will affect.

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
<param name="Items" value="ZReleaseNotes2003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\FeatureManager\FeatureManager__InsertProtrusionSwept.htm" >
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
<param name="Items" value="FeatureManager_Object$$**$$Feature_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\FeatureManager\FeatureManager__InsertProtrusionSwept.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
