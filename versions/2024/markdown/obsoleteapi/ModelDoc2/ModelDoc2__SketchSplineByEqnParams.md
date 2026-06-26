---
title: "ModelDoc2::SketchSplineByEqnParams"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SketchSplineByEqnParams.htm"
---

# ModelDoc2::SketchSplineByEqnParams

This method is obsolete and has been superseded
by[SketchManager::CreateSplineByEqnParams](sldworksAPI.chm::/SketchManager/SketchManager__CreateSplineByEqnParams.htm).

Description

This method creates a spline on the active 2D sketch using the specified
b-curve parameters.

Syntax (OLE Automation)

Not available. See ModelDoc2::SketchSplineByEqnParams2.

Syntax (COM)

status = ModelDoc2->ISketchSplineByEqnParams
( propArray, knotsArray, cntrlPntCoordArray, &retval )

(Table)=========================================================

| Input: | (int*) propArray | Includes dimension, order, number of control points, and periodicity |
| --- | --- | --- |
| Input: | (double*) knotsArray | knot1, knot2, and so on |
| Input: | (double*) cntrlPntCoordArray | controlpoint1[dimension], controlpoint2[dimension], and so on |
| Output: | (BOOL) retval | TRUE if created successfully, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The propArray argument contains 4 integers packed into the first two
doubles in the SafeArray:

- Dimension
- Order
- Number of Control Points
- Periodicity ( TRUE or FALSE )

The knotsArray argument is an array of doubles with (Number of Control
Points + Order) elements.

The size of the cntrlPntCoordArray array is based upon the curve dimension:

- Dimension = 2 then each control point is an array
  of 2 doubles ( x, y )
- Dimension = 3 then each control point is an array
  of 3 doubles ( x, y, z)
- Dimension = 4 then each control point is an array
  of 4 doubles ( x, y, z, w ) where w = weight

The parameters are provided as 3 arrays, which for COM applications
are passed separately.

Pass control point coordinateskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}to
this method in sketch space. The Z value is interpreted as 0. In certain
situations, you must transform your b-curve parameters to sketch space
with the help of Sketch::ModelToSketchTransform.

NOTE:If the spline being generated
is a closed spline, then it must be flagged as periodic. In addition,
splines generated in sketches must be G1 continuous. If the data passed
to this method does not generate a G1 continuous spline, then it is rejected
and a spline is not created.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__SketchSplineByEqnParams.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__SketchSplineByEqnParams.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic5
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
<param name="Items" value="EXInsertSplineDrawing$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__SketchSplineByEqnParams.htm" >
<param name="_ID" value="RelatedTopic5" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
