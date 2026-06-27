---
title: "Modeler::CreateConicalSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Modeler/Modeler__CreateConicalSurface.htm"
---

# Modeler::CreateConicalSurface

This
method is obsolete and has been superseded by[Modeler::CreateConicalSurface2](sldworksAPI.chm::/Modeler/Modeler__CreateConicalSurface2.htm).

Description

This method creates an untrimmed conical surface
from the specified arguments.

Syntax (OLE Automation)

retval = Modeler.CreateConicalSurface ( center, direction,
radius, semiAngle )

(Table)=========================================================

| Input: | (VARIANT) center | VARIANT of type SafeArray containing 3 doubles
(see Remarks ) |
| --- | --- | --- |
| Input: | (VARIANT) direction | VARIANT of type SafeArray containing 3 doubles
(see Remarks ) |
| Input: | (double) radius | (see Remarks ) |
| Input: | (double) semiAngle | (see Remarks ) |
| Return: | (LPDISPATCH) retval | Dispatch pointer to the resulting Surface object |

Syntax (COM)

status = Modeler->ICreateConicalSurface ( center,
direction, radius, semiAngle, &retval )

(Table)=========================================================

| Input: | (double*) center | Pointer to an array of 3 doubles (see Remarks ) |
| --- | --- | --- |
| Input: | (double*) direction | Pointer to an array of 3 doubles (see Remarks ) |
| Input: | (double) radius | (see Remarks ) |
| Input: | (double) semiAngle | (see Remarks ) |
| Output: | (LPSURFACE) retval | Pointer to the resulting Surface object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The input arguments are:

- center
  – an XYZ location that represents the center of the bottom.
- direction
  – an XYZ direction of the axis of the conical surface.
- radius
  – the radius at the center.
- semiAngle
  – the half angle of the cone in radians.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\Modeler\Modeler__CreateConicalSurface.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
