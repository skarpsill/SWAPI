---
title: "ModelDoc::CreatePlaneFixed"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreatePlaneFixed.htm"
---

# ModelDoc::CreatePlaneFixed

This
method is obsolete and has been superseded by[ModelDoc2::CreatePlaneFixed](../ModelDoc2/ModelDoc2__ICreatePlaneFixed.htm).

Description

This method creates a fixed reference plane through three points. The
resulting plane is not parametric.

Syntax (OLE Automation)

retval = ModelDoc.CreatePlaneFixed
( P1, P2, P3, useGlobal)

(Table)=========================================================

| Input: | (VARIANT) P1 | VARIANT of type SafeArray of 3 doubles (x1, y1, z1) in meters; this
is the first of three model-space points used to define the plane orientation;
it can also be used as the origin for the plane coordinate system |
| --- | --- | --- |
| Input: | (VARIANT) P2 | VARIANT of type SafeArray of 3 doubles (x2, y2, z2) in meters; this
is the second of three model-space points used to define the plane orientation;
it can also be used to determine the direction of the plane's X-axis;
the plane's X-axis will be directed from P1 to P2 unless useGlobal is
set to TRUE |
| Input: | (VARIANT) P3 | VARIANT of type SafeArray of 3 doubles (x3, y3, z3) in meters; this
is the final model-space point used to define the plane orientation |
| Input: | (BOOL) useGlobal | Flag controlling X-axis orientation |
| Return: | (BOOL) retval | TRUE if plane is created successfully, FALSE if not |

Syntax (COM)

status = ModelDoc->ICreatePlaneFixed
( P1, P2, P3, useGlobal )

(Table)=========================================================

| Input: | (double*) P1 | Pointer to an array of 3 doubles (x1, y1, z1) in meters; this is the
first of three model-space points used to define the plane orientation;
it can also be used as the origin for the plane coordinate system |
| --- | --- | --- |
| Input: | (double*) P2 | Pointer to an array of 3 doubles (x2, y2, z2) in meters; this is the
second of three model-space points used to define the plane orientation;
it can also be used to determine the direction of the plane's X-axis;
the plane's X-axis will be directed from P1 to P2 unless useGlobal is
set to TRUE |
| Input: | (double*) P3 | Pointer to an array of type SafeArray of 3 doubles (x3, y3, z3) in meters;
this is the final model-space point used to define the plane orientation |
| Input: | (VARIANT_BOOL) useGlobal | Flag controlling X-axis orientation |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The planes normal vector is calculated using the cross product of the
vectors (P2 - P1) and (P3 - P1), respectively.

The X-axis of the planes coordinate system is a vector from P1 to P2,
or it is a vector that was projected from the X-axis of the global coordinate
system onto the plane.

TheuseGlobalargument denotes whether to align the X-axis
of the plane with global orientation. If set to TRUE, then the X-axis
of the global (model) coordinate system is projected onto the plane. That
vector is used to determine the direction of the plane's X-axis. This
does not reorient the plane. Instead, it rotates the plane coordinate
system about P1 until the X-axis of the plane aligns with the projected
vector. P1, P2, and P3 are still required because they define the plane.
If FALSE, then the X-axis of the plane iskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}aligned
based on your input points: P1 and P2.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name=_Version value="65536" >
<param name=_ExtentX value="1323" >
<param name=_ExtentY value="556" >
<param name=_StockProps value="13" >
<param name=ForeColor value="0" >
<param name=BackColor value="13160660" >
<param name=UseButton value="0" >
<param name=ControlLabel value="See Also" >
<param name=UseIcon value="0" >
<param name=Items value="ModelDoc_Object$$**$$ZCreateRefPlane$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="C:\Home\Oneill\ModelDoc\ModelDoc__CreatePlaneFixed.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan
