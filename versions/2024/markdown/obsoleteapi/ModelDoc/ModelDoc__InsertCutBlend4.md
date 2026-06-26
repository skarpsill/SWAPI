---
title: "ModelDoc::InsertCutBlend4"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertCutBlend4.htm"
---

# ModelDoc::InsertCutBlend4

This
method is obsolete and has been superseded by[ModelDoc2::InsertCutBlend4](../ModelDoc2/ModelDoc2__InsertCutBlend4.htm).

Description

This method inserts a lofted cut based on the selected
profiles, centerline, and guide curves.

Syntax (OLE Automation)

void ModelDoc.InsertCutBlend4 ( closed, keepTangency,
forceNonRational, tessToleranceFactor, startMatchingType, endMatchingType,
isThinBody, thickness1, thickness2, thinType )

(Table)=========================================================

| Input: | (BOOL) closed | TRUE if you want the loft to be closed, FALSE
if the loft will be open |
| --- | --- | --- |
| Input: | (BOOL) keepTangency | Controls whether the section curves are tangent |
| Input: | (BOOL) forceNonRational | TRUE to force the resulting surface to be non-rational,
FALSE otherwise |
| Input: | (double) tessToleranceFactor | A factor to control the number of intermediate
sections used for loft with centerline; the default value is 1.0; the
greater the variable, the more intermediate sections are created |
| Input: | (short) startMatchingType | Tangency type at the start profile |
| Input: | (short) endMatchingType | Tangency type at the end profile |
| Input: | (BOOL) isThinBody | TRUE if this feature is a thin body, FALSE otherwise |
| Input: | (double) thickness1 | Thickness value for the first direction |
| Input: | (double) thickness2 | Thickness value for the second direction |
| Input: | (short) thinType | TRUE if this feature is a thin feature, FALSE
otherwise |

Syntax (COM)

status = ModelDoc->InsertCutBlend4 ( closed, keepTangency,
forceNonRational, tessToleranceFactor, startMatchingType, endMatchingType,
isThinBody, thickness1, thickness2, thinType )

(Table)=========================================================

| Input: | (VARIANT_BOOL) closed | TRUE if you want the loft to be closed, FALSE
if the loft will be open |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) keepTangency | Controls whether the section curves are tangent |
| Input: | (VARIANT_BOOL) forceNonRational | TRUE to force the resulting surface to be non-rational,
FALSE otherwise |
| Input: | (double) tessToleranceFactor | A factor to control the number of intermediate
sections used for loft with centerline; the default value is 1.0; the
greater the variable, the more intermediate sections are created. |
| Input: | (short) startMatchingType | Tangency type at the start profile, |
| Input: | (short) endMatchingType | Tangency type at the end profile |
| Input: | (VARIANT_BOOL) isThinBody | TRUE if this feature is a thin body, FALSE otherwise |
| Input: | (double) thickness1 | Thickness value for the first direction |
| Input: | (double) thickness2 | Thickness value for the second direction |
| Input: | (short) thinType | TRUE if this feature is a thin feature, FALSE
otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Selection of guide curves and centerline is optional;
however, selection of the profiles must be in an order consistent with
the desired direction of the loft. Because you are creating a surface,
the section profiles can be open.

Use of guide curves is recommended when selecting
profiles in the FeatureManager design tree.

You may use any number of profiles; however, if
you have selected only one profile, then any selected guide curves must
be closed curves.

If closed is TRUE and if you have selected less
that three profiles, then any selected guide curves must be closed curves.

If the section curves are tangent, then keepTangency
controls whether the resulting surfaces will also be tangent. Specify
TRUE to maintain the tangency as seen in the section curves, FALSE otherwise.
When generating tangent surfaces, SolidWorks will maintain planar and
cylindrical surface shapes if the section curves exhibit these characteristics.

Use SelectByMark and AndSelectByMark methods to select the profiles
and guide curves. The mark for the profile selections should be a 1; the
mark for any guide curve selection, if provided, should be a 2; the mark
for the centerline selection, if provided, should be a 4; the mark for
the start tangency vector selection, if provided, should be a 8; the mark
for the start tangency faces selection, if provided, should be a 16 (not
currently available); the mark for the end tangency vector selection,
if provided, should be a 32; the mark for the end tangency faces selection,
if provided, should be a 64 (not currently available). Linear edge, sketch
line, axis, plane and planar faces are qualified for tangency vector sections.

The tangency type arguments can take the following
values:

- 0 - none
- 1 - tangent
  to the normal of the profile
- 2 - tangent
  to a selected vector
- 3 - tangent
  to all of the adjacent faces sharing an edge with the start profile
- 4 - tangent
  to some of the selected faces sharing an edge with the start profile (not
  currently available)

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__InsertCutBlend4.htm" >
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
<param name="Items" value="ModelDoc_Object$$**$$ZModifyBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__InsertCutBlend4.htm" >
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Entity::SelectByMark$$**$$ModelDoc::SelectByMark$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__InsertCutBlend4.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic3
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
<param name="Items" value="Entity::SelectByMark$$**$$ModelDoc::AndSelectByMark$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__InsertCutBlend4.htm" >
<param name="_ID" value="RelatedTopic3" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
