---
title: "Component::GetTessTriStrips"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetTessTriStrips.htm"
---

# Component::GetTessTriStrips

This
method is obsolete and has been superseded by[Component2::GetTessTriStrips](sldworksAPI.chm::/Component2/Component2__GetTessTriStrips.htm).

Description

This method returns the vertices that make up the shaded picture tessellation
for this component.

Syntax (OLE Automation)

retval = Component.GetTessTriStrips (noConversion)

(Table)=========================================================

| Input: | (BOOL) noConversion | TRUE prohibits conversion to user units from system units, FALSE does
not |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray (see Remarks ) |

Syntax (COM)

status = Component->IGetTessTriStrips ( noConversion,
retval )

(Table)=========================================================

| Input: | (VARIANT_BOOL) noConversion | TRUE prohibits conversion to user units from system units, FALSE does
not |
| --- | --- | --- |
| Output: | (float*) retval | Pointer to an array of floats (see Remarks ) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Vertices are all unique for that strip. A vertex
that is shared by two tessellation triangles appears only once in the
VARIANT return value.

Tessellation information is available only when
the component is loaded as lightweight.

These triangles are intended for graphical display
purposes and do not represent a tessellation that can be used, for example,
by a machining application. If you need the type of accuracy associated
with a machining product, we recommend that you traverse the body faces
and extract the topology and geometry data to create your own faceting.

The format of the returned data is:

- DWORDFaceCount
- DWORDStripCount
- DWORD (VertexCount)
  x 3
- DWORDNumStrips
- DWORD [VertexPerStrip]
  where this is an array from 0 to (Numstrips-1)
- Float[VertexPoints] where this is an array
  X,Y,Z for each strip from 0 to (VertexPerStrip-1)

where:

- FaceCount= number of faces on the body
- StripCount= total number of strips on the body
- VertexCountx 3 = total number of vertices. Multiplied by three to cover X,Y, and
  Z
- NumStrips=
  number of strips on a particular face
- VertexPerStrip=
  an array containing the number of vertex points on particular face strip
- VertexPoints=
  an array of X,Y,Z points for each vertex on the particular face strip

Because the returned array elements are of type float (or type single
in VB), andFaceCount, StripCount, VertexCount,
NumStripsand the elements ofVertexPerStripare integers that have been packed into the return array elements, you
must unpack them before you can use them.

For example:

- sa[0] = number of faces
- sa[1] = total number of strips
- sa[2] = total number of vertices x 3 (data values)

For each face:

- sa[3] = number of strips in this face
- sa[4]
  = number of vertices in first strip of this face
- sa[5] = number of vertices in second
  strip of this face

...

- sa[3
  + sa[3]] = number of vertices in last strip of this face

For each strip, i:

- kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sa[3
  + sa[3] + 1] = X value of first vertex in this strip of the face
- kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sa[3
  + sa[3] + 2] = Y value of first vertex in this strip of the face
- kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sa[3
  + sa[3] + 3] = Z value of first vertex in this strip of the face
- kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sa[3
  + sa[3] + 4] = X value of second vertex in this strip of the face

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}...

- kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sa[3
  + sa[3] + (sa[3+i] x 3)] = Z value of last vertex in this strip of the
  face

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\Component\Component__GetTessTriStrips.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
