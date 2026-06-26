---
title: "Face::IGetFacetData"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__IGetFacetData.htm"
---

# Face::IGetFacetData

This
method is obsolete and has been superseded by[Face2::IGetFacetData](sldworksAPI.chm::/Face2/Face2__IGetFacetData.htm).

Description

Thismethodprovides direct access to the facet data of a face.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Face->IGetFacetData
( facetMesh, &nFacets, &nStrips, stripVertexNums, vertexCoords,
normalCoords )

(Table)=========================================================

| Input: | (int)facetMesh | Mesh to be output (see below) |
| --- | --- | --- |
| Output: | (int)nFacets | Total number of facets overall |
| Output: | (int)nStrips | Number of strips overall |
| Output: | (int)*stripVertexNums | Array of nStrips integers containing the number
of facet vertices in each facet strip |
| Output: | (float)*vertexCoords | Pointer to the vertex coordinates (see below) |
| Output: | (float)*normalCoords | Pointer to the normal coordinates (see below) |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This should provide
performance benefits over the GetTess* routines.

Before calling this
function, you should check whether the current facet information within
SolidWorks is valid. This can be done using ModelDoc2::IsTessellationValid.

IGetFacetData provides
direct access to facet data within SolidWorks. The values returned are
pointers that access SolidWorks memory addresses. Therefore, memory has
already been allocated by SolidWorks. This function will simply hand back
the pointer values for you to access the data. This is done to avoid the
overhead of copying data and to provide increased performance. This function
is unique and unlike any other API currently available in SolidWorks because
it exposes SolidWorks data directly to the calling application.

All arrays contain
internal SolidWorks data and should not be modified or freed.

The facet data obtained
from this function can be used until a RegenNotify is received or until[ModelDoc::IsTessellationValid](../ModelDoc/ModelDoc__IsTessellationValid.htm)returns FALSE. When a RegenNotify is received, you must recognize that
the facet data is invalid and flag yourself to reacquire the facet data
within one of the Repaint Notifications. In addition, if your application
is drawing to the SolidWorks display using this facet data, then you should
call[ModelDoc::IsTessellationValid](../ModelDoc/ModelDoc__IsTessellationValid.htm)before each use of the facet data.

Valid input values
for the factMesh argument are as follows:

-1: Returns data for the facet mesh that
SolidWorks is currently using

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0:
Returns the default SolidWorks mesh

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1:
Returns the reduced, less accurate mesh

The size of the vertexCoords
and normalCoords arrays is equal to (N * 3) where N is:

N = stripVertexNums[ 0 ] + ... + stripVertexNums[
nStrips - 1 ]

The vertex data (e.g.
vertex coords) is in the order:

Strip1Vertex1, Strip1Vertex2, ..., Strip1VertexM1,
Strip2Vertex1, ...

Strip1VertexM1 is the last vertex in the
first strip. M1 is therefore equal to stripVertexNums[0]

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
<param name="_CURRENTFILEPATH" value="D:\sjesse\sw2001Plus\Face\Face__IGetFacetData.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
