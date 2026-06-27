---
title: "Modeler::ICreateBrepBody2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Modeler/Modeler__ICreateBrepBody2.htm"
---

# Modeler::ICreateBrepBody2

This method is obsolete and has been superseded
by[Modeler::CreateBrepBody3](sldworksAPI.chm::/Modeler/Modeler__CreateBrepBody3.htm).

Description

This method creates a body from BREP data.

Syntax (OLE Automation)

See[Modeler::CreateBrepBody](Modeler__CreateBrepBody.htm).

Syntax (COM)

status = Modeler->ICreateBrepBody2 ( type, nTopologies,
*topologies, edgeTolArray, vertexTolArray, pointArray, curveArray, surfaceArray,
nRelations, *parents, *children, *senses, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (int) type | Type of body to create as defined in swTopology_e |
| --- | --- | --- |
| Input: | (int) nTopologies | Number of topological entities in the topologies argument |
| Input: | (int) *topologies | Array of topologies (see swTopoEntity_e), one for each topological entity |
| Input: | (double*) edgeTolArray | Array of tolerances for edges |
| Input: | (double*) vertexTolArray | Array of tolerances for vertices |
| Input: | (double*) pointArray | Array of coordinates of vertices (geometry for vertices) |
| Input: | (LPCURVE*) curveArray | Array of curves (geometry for edges) |
| Input: | (LPSURFACE*) surfaceArray | Array of surfaces (geometry for faces) |
| Input: | (int) nRelations | Number of 1-to-1 relationships between topological entities |
| Input: | (int) *parents | Array of parents, one in each relationship |
| Input: | (int) *children | Array of children, one in each relationship |
| Input: | (int) *senses | Array of senses in which child is used by parent in the relationship |
| Output: | (LPBODY2) retval | Pointer to the resulting Body2 object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If non-negative values are packed into the edgeTolArrayand vertexTolArray arrays, then tolerances
are applied to the corresponding edges or vertices. These arrays should
be the same size as curveArray and pointArray, respectively. Otherwise
a default value of 1.0e-8 (modeler precision) is used.

NOTE: Modeler::SetInitKnitGapWidth
does not affect this method.

Useful functions for creating geometry for the topological entities
are:

- Body2::CreatePlanarSurface
- Body2::AddProfileArc
- Body2::AddProfileLine
- Body2::CreateRevolutionSurface

For example, to create a cone, find topological
relationships and form relevant arrays. A complete solid cone consists
of 8 topological entities:

There are 8 relations:

The topologies array:

(Table)=========================================================

| Index | Value |
| --- | --- |
| 0 | swTopoShell |
| 1 | swTopoFace |
| 2 | swTopoFace |
| 3 | swTopoLoop |
| 4 | swTopoEdge |
| 5 | swTopoLoop |
| 6 | swTopoLoop |
| 7 | swTopoVertex |

The set of arrays:

(Table)=========================================================

| index | parents | children | senses | relation |
| --- | --- | --- | --- | --- |
| 0 | 0 | 1 | 0 | shell to face |
| 1 | 0 | 2 | 0 | shell to face |
| 2 | 1 | 3 | 0 | face to loop |
| 3 | 3 | 4 | -1 | loop to edge |
| 4 | 2 | 5 | 0 | face to loop |
| 5 | 2 | 6 | 0 | face to loop |
| 6 | 5 | 4 | 1 | loop to edge |
| 7 | 6 | 7 | 0 | loop to vertex |

Values in the parents and children arrays correspond to the indices
of the topology array.

Every shell should be a closed shell. Sheet bodies should have additional
back faces to form a closed shell. When creating a sheet body, these extra
back faces are retained in the result and should be removed using Modeler::DeleteFacesFromSheetBody
.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Modeler\Modeler__ICreateBrepBody2.htm" >
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
<param name="Items" value="Modeler Method$$**$$Body2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Modeler\Modeler__ICreateBrepBody2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
