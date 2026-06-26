---
title: "MateEntity::GetEntityParams"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MateEntity/MateEntity__GetEntityParams.htm"
---

# MateEntity::GetEntityParams

This method is obsolete and has been superseded
by[MateEntity2::EntityParams](sldworksAPI.chm::/MateEntity2/MateEntity2__EntityParams.htm).

Description

This method returns the parameters of this particular mate entity. Use
MateEntity::GetEntityType to know what parameters to expect.

Syntax (OLE Automation)

retval = MateEntity.GetEntityParams
()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray; this is an array of doubles representing
the mate entity parameters |
| --- | --- | --- |

Syntax (COM)

status = MateEntity->IGetEntityParams
( retval )

(Table)=========================================================

| Output: | (double*) retval | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value is the following array of doubles:

[pointX,
pointY, pointZ, vectorI, vectorJ, vectorK, radius1, radius2]

where

- pointXis the X location of this mate
  entity in the assembly model space
- pointYis the Y location of this mate
  entity in the assembly model space
- pointZis the Z location of this mate
  entity in the assembly model space
- vectorIis the i component of the assembly
  mate vector
- vectorJis the j component of the assembly
  mate vector
- vectorKis the k component of the assembly
  mate vector
- radius1is the value for the first
  radius
- radius2is the value for the second
  radius

To define the mate entity, the following information is returned based
upon the mate type. All coordinate information is given in terms of the
assembly coordinate system where the mate resides.

(Table)=========================================================

| Mate Type | Returned |
| --- | --- |
| swMatePoint | pointX, pointY, pointZ |
| swMateLine | pointX, pointY, pointZ, vectorI, vectorJ,
vectorK where the point is a point on the line and the vector represents
the line direction. |
| swMatePlane | pointX, pointY, pointZ, vectorI, vectorJ,
vectorK where the point is a point on the plane and the vector
represents the plane normal. |
| swMateCylinder | pointX, pointY, pointZ, vectorI, vectorJ,
vectorK, radius1 where the point is a point on the cylinder axis
and the vector represents the cylinder axis. |
| swMateCone | pointX, pointY, pointZ, vectorI, vectorJ,
vectorK, radius1, radius2 where the point is a point on the cone
axis and the vector represents the cone axis. |

To get to the
MateEntity interface, use Mate::GetMateEntities.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="MateEntity_Object$$**$$ZGetInfoMate$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\MateEntity\MateEntity__GetEntityParams.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
