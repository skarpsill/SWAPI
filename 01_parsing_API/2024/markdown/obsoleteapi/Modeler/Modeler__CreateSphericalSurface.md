---
title: "Modeler::CreateSphericalSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Modeler/Modeler__CreateSphericalSurface.htm"
---

# Modeler::CreateSphericalSurface

This method is obsolete and has been superseded
by[Modeler::CreateSphericalSurface2](sldworksAPI.chm::/Modeler/Modeler__CreateSphericalSurface2.htm).

Description

This method creates an untrimmed spherical
surface from the specified arguments.

Syntax (OLE Automation)

retval = Modeler.CreateSphericalSurface ( center,
radius )

(Table)=========================================================

| Input: | (VARIANT) center | VARIANT of type SafeArray containing 3 doubles (see Remarks ) |
| --- | --- | --- |
| Input: | (double) radius | See Remarks |
| Return: | (LPDISPATCH) retval | Dispatch pointer to the resulting surface |

Syntax (COM)

status = Modeler->ICreateSphericalSurface ( center,
radius, &retval )

(Table)=========================================================

| Input: | (double*) center | Pointer to an array of 3 doubles (see Remarks ) |
| --- | --- | --- |
| Input: | (double) radius | See Remarks |
| Output: | (LPSURFACE) retval | Pointer to the resulting surface |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Input arguments:

- center
  – an XYZ location which represents the center of the spherical surface.
- radius
  – the radius at the center.

You can trim the resulting surface can be
trimmed using, for example, Surface::CreateTrimmedSheet, to generate a
sheet body.

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
<param name="Items" value="Modeler_Object$$**$$ZSewingRoutinesNEW$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\Modeler\Modeler__CreateSphericalSurface.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
