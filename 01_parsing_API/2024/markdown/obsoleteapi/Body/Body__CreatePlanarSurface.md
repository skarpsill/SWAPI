---
title: "Body::CreatePlanarSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__CreatePlanarSurface.htm"
---

# Body::CreatePlanarSurface

This method is obsolete and has been superseded by[Body2::CreatePlanarSurface](sldworksAPI.chm::/Body2/Body2__CreatePlanarSurface.htm).

Description

This method creates a new infinite planar surface.

Syntax (OLE Automation)

retval
= Body.CreatePlanarSurface ( vRootPoint, vNormal)

(Table)=========================================================

| Input: | (VARIANT)
vRootPoint | VARIANT
of type SafeArray of 3 doubles (x,y,z) |
| --- | --- | --- |
| Input: | (VARIANT)
vNormal | VARIANT
of type SafeArray of 3 doubles (x,y,z) |
| Return: | (LPDISPATCH)
retval | Dispatch
pointer to dispatch object, a new planar surface |

Syntax (COM)

status = Body->ICreatePlanarSurfaceDLL
( vRootPoint, vNormal, &retval )

(Table)=========================================================

| Input: | (double*) vRootPoint | Pointer to an array of 3 doubles (x,y,z) |
| --- | --- | --- |
| Input: | (double*) vNormal | Pointer to an array of 3 doubles (x,y,z) |
| Output: | (LPSURFACE) retval | Pointer to the new planar surface |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

You can use this method with:

- A set of related functions that construct a body
  from trimmed surfaces.
- Trimming curve creation routines (for example,
  Surface::AddTrimmingLoop) to construct a trimmed surface.

Also. see Body::ICreatePlanarTrimSurfaceDLL, which allows you to create
a planar trimmed surface directly from the vertex points.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Body\Body__CreatePlanarSurface.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
