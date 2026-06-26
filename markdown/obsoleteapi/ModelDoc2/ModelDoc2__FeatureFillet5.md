---
title: "ModelDoc2::FeatureFillet5"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__FeatureFillet5.htm"
---

# ModelDoc2::FeatureFillet5

This method is obsolete and has been superseded
by[FeatureManager::FeatureFillet](sldworksAPI.chm::/FeatureManager/FeatureManager__FeatureFillet.htm).

Description

This method creates an edge fillet feature.

Syntax (OLE Automation)

retval = ModelDoc2.FeatureFillet5 ( options, r1,
ftyp, overFlowType, radii, setBackDistances, pointRadiusArray )

(Table)=========================================================

| Input: | (long) options | Feature fillet option as defined in swFeatureFilletOptions_e |
| --- | --- | --- |
| Input: | (double) r1 | Radius for uniform radius edge fillet |
| Input: | (long) ftyp | 0
for simple fillet 1
for variable radius 2
for surface blend |
| Input: | (long) overFlowType | Control of fillet overflowing onto adjacent surfaces |
| Input: | (VARIANT) radii | Array containing the radii for variable radius fillet |
| Input: | (VARIANT) setBackDistances | Array containing setback distances for the fillet along the edge |
| Input: | (VARIANT) pointRadiusArray | Array containing radius values at various points along the length of
the edge; used by variable radius fillet |
| Output: | (long) retval | 1 if the fillet is created, 0 if it is not |

Syntax (COM)

status = ModelDoc2->IFeatureFillet5 ( options,
r1, ftyp, overFlowType, nRadii, radii, setbackDistCount, setBackDistances,
pointCount, pointRadiusArray, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (long) options | Feature fillet option as defined in swFeatureFilletOptions_e |
| --- | --- | --- |
| Input: | (double) r1 | Radius for uniform radius edge fillet |
| Input: | (long) ftyp | 0
for simple fillet 1
for variable radius 2
for surface blend |
| Input: | (long) overFlowType | Control of fillet overflowing onto adjacent surfaces |
| Input: | (long) nRadii | Number of radii for variable radius fillet |
| Input: | (double*) radii | Array containing the radii for variable radius
fillet of size nRadii |
| Input: | (long) setbackDistCount | Number of setback distances for the fillet along the edge |
| Input: | (double*) setBackDistances | Array containing setback distances for the
fillet along the edge of size setbackDistCount |
| Input: | (long) pointCount | Number of radius values at various points along the length of the edge |
| Input: | (double*) pointRadiusArray | Array of size pointCount |
| Output: | (long) retval | 1 if the fillet is created, 0 if it is not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The overFlowType argument
controls how the fillet behaves when it meets adjacent surfaces:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

- 0 - Default: System picks the appropriate method
  to create a fillet when the fillet surface overflows to adjacent surfaces.
  It either smoothly blends with adjacent surfaces or limits the fillet
  surface with the adjacent edges (thus not changing the edge), or trims
  the fillet surface by the adjacent surface onto which the fillet overflows.
  The method actually used by default depends on the geometric condition.
  This option always tries to create a fillet if possible.
- 1
  - Keep Edge: Edges that are overflowed by the fillet are not modified.
  The fillet surface is trimmed by all the adjacent edges. As a result,
  an additional transition fillet surface might be needed to complete the
  fillet.
- 2
  - Keep Surface: Fillet surface is either merged with the adjacent surfaces
  smoothly or trimmed by the adjacent surfaces. As a result, it is unlikely
  that an additional transition fillet surface is created.

For face blend fillets, the
first set of faces are selected with mark 2 and the second set of faces
by mark 4.

See the SolidWorks online
user's guide for details about setback fillets.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__FeatureFillet5.htm" >
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__FeatureFillet5.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
