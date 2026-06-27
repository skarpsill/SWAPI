---
title: "Component::GetTessTriStripNorms"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetTessTriStripNorms.htm"
---

# Component::GetTessTriStripNorms

This
method is obsolete and has been superseded by[Component2::GetTessTriStripNorms](sldworksAPI.chm::/Component2/Component2__GetTessTriStripNorms.htm).

Description

This method gets the normal vector for each
of the triangles, which make up the shaded picture tessellation for this
component.

Syntax (OLE Automation)

retval = Component.GetTessTriStripNorms ()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray containing the tri-strip normals |
| --- | --- | --- |

Syntax (COM)

status = Component->IGetTessTriStripNorms ( retval
)

(Table)=========================================================

| Output: | (float*) retval | Pointer to an array of floats (see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Tessellation information is
available only when the component is loaded as lightweight.

The format of the returned data is:

- DWORDFaceCount
- DWORDStripCount
- DWORD (VertexCount)
  x 3
- DWORDNumStrips
- DWORD [VertexPerStrip]
  where this is an array from 0 to (Numstrips-1)
- Float
  [Normals]
  where this is an array of X,Y,Z normal components for each strip from
  0 to (VertexPerStrip-1)

where

- FaceCount= number of faces on
  the body
- StripCount= total number of
  strips on the body
- VertexCountx 3 = total number
  of vertices; multiplied by three to cover X,Y, and Z
- NumStrips= number of strips on
  a particular face
- VertexPerStrip= an array containing
  the number of vertex points on particular face strip
- NormalComp= an array of X,Y,Z
  normal components for each vertex on the particular face strip

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
<param name="Items" value="Component_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\Component\Component__GetTessTriStripNorms.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
