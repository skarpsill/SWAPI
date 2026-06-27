---
title: "ModelDoc::InsertCutBlend2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertCutBlend2.htm"
---

# ModelDoc::InsertCutBlend2

This
method is obsolete and has been superseded by[ModelDoc::InsertCutBlend2](ModelDoc__InsertCutBlend3.htm).

Description

This method inserts a lofted cut based on the selected profiles and
guide curves. Selection of guide curves is optional; however, selection
of the profiles must be in an order consistent with the desired direction
of the loft.

Syntax (OLE Automation)

void ModelDoc.InsertCutBlend2 ( closed,
keepTangency, forceNonRational)

(Table)=========================================================

| Input: | (BOOL) closed | TRUE if you want the loft to be closed, FALSE if the loft will be open;
if TRUE, and if you have selected less that three profiles, then any selected
guide curves must be closed curves |
| --- | --- | --- |
| Input: | (BOOL) keepTangency | If the section curves are tangent, then you have the option to specify
whether the resulting surfaces will also be tangent; Specify
TRUE to maintain the tangency as seen in the section curves, FALSE otherwise;
when generating tangent surfaces, SolidWorks will maintain planar and
cylindrical surface shapes if the section curves exhibit these characteristics. |
| Input: | (BOOL) forceNonRational | TRUE to force the resulting surface to be non-rational, FALSE otherwise |

Syntax (COM)

status = ModelDoc->InsertCutBlend2
( closed, keepTangency, forceNonRational )

(Table)=========================================================

| Input: | (VARIANT_BOOL) closed | TRUE if you want the loft to be closed, FALSE if the loft will be open;
if TRUE, and if you have selected less that three profiles, then any selected
guide curves must be closed curves |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) keepTangency | If the section curves are tangent, then you have the option to specify
whether the resulting surfaces will also be tangent; specify TRUE to maintain
the tangency as seen in the section curves, FALSE otherwise; when generating
tangent surfaces, SolidWorks will maintain planar and cylindrical surface
shapes if the section curves exhibit these characteristics |
| Input: | (VARIANT_BOOL) forceNonRational | TRUE to force the resulting surface to be non-rational, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use of guide curves is recommended when selecting profiles in the FeatureManager
design tree.

You can use any number of profiles; however, if you have selected less
that three profiles, then any selected guide curves must be closed curves.

Use a SelectByMark method to select the profiles and guide curves. The
markfor the profile selections
should be a 1, while the mark for any guide curve selection, if provided,
should be a2.

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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__InsertCutBlend2.htm" >
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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Entity::SelectByMark$$**$$ModelDoc::SelectByMark$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__InsertCutBlend2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
