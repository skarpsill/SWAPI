---
title: "ModelDoc::InsertLoftRefSurface2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertLoftRefSurface2.htm"
---

# ModelDoc::InsertLoftRefSurface2

This
method is obsolete and has been superseded by[ModelDoc2::InsertLoftRefSurface2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertLoftRefSurface2.htm).

Description

This method creates a lofted surface from the selected profiles, centerline,
and guide curves.

Syntax (OLE Automation)

(void) ModelDoc.InsertLoftRefSurface2
( closed, keepTangency, forceNonRational, tessToleranceFactor, startMatchingType,
endMatchingType )

(Table)=========================================================

| Input: | (BOOLEAN) closed | TRUE if you want the loft to be closed, FALSE if the loft will be open;
if TRUE, then you must have at least three profiles selected, and if you
are using guide curves, the guide curves must be closed |
| --- | --- | --- |
| Input: | (BOOLEAN) keepTangency | If the section curves are tangent, then you have the option to specify
whether the resulting surfaces will also be tangent; specify TRUE to maintain
the tangency as seen in the section curves, FALSE otherwise; when generating
tangent surfaces, SolidWorks will maintain planar and cylindrical surface
shapes if the section curves exhibit these characteristics |
| Input: | (BOOLEAN) forceNonRational | TRUE to force the resulting surface to be non-rational, FALSE otherwise |
| Input: | (double) tessToleranceFactor | A factor to control the number of intermediate sections used for loft
with centerline; the default value is 1.0; the greater the variable, the
more intermediate sections are created |
| Input: | (short) startMatchingType | Tangency type at the start profile |
| Input: | (short) endMatchingType | Tangency type at the start profile |

Syntax (COM)

status = ModelDoc->InsertLoftRefSurface2
( closed, keepTangency, forceNonRational, tessToleranceFactor, startMatchingType,
endMatchingType )

(Table)=========================================================

| Input: | (VARIANT_BOOL) closed | TRUE if you want the loft to be closed, FALSE if the loft will be open;
if TRUE, then you must have at least three profiles selected, and if you
are using guide curves, the guide curves must be closed |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) keepTangency | If the section curves are tangent, then you have the option to specify
whether the resulting surfaces will also be tangent; specify TRUE to maintain
the tangency as seen in the section curves, FALSE otherwise; when generating
tangent surfaces, SolidWorks will maintain planar and cylindrical surface
shapes if the section curves exhibit these characteristics |
| Input: | (VARIANT_BOOL) forceNonRational | TRUE to force the resulting surface to be non-rational, FALSE
otherwise |
| Input: | (double) tessToleranceFactor | A factor to control the number of intermediate sections used for loft
with centerline; the default value is 1; the greater the variable, the
more intermediate sections are created |
| Input: | (short) startMatchingType | Tangency type at the start profile |
| Input: | (short) endMatchingType | Tangency type at the start profile |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Selection of guide curves and centerline is optional; however, selection
of the profiles must be in an order consistent with the desired direction
of the loft. Because you are creating a surface, the section profiles
can be open.

Use of guide curves is recommended when selection of profiles is done
in the FeatureManager design tree.

You can use any number of profiles; however, if you have selected only
one profile, then any selected guide curves must be closed curves.

Use SelectByMark and AndSelectByMark to select the profiles and guide
curves. The mark for the profile selections should be a 1, the mark for
any guide curve selection, if provided, should be a 2; the mark for the
centerline selection, if provided, should be a 4; the mark for the start
tangency vector selection, if provided, should be an 8; the mark for the
start tangency faces selection, if provided, should be a 16 (not currently
available); the mark for the end tangency vector selection, if provided,
should be a 32; the mark for the end tangency faces selection, if provided,
should be a 64 (not currently available). Linear edge, sketch line, axis,
plane, and planar faces are qualified for tangency vector sections.

The tangency types can be one of the following:

(Table)=========================================================

| 0 | None |
| --- | --- |
| 1 | Tangent to the normal of the profile |
| 2 | Tangent to a selected vector |
| 3 | Tangency to all the adjacent faces sharing an edge with the start profile |
| 4 | Tangent to some of the selected faces sharing an edge with the start
profile (not currently available) |

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZCreateRefSurface$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\ModelDoc\ModelDoc__InsertLoftRefSurface2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Entity::SelectByMark$$**$$ModelDoc::SelectByMark$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\ModelDoc\ModelDoc__InsertLoftRefSurface2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Entity::SelectByMark$$**$$ModelDoc::AndSelectByMark$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2005\obsoleteapi\ModelDoc\ModelDoc__InsertLoftRefSurface2.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
