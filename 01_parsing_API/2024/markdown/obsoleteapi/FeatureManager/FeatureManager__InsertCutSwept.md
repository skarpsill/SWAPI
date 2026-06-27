---
title: "FeatureManager::InsertCutSwept"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__InsertCutSwept.htm"
---

# FeatureManager::InsertCutSwept

This method is obsolete and has been superseded
by[FeatureManager::InsertCutSwept2](FeatureManager__InsertCutSwept2.htm).

Description

This method inserts a swept
cut.

Syntax (OLE Automation)

retval = FeatureManager.InsertCutSwept ( propagate,
alignment, twistCtrlOption, keepTangency, forceNonRational, startMatchingType,
endMatchingType, isThinBody, thickness1, thickness2, thinType, useFeatScope,
useAutoSelect )

(Table)=========================================================

| Input: | (BOOL) propagate | TRUE propagates the swept cut propagates to the next edge, FALSE causes
the swept cut to occur only on the selected edge; to propagate to the
next edge, the next edge must be tangent to the current edge |
| --- | --- | --- |
| Input: | (BOOL) alignment | If the curve used to sweep goes from one face to another or from one
edge to another, passing TRUE causes the sweep to cut completely through
the end faces of the cut, FALSE causes the swept cut to begin and ends
perpendicular to the sweep curve; therefore, it may not break through
the two end faces of the body being cut |
| Input: | (short) twistCtrlOption | Twist control options (see Remarks ) |
| Input: | (BOOL) keepTangency | Follow path |
| Input: | (BOOL) forceNonRational | Keep constant normal |
| Input: | (short) startMatchingType | Tangency type (see Remarks ) |
| Input: | (short) endMatchingType | Tangency type (see Remarks ) |
| Input: | (BOOL) isThinBody | TRUE if this feature is a thin body, FALSE if
not |
| Input: | (double) thickness1 | Thickness value for the first direction. |
| Input: | (double) thickness2 | Thickness value for the second direction. |
| Input: | (short) thinType | Thin wall type (see Remarks ) |
| Input: | (VARIANT_BOOL) useFeatScope | TRUE if the feature only affects selected bodies,
FALSE if the feature affects all bodies |
| Input: | (VARIANT_BOOL) useAutoSelect | TRUE to automatically select all bodies and have
the feature affect those bodies, FALSE to select the bodies the feature
affects (see Remarks ) |
| Output: | (LPFEATURE) *retval | Pointer to the feature object |

Syntax (COM)

status = FeatureManager->InsertCutSwept ( propagate,
alignment, twistCtrlOption, keepTangency, forceNonRational, startMatchingType,
endMatchingType, isThinBody, thickness1, thickness2, thinType, useFeatScope,
useAutoSelect, retval )

Parameters Table Start

(Table)=========================================================

| Input: | (BOOL) propagate | TRUE propagates the swept cut propagates to the next edge, FALSE causes
the swept cut to occur only on the selected edge; to propagate to the
next edge, the next edge must be tangent to the current edge |
| --- | --- | --- |
| Input: | (BOOL) alignment | If the curve used to sweep goes from one face to another or from one
edge to another, passing TRUE causes the sweep to cut completely through
the end faces of the cut, FALSE causes the swept cut to begin and ends
perpendicular to the sweep curve; therefore, it may not break through
the two end faces of the body being cut |
| Input: | (short) twistCtrlOption | Twist control options (see Remarks ) |
| Input: | (BOOL) keepTangency | Follow path |
| Input: | (BOOL) forceNonRational | Keep constant normal |
| Input: | (short) startMatchingType | Tangency type (see Remarks ) |
| Input: | (short) endMatchingType | Tangency type (see Remarks ) |
| Input: | (BOOL) isThinBody | TRUE if this feature is a thin body, FALSE if
not |
| Input: | (double) thickness1 | Thickness value for the first direction |
| Input: | (double) thickness2 | Thickness value for the second direction |
| Input: | (short) thinType | Thin wall type (see Remarks ) |
| Input: | (VARIANT_BOOL) useFeatScope | TRUE if the feature only affects selected bodies,
FALSE if the feature affects all bodies |
| Input: | (VARIANT_BOOL) useAutoSelect | TRUE to automatically select all bodies and have
the feature affect those bodies, FALSE to select the bodies the feature
affects (see Remarks ) |
| Output: | (LPFEATURE) *retval | Pointer to the feature object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

UseModelDocExtension::SelectByIDto select the profile and sweep curves. The mark for:

Profile selection should be a 1

Sweep path should be 4

Guide-curve selection should be 2

The twistCtrlOption argument can take one of these values:

0 = Follow path

1 = Keep constant normal

2 = Follow path and first guide curve

3 = Follow first and second guide curve

The tangencytype arguments can take one of these
following values:

0 - none

1 - tangent to
the normal of the profile

2 - tangent to
a selected vector

3 - tangency to
all the adjacent faces sharing an edge with the start profile

4 - tangent to
some of the selected faces sharing an edge with the start profile (not
available)

The thinType arguemnt can take one of these values:

0 = One direction

1 = One direction reverse

2 = Mid-plane

3 = Two direction

When useAutoSelect is FALSE, the user must select
the bodies that the feature will affect.

When using cut or cavity features that result in
multiple bodies, you cannot select to keep all of the resulting bodies
or one or more selected bodies.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\FeatureManager\FeatureManager__InsertCutSwept.htm" >
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\FeatureManager\FeatureManager__InsertCutSwept.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
