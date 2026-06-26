---
title: "Face::GetTessTriStripNorms"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetTessTriStripNorms.htm"
---

# Face::GetTessTriStripNorms

This
method is obsolete and has been superseded by[Face2::GetTessTriStripNorms](sldworksAPI.chm::/Face2/Face2__GetTessTriStripNorms.htm).

Description

Thismethodgives the normal vector for each of the triangles which make up
the shaded picture tessellation for this face.

Syntax (OLE Automation)

retval = Face.GetTessTriStripNorms
()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray containing
the tristrip normals |
| --- | --- | --- |

Syntax (COM)

status = Face->IGetTessTriStripNorms
( retval )

(Table)=========================================================

| Output: | (float*) retval | Pointer to an array of floats (see below) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The format of the return data is:

DWORD NumStrips

DWORD [VertexPerStrip] where this is an
array from 0 to (Numstrips-1)

Float [Normals ] where this is an array
of X,Y,Z normal components for each strip from 0 to (VertexPerStrip-1)

where:

NumStrips = number of strips on a particular
face

VertexPerStrip = an array containing
the number of vertex points on particular face strip

NormalComp = an array of X,Y,Z normal
components for each vertex on the particular face strip

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
<param name="Items" value="Face_Object$$**$$ZTesselation$$**$$ZTessellat$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Face\Face__GetTessTriStripNorms.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
