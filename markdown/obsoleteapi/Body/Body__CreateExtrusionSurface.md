---
title: "Body::CreateExtrusionSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__CreateExtrusionSurface.htm"
---

# Body::CreateExtrusionSurface

This
method is obsolete and has been superseded by[Body2::CreateExtrusionSurface](sldworksAPI.chm::/Body2/Body2__CreateExtrusionSurface.htm).

Description

This method creates a new extrusion surface (infinitely long tabulated
cylinder).

Syntax (OLE Automation)

retval = Body.CreateExtrusionSurface
( profileCurve, axisDirection)

(Table)=========================================================

| Input: | (LPDISPATCH) profileCurve | Pointer to Dispatch object, the profile curve |
| --- | --- | --- |
| Input: | (VARIANT) axisDirection | VARIANT of type SafeArray of 3 doubles (x,y,z) |
| Return: | (LPDISPATCH) retval | Pointer to Dispatch object, a new surface of extrusion (tabulated cylinder) |

Syntax (COM)

status = Body->ICreateExtrusionSurfaceDLL(
profileCurve, axisDirection, &retval )

(Table)=========================================================

| Input: | (LPCURVE) profileCurve | Pointer to the profile curve |
| --- | --- | --- |
| Input: | (double*) axisDirection | Array of 3 doubles (x,y,z) |
| Output: | (LPSURFACE) retval | Pointer to the new surface of extrusion (tabulated cylinder) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is used with a set of related functions
that construct a body from trimmed surfaces.

The profileCurve argument is extruded along the
direction vector of axisDirection, the new surface being the envelope
of the curve. The profile curve must be a line, circle, or B-spline curve.

You can use this method with trimming curve creation
routines (for example, Surface::AddTrimmingLoop) to construct a trimmed
tabulated cylinder.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Body\Body__CreateExtrusionSurface.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
