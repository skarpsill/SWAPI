---
title: "Face::GetTessTriStripEdges"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetTessTriStripEdges.htm"
---

# Face::GetTessTriStripEdges

This
method is obsolete and has been superseded by[Face2::GetTessTriStripEdges](sldworksAPI.chm::/Face2/Face2__GetTessTriStripEdges.htm).

Description

Thismethodgives the edge ID for each of the edges in the triangles that make
up the tessellation for this face.

Syntax (OLE Automation)

retval = Face.GetTessTriStripEdges ()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray of type long containing
the list of edge IDs for this face |
| --- | --- | --- |

Syntax (COM)

status = Face->IGetTessTriStripEdges (retval )

(Table)=========================================================

| Output: | (long*) retval | Pointer to an array of type long containing the
list of edge IDs for this face |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

A zero value for edge ID indicates that there is no corresponding model
edge.

The format of the returned data is:

(Table)=========================================================

| DWORD NumStrips | Number of strips on a particular face. |
| --- | --- |
| DWORD [StripLengths] | Array containing the number from 0 to (NumStrips-1) of vertex points
on particular face strip. |
| ForEach Strip | Array of edge IDs for each vertex on the particular face strip. |
| Long [EdgeIds] | Array of edge IDs for each strip from 1 to (VertexPerStrip-1). Element
0 indicates if it is a triangle strip (value = 1) or a single triangle
(value = 0). |

For triangle strips, EdgeIds is:

If the strip has n vertices, then there
is 2(n – 2) + 1 edge tags. The i-th element of the tags array (starting
at i = 1) is the tag of the edge between vertex floor((i – 1) / 2) + 1
and vertex floor(i/2) + 2, where floor(x) is the integer portion of x.

For single triangles, EdgeIds is:

The i-th element of the tags array (starting
at i = 1) is the tag of the edge between vertex i-1 (if i=1 then i=n)
and vertex i.

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
<param name="Items" value="Face_Object$$**$$ZTessellation$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Face\Face__GetTessTriStripEdges.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
