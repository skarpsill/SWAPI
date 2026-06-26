---
title: "Component::GetTessTriangles"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetTessTriangles.htm"
---

# Component::GetTessTriangles

This
method is obsolete and has been superseded by[Component2::GetTessTriangles](sldworksAPI.chm::/Component2/Component2__GetTessTriangles.htm).

Description

This method returns the triangles that make
up the shaded picture tessellation for this component.

Syntax (OLE Automation)

retval = Component.GetTessTriangles (noConversion)

(Table)=========================================================

| Input: | (BOOL) noConversion | TRUE prohibits conversion to user units from system units, FALSE does
not |
| --- | --- | --- |
| Return: | (VARIANT) retval | VARIANT of type SafeArray (see Remarks ) |

Syntax (COM)

status = Component->IGetTessTriangles ( noConversion,
retval )

(Table)=========================================================

| Input: | (VARIANT_BOOL) noConversion | TRUE prohibits conversion to user units from system units, FALSE does
not |
| --- | --- | --- |
| Output: | (float*) retval | Pointer to array of floats (see Remarks ) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Tessellation information is
available only when the component is loaded as lightweight.

These triangles are intended for graphical display purposes and do not
represent a tessellation that an be used, for example, by a machining
application. If you need the type of accuracy associated with a machining
product, we recommend that you traverse the body faces and extract the
topology and geometry data to create your own faceting.

The format of the returned data is:

- float x, y, z first
  point in meters
- float x, y, z second
  point in meters
- float x, y, z third
  point in meters

for the set of triangles for the component.

The total size of the data is[9 x sizeof(float)
x (number of triangles)].

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\Component\Component__GetTessTriangles.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
