---
title: "Face::GetTessNorms"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetTessNorms.htm"
---

# Face::GetTessNorms

This
method is obsolete and has been superseded by[Face2::GetTessNorms](sldworksAPI.chm::/Face2/Face2__GetTessNorms.htm).

Description

Thismethodreturns
the normal vector for each of the triangles that make up the shaded picture
tessellation.

Syntax (OLE Automation)

retval = Face.GetTessNorms ()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray (see below) |
| --- | --- | --- |

Syntax
(COM)

status = Face->IGetTessNorms ( retval
)

(Table)=========================================================

| Output: | (float*) retval | Pointer to an array of floats (see below) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value for this method is in
the format:

float x, y, z - first point unit normal

float x, y, z - second point unit normal

float x, y, z - third point unit normal

where this data repeats itself for the set of triangles
on this face.

The total size of the data is[9 x sizeof(float) x (number of triangles)].

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
<param name="Items" value="Face_Object$$**$$ZTessellation$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Face\Face__GetTessNorms.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
