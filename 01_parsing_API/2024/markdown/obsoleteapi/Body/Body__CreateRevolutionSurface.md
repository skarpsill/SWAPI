---
title: "Body::CreateRevolutionSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__CreateRevolutionSurface.htm"
---

# Body::CreateRevolutionSurface

This
method is obsolete and has been superseded by[Body2::CreateRevolutionSurface](sldworksAPI.chm::/Body2/Body2__CreateRevolutionSurface.htm).

Description

This method creates a new surface of revolution.

Syntax (OLE Automation)

retval = Body.CreateRevolutionSurface ( profileCurve,
axisPoint, axisDirection, profileEndPtParams)

(Table)=========================================================

| Input: | (LPDISPATCH)
profileCurve | Pointer
to a Dispatch object, the profile curve (generatrix) |
| --- | --- | --- |
| Input: | (VARIANT)
axisPoint | VARIANT
of type SafeArray of 3 doubles (x,y,z) |
| Input: | (VARIANT)
axisDirection | VARIANT
of type SafeArray of 3 doubles (x,y,z) |
| Input: | (VARIANT)
profileEndPtParams | VARIANT
of type SafeArray of 2 doubles (uStart,uEnd) (see Remarks ) |
| Return: | (LPDISPATCH)
retval | Dispatch
pointer to dispatch object, a new surface of revolution |

Syntax (COM)

status = Body->ICreateRevolutionSurface ( profileCurve,
axisPoint, axisDirection, profileEndPtParams, &retval )

(Table)=========================================================

| Input: | (LPCURVE)
profileCurve | Pointer
to a Dispatch object, the profile curve (generatrix) |
| --- | --- | --- |
| Input: | (VARIANT)
axisPoint | VARIANT
of type SafeArray of 3 doubles (x,y,z) |
| Input: | (VARIANT)
axisDirection | VARIANT
of type SafeArray of 3 doubles (x,y,z) |
| Input: | (VARIANT)
profileEndPtParams | VARIANT
of type SafeArray of 2 doubles (uStart,uEnd) (see Remarks ) |
| Output: | (LPSURFACE*)
retval | Pointer
to a new surface of revolution |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

You can use this method in conjunction with a set
of related functions that construct a body from trimmed surfaces. If you
pass in profileEndPtParams, SolidWorks trims the surface in the axial
direction, otherwise it will be infinite. SolidWorks closes the surface
periodic (period [0,2PI]) in the direction of revolution.

You can also use this function in conjunction with
trimming curve creation routines (for example, Surface::AddTrimmingLoop)
to construct a trimmed surface of revolution.

The profileEndPtParams parameters indicate which
part of the curve to spin. SolidWorks uses these parameters only when
the profile curve intersects the revolve axis. You must specify the parameters
in ascending order. SolidWorks extends the curve from the given parameter
range to meet the revolve axis and spins this portion of curve.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\Body\Body__CreateRevolutionSurface.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
