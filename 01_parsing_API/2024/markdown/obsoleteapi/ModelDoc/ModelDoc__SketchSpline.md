---
title: "ModelDoc::SketchSpline"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchSpline.htm"
---

# ModelDoc::SketchSpline

This method is obsolete
and has been superseded by[ModelDoc2::SketchSpline](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SketchSpline.htm).

Description

This method creates a spline, or continues
one, passing through the point (x, y, z). See alsokadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ModelDoc::CreateSpline.

Syntax (OLE Automation)

void ModelDoc.SketchSpline ( morePts,
x, y, z)

(Table)=========================================================

| Input: | (long) morePts | Number of points left to specify after this point |
| --- | --- | --- |
| Input: | (double) x | x coordinate of point in meters |
| Input: | (double) y | y coordinate of point in meters |
| Input: | (double) z | z coordinate of point in meters |

Syntax (COM)

status = ModelDoc->SketchSpline
( morePts, x, y, z )

(Table)=========================================================

| Input: | (long) morePts | Number of points left to specify after this point |
| --- | --- | --- |
| Input: | (double) x | x coordinate of point in meters |
| Input: | (double) y | y coordinate of point in meters |
| Input: | (double) z | z coordinate of point in meters |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If you are creating a sketch spline from a macro,
then you must use ModelDoc::SketchSpline. You cannot use ModelDoc::CreateSpline
because it requires an array of points.

In 2D sketches, SolidWorks ignores the z value.

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
<param name="Items" value="ModelDoc_Object$$**$$ZCreateSketchEntity$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc\ModelDoc__SketchSpline.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
