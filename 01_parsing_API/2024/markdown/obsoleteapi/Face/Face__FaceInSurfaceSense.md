---
title: "Face::FaceInSurfaceSense"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__FaceInSurfaceSense.htm"
---

# Face::FaceInSurfaceSense

This
method is obsolete and has been superseded by[Face2::FaceInSurfaceSense](sldworksAPI.chm::/Face2/Face2__FaceInSurfaceSense.htm).

Description

This method checks if the face normal has the opposite direction (sense)
as the underlying surface.

Syntax (OLE Automation)

retval
= Face.FaceInSurfaceSense ()

(Table)=========================================================

| Return: | (BOOL)
retval | TRUE
if face normal and surface normal are in the opposite direction, FALSE
if face normal and surface normal are in same direction |
| --- | --- | --- |

Syntax (COM)

status
= Face->FaceInSurfaceSense ( &retval )

(Table)=========================================================

| Output: | (VARIANT_BOOL)
retval | TRUE
if face normal and surface normal are in the opposite direction, FALSE
if face normal and surface normal are in same direction |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

This method is important because the underlying surface geometry created
by parasolids can have an orientation with which its normal vector points
toward or away from the body material. The normal vector of faces, however,
is always directed away from the body material.

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
<param name="Items" value="Face_Object$$**$$ZGetInfoFace$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\sjesse\sw2001Plus\Face\Face__FaceInSurfaceSense.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
