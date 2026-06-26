---
title: "Modeler::CreateCylindricalSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Modeler/Modeler__CreateCylindricalSurface.htm"
---

# Modeler::CreateCylindricalSurface

This method is obsolete and has been superseded
by[Modeler::CreateCylindricalSurface2](sldworksAPI.chm::/Modeler/Modeler__CreateCylindricalSurface2.htm).

Description

This method creates an untrimmed cylindrical
surface from the specified arguments.

Syntax (OLE Automation)

retval = Modeler.CreateCylindricalSurface ( center,
direction, radius )

(Table)=========================================================

| Input: | (VARIANT) center | VARIANT of type SafeArray containing 3 doubles
(see Remarks ) |
| --- | --- | --- |
| Input: | (VARIANT) direction | VARIANT of type SafeArray containing
3 doubles (see Remarks ) |
| Input: | (double) radius | See Remarks |
| Return: | (LPDISPATCH) retval | Dispatch pointer to the resulting Surface object |

Syntax (COM)

status = Modeler->ICreateCylindricalSurface (
center, direction, radius, &retval )

(Table)=========================================================

| Input: | (double*) center | Pointer to an array of 3 doubles (see Remarks ) |
| --- | --- | --- |
| Input: | (double*) direction | Pointer to an array of 3 doubles (see Remarks ) |
| Input: | (double) radius | See Remarks |
| Output: | (LPSURFACE) retval | Pointer to the resulting Surface object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Input arguments:

- center
  – an XYZ location which represents the center of the bottom.
- direction
  – an XYZ direction of the axis of the cylindrical surface.
- radius
  – the radius at the center.

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\Modeler\Modeler__CreateCylindricalSurface.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
