---
title: "Body::ICreatePlanarTrimSurfaceDLL"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__ICreatePlanarTrimSurfaceDLL.htm"
---

# Body::ICreatePlanarTrimSurfaceDLL

## Body:: ICreatePlanarTrimSurfaceDLL

This
method is obsolete and has been superseded by[Body2::ICreatePlanarTrimSurfaceDLL](sldworksAPI.chm::/Body2/Body2__ICreatePlanarTrimSurfaceDLL.htm).

Description

This method creates a planar trim surface for this body.

Syntax (OLE Automation)

Not available.

Syntax
(COM)

status = Body::ICreatePlanarTrimSurfaceDLL(VertexCount,
Points, Normal )

(Table)=========================================================

| Input: | (long) VertexCount | Number of vertices |
| --- | --- | --- |
| Input: | (double*) Points | Pointer to an array of doubles describing the points for the surface;
SolidWorks automatically creates trim curves between each sequential vertex |
| Input: | (double*) Normal | Normal vector for the surface |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can use this method instead of using[Body::CreatePlanarSurface](Body__CreatePlanarSurface.htm),[Body::CreateTrimmedSurface](Body__CreateTrimmedSurface.htm),
and[Surface::AddTrimmingLoop](../Surface/Surface__AddTrimmingLoop.htm).

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
<param name="Items" value="Body_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\sw2003\Body\Body__ICreatePlanarTrimSurfaceDLL.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
