---
title: "Body::SetCurrentSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__SetCurrentSurface.htm"
---

# Body::SetCurrentSurface

This
method is obsolete and has been superseded by[Body2::SetCurrentSurface](sldworksAPI.chm::/Body2/Body2__SetCurrentSurface.htm).

Description

This method places an existing surface object
into a temporary body object that is under construction.

Syntax (OLE Automation)

void Body.SetCurrentSurface (surfaceIn)

(Table)=========================================================

| Input: | (LPDISPATCH) surfaceIn | Pointer to a Dispatch object, a surface; this
surface might have been created using other surface creation routines,
such as Modeler::CreateCylindricalSurface |
| --- | --- | --- |

Syntax (COM)

status = Body->ISetCurrentSurface ( surfaceIn
)

(Table)=========================================================

| Input: | (LPSURFACE) surfaceIn | Pointer to a surface object; this surface might
have been created using other surface creation routines, such as Modeler::CreateCylindricalSurface |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is used with a set of related methods
that construct a body from trimmed surfaces. This method takes a surface
object created elsewhere and adds it to the temporary body object, which
is acting as a placeholder for the trimmed surfaces.

Follow calls to this method with one or more
calls to the trimming-curve creation methods, such as Surface::AddTrimmingLoop2.
Than, trim the surface using Body::CreateTrimmedSurface. After you add
all the surfaces to the body and trim appropriately, you can sew the body
to create an imported SolidWorks body feature using Body::CreateBodyFromSurfaces.

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
<param name="Items" value="Body_Object$$**$$ZCreateSurface$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Body\Body__SetCurrentSurface.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
