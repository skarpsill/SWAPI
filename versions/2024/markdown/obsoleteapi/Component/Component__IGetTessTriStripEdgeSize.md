---
title: "Component::IGetTessTriStripEdgeSize"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__IGetTessTriStripEdgeSize.htm"
---

# Component::IGetTessTriStripEdgeSize

This
method is obsolete and has been superseded by[Component2::IGetTessTriStripEdgeSize](sldworksAPI.chm::/Component2/Component2__IGetTessTriStripEdgeSize.htm).

Description

This method gets the number of triangles.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = Component->IGetTessTriStripEdgeSize (
long* retval )

(Table)=========================================================

| Input: | (double) x | X component of the direction vector |
| --- | --- | --- |
| Input: | (double) y | Y component of the direction vector |
| Input: | (double) z | Z component of the direction vector |
| Input: | (VARIANT_BOOL) found | TRUE if a point is found |
| Input: | (double*) startPoint | Pointer to an array of 3 doubles (x,y,z) |
| Output: | (LPASSEMBLYDOC) retval | Pointer to a newly created assembly or NULL if
the operation fails |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Tessellation information is available only when
the component is loaded as lightweight.

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
<param name="_CURRENTFILEPATH" value="D:\sw2003\Component\Component__IGetTessTriStripEdgeSize.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
