---
title: "Component::GetTessNorms"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetTessNorms.htm"
---

# Component::GetTessNorms

This method is obsolete and has been superseded by[Component2::GetTessNorms](sldworksAPI.chm::/Component2/Component2__GetTessNorms.htm).

Description

This method returns the normal vector for each
of the triangles, which make up the shaded picture tessellation for the
component.

Syntax (OLE Automation)

retval = Component.GetTessNorms ()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = Component->IGetTessNorms ( retval )

(Table)=========================================================

| Output: | (float*) retval | Pointer to an array of floats |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Tessellation information is available only when the component is loaded
as lightweight.

The format of the returned data is:

- float
  x, y, z first point's unit normal
- float
  x, y, z second point's unit normal
- float
  x, y, z third point's unit normal

for the set of triangles for the component.

The total size of the data is [ 9 x sizeof(float)
x (number of triangles) ].

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\Component\Component__GetTessNorms.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
