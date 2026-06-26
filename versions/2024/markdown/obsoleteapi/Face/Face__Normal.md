---
title: "Face::Normal"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__Normal.htm"
---

# Face::Normal

This
property is obsolete and has been superseded by[Face2::Normal](sldworksAPI.chm::/Face2/Face2__Normal.htm).

Description

This read-only property gets the unit normal vector for any planar face.

Syntax (OLE Automation)

Normal
= Face.Normal (VB Get property)

Face.Normal
= Normal (VB Set property)

Normal
= Face.GetNormal ( ) (C++ Get property)

Face.SetNormal
( Normal ) (C++ Set property)

(Table)=========================================================

| Property: | (VARIANT)
Normal | VARIANT
of type SafeArray of 3 doubles (i,j,k) |
| --- | --- | --- |

Syntax (COM)

status
= Face->get_INormal( Normal)

(Table)=========================================================

| Property: | (double*)
Normal | Pointer
to an array of 3 doubles (i,j,k) |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

If this is not a planar face, then this property returns 0,0,0.

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
<param name="Items" value="Face_Object$$**$$ZGetInfoSurface$$**$$ZGetInfoFace$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Face\Face__Normal.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
