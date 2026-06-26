---
title: "Face::GetUVBounds"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetUVBounds.htm"
---

# Face::GetUVBounds

This
method is obsolete and has been superseded by[Face2::GetUVBounds](sldworksAPI.chm::/Face2/Face2__GetUVBounds.htm).

Description

Thismethodreturns values describing the U, V bounds of the face.

Syntax (OLE Automation)

retval
= Face.GetUVBounds ()

(Table)=========================================================

| Return: | (VARIANT)
retval | VARIANT
of type SafeArray (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status
= Face->IGetUVBounds ( &retval )

(Table)=========================================================

| Output: | (double*)
retval | Pointer
to an array of doubles (see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

These return values bound an area of the surface
in which the face is defined. Use Surface::Parameterization to determine
the surface U, V bounds.

The returned data is an array of 4 doubles arranged
in the following order:

retval[0] - Minimum U parameter of the face

retval[1] - Maximum U parameter of the face

retval[2] - Minimum V parameter of the face

retval[3] - Maximum V parameter of the face

The Minimum parameters is always less than the
Maximum parameters and the range (for example, retval[1] - retval[0] and
retval[3]-retval[2]) is always less than or equal to the U and V range
of the underlying surface.

For surfaces with periodic parameters, the face
parameter box can never be larger than the period of the corresponding
surface parameter.

uRange[0] <= retval[0] < uRange[1]

vRange[0] <= retval[2] < vRange[1] where
uRange and vRange describe the UV range of the surface

Therefore, a face that straddles the boundary of
a periodic parameter has an upper parameter value for the face that is
greater than the upper parameter range of the surface.

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
<param name="Items" value="Face_Object$$**$$ZGetInfoFace$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Face\Face__GetUVBounds.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
