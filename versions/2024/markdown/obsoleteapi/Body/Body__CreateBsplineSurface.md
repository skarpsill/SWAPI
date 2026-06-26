---
title: "Body::CreateBsplineSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__CreateBsplineSurface.htm"
---

# Body::CreateBsplineSurface

This method is obsolete and has been superseded by[Body2::CreateBsplineSurface](sldworksAPI.chm::/Body2/Body2__CreateBsplineSurface.htm).

Description

This function creates a new B-spline surface.

Syntax (OLE Automation)

retval
= Body.CreateBsplineSurface ( props, uKnots, vKnots, ctrlPtCoords)

(Table)=========================================================

| Input: | (VARIANT)
props | VARIANT
of type SafeArray containing 8 integers packed as 4 double elements (see Remarks ) |
| --- | --- | --- |
| Input: | (VARIANT)
uKnots | VARIANT
of type SafeArray of numUKnots doubles (see Remarks ) |
| Input: | (VARIANT)
vKnots | VARIANT
of type SafeArray of numVKnots doubles (see Remarks ) |
| Input: | (VARIANT)
ctrlPtCoords | VARIANT
of type SafeArray of numCtrlPtCoord doubles (see Remarks ) |
| Return: | (LPDISPATCH)
retval | pDispatch
pointer to dispatch object, a new B-spline surface |

Syntax (COM)

status
= Body->ICreateBsplineSurfaceDLL( props, uKnots, vKnots, ctrlPtCoords,
&retval )

(Table)=========================================================

| Input: | (long*)
props | Contains
8 longs (see Remarks ) |
| --- | --- | --- |
| Input: | (double*)
uKnots | Pointer
to an array of numUKnots doubles (see Remarks ) |
| Input: | (double*)
vKnots | Pointer
to an array of numVKnots doubles (see Remarks ) |
| Input: | (double*)
ctrlPtCoords | Pointer
to an array of numCtrlPtCoord doubles (see Remarks ) |
| Output: | (LPSURFACE)
retval | pointer
to the new B-spline surface |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

You can use this method with trimming curve creation routines (for example,
Surface::AddTrimmingLoop) to construct a trimmed surface.

The props array contains the following
elements (note that these are integers packed into a double array in the
Dispatch version):

- Uorder, Vorder
- numV_CtrlPoints, numU_CtrlPoints
- Uperiodicity, Vperiodicity
- DimensionControlPoints,
  UNUSED ( set =0 )

The number of elements in the uKnots array
is given by:

numUKnots = numU_CtrlPoints + Uorder

The number of elements in the vKnots array
is given by:

numVKnots = numV_CtrlPoints + Vorder

The number of elements in the ctrlPtCoords
array is given by:

numCtrlPtCoord =( NumV_CtrlPoints * NumU_CtrlPoints
* DimensionControlPoints )

For periodics, the first knot must have multiplicity set to 1 and all
excess multiplicity must be imposed on the last knot. Therefore, { 0,
1, 2, 3, 3, 3 } is a valid periodic knot vector for a cubic curve. The
control point on the seam of the closed curve cannot be replicated at
both ends; it should only occur at the beginning.

To convert from a clamped periodic curve (numKnots = numCtrlPts + Order,
ctrlPts replicated, knot multiplicity = order at each end) to a SolidWorks
periodic curve, remove all but one of the knots at the beginning of the
vector and remove one at the end and remove the last control point to
avoid point replication.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Body_Object$$**$$ZAccessorByCreate$$**$$ZCreateSurface$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\Body\Body__CreateBsplineSurface.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
