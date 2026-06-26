---
title: "ModelDoc2::InsertCutBlend3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertCutBlend3.htm"
---

# ModelDoc2::InsertCutBlend3

This
method is obsolete and has been superseded by ModelDoc2:InsertCutBlend4 .

Description

This method inserts a lofted cut based on the selected
profiles, centerline, and guide curves.

Syntax (OLE Automation)

(void) ModelDoc2.InsertCutBlend3 ( closed, keepTangency,
forceNonRational, tessToleranceFactor, startMatchingType, endMatchingType
)

(Table)=========================================================

| Input: | (Boolean) closed | TRUE for a closed loft, FALSE for an open loft |
| --- | --- | --- |
| Input: | (Boolean) keepTangency | Controls whether the section curves are tangent |
| Input: | (Boolean) forceNonRational | TRUE to force the resulting surface to be non-rational,
FALSE otherwise |
| Input: | (double) tessToleranceFactor | Factor to control the number of intermediate
sections used for loft with centerline; the default value is 1.0; the
greater the variable, the more intermediate sections created |
| Input: | (short) startMatchingType | Tangency type at the start profile |
| Input: | (short) endMatchingType | Tangency type at the end profile |

Syntax
(COM)

status = ModelDoc2->InsertCutBlend3 ( closed,
keepTangency, forceNonRational, tessToleranceFactor, startMatchingType,
endMatchingType )

(Table)=========================================================

| Input: | (VARIANT_BOOL) closed | TRUE for a closed loft, FALSE for an open loft |
| --- | --- | --- |
| Input: | (Boolean) keepTangency | Controls whether the section curves are tangent |
| Input: | (VARIANT_BOOL) forceNonRational | TRUE to force the resulting surface to be non-rational,
FALSE otherwise |
| Input: | (double) tessToleranceFactor | Factor to control the number of intermediate
sections used for loft with centerline; the default value is 1.0; the
greater the variable, the more intermediate sections created |
| Input: | (short) startMatchingType | Tangency type at the start profile |
| Input: | (short) endMatchingType | Tangency type at the end profile, see below. |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Selection of guide curves and centerline is optional;
however, selection of the profiles must be in an order consistent with
the desired direction of the loft. Because you are creating a surface,
the section profiles can be open.

Use of guide curves is recommended, especially
when selection of profiles is done in the FeatureManager design tree.

You can use any number of profiles; however, if
you selected only one profile, then any selected guide curves must be
closed curves.

If closed is TRUE and you have selected less that
three profiles, then any selected guide curves must be closed curves.

If the section curves are tangent, then keepTangency
controls whether the resulting surfaces arel also be tangent. Specify
TRUE to maintain the tangency as seen in the section curves. When generating
tangent surfaces, planar and cylindrical surface shapes are maintained
if the section curves exhibit these characteristics.

UseModelDocExtenstion::SelectByIDto select the profiles and guide curves. The mark for:

- profile selections should
  be a 1
- any guide curve selection,
  if provided, should be a 2
- centerline selection,
  if provided, should be a 4
- start tangency vector
  selection, if provided, should be a 8
- start tangency faces
  selection, if provided, should be a 16 (not currently available)
- kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}end
  tangency vector selection, if provided, should be a 32
- end tangency faces selection,
  if provided, should be a 64 (not currently available)

Linear edge, sketch line, axis, plane ,and planar faces are qualified
for tangency vector sections.

The tangency type arguments can be:

- 0 - none
- 1 - tangent
  to the normal of the profile
- 2 - tangent
  to a selected vector
- 3 - tangent
  to all the adjacent faces sharing an edge with the start profile
- 4 - tangent
  to some of the selected faces sharing an edge with the start profile (not
  currently available)

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc2\ModelDoc2__InsertCutBlend3.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc2\ModelDoc2__InsertCutBlend3.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
