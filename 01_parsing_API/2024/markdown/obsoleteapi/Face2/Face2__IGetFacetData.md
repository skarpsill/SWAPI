---
title: "Face2::IGetFacetData"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face2/Face2__IGetFacetData.htm"
---

# Face2::IGetFacetData

This method is obsolete and was not replaced.
Use these methods in its place:

- [Face2::GetTessNorms](sldworksAPI.chm::/Face2/Face2__GetTessNorms.htm)
- [Face2::GetTessTextures](sldworksAPI.chm::/Face2/Face2__GetTessTextures.htm)
- [Face2::GetTriangleCount](sldworksAPI.chm::/Face2/Face2__GetTessTriangleCount.htm)
- [Face2::GetTriangles](sldworksAPI.chm::/Face2/Face2__GetTessTriangles.htm)
- [Face2::GetTessTriStripEdges](sldworksAPI.chm::/Face2/Face2__GetTessTriStripEdges.htm)
- [Face2::GetTessTriStripNorms](sldworksAPI.chm::/Face2/Face2__GetTessTriStripNorms.htm)
- [Face2::GetTessTriStrips](sldworksAPI.chm::/Face2/Face2__GetTessTriStrips.htm)
- [Face2::GetTessTriStripSize](sldworksAPI.chm::/Face2/Face2__GetTessTriStripSize.htm)

Description

This method provides direct access to the facet
data of a face.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Face2->IGetFacetData ( facetMesh, &nFacets,
&nStrips, stripVertexNums, vertexCoords, normalCoords )

(Table)=========================================================

| Input: | (int) facetMesh | Mesh to be output: - 1 - Returns data for the facet mesh
currently used by SolidWorks 0
- Returns the default SolidWorks mesh 1
- Returns the reduced, less accurate mesh |
| --- | --- | --- |
| Output: | (int) nFacets | Total number of facets overall |
| Output: | (int) nStrips | Number of strips overall |
| Output: | (int)*stripVertexNums | Array of nStrips integers containing the number
of facet vertices in each facet strip |
| Output: | (float)*vertexCoords | Pointer to the vertex coordinates |
| Output: | (float)*normalCoords | Pointer to the normal coordinates |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Before
calling this function, check whether the current facet information within
SolidWorks is valid using ModelDoc2::IsTessellationValid.

Face2::IGetFacetData
provides direct access to facet data within SolidWorks. The values returned
are pointers that access SolidWorks memory addresses. Therefore, memory
has already been allocated by SolidWorks. This method hands back the pointer
values for you to access the data. This is done to avoid the overhead
of copying data and to provide increased performance. This method is unique
and unlike any other method currently available in SolidWorks because
it exposes SolidWorks data directly to the calling application.

All arrays contain
internal SolidWorks data should not be modified or freed.

You can use the facet
data from this method until you receive RegenNotify or ModelDoc2::IsTessellationValid
returns FALSE. When you receive RegenNotify, the facet data is invalid
and you need to reacquire the facet data within one of the repaint notifications.
If your application is drawing to the SolidWorks display using this facet
data, call ModelDoc2::IsTessellationValid before each use of the facet
data.

The size of the vertexCoords
and normalCoords arrays is equal to (N * 3) where N is:

N = stripVertexNums[ 0 ] + ... + stripVertexNums[
nStrips - 1 ]

The vertex data (for
example, vertex coordinates) is in the order:

Strip1Vertex1, Strip1Vertex2, ..., Strip1VertexM1,
Strip2Vertex1, ...

Strip1VertexM1 is the last vertex in the
first strip. M1 is equal to stripVertexNums[0].

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\Face2\Face2__IGetFacetData.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Face2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\Face2\Face2__IGetFacetData.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
