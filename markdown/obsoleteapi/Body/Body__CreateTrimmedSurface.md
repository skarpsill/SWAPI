---
title: "Body::CreateTrimmedSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__CreateTrimmedSurface.htm"
---

# Body::CreateTrimmedSurface

This
method is obsolete and has been superseded by[Body2::CreateTrimmedSurface](sldworksAPI.chm::/Body2/Body2__CreateTrimmedSurface.htm).

Description

This method creates a trimmed surface from a base surface and a list
of existing trimming curves assumed to have been already created.

Syntax (OLE Automation)

retval
= Body.CreateTrimmedSurface ()

(Table)=========================================================

| Return: | (BOOL)
retval | TRUE
if the trimmed surface was created, FALSE if it was not |
| --- | --- | --- |

Syntax (COM)

status
= Body->CreateTrimmedSurface ( &retval )

(Table)=========================================================

| Output: | (VARIANT_BOOL)
retval | TRUE if the trimmed surface was created, FALSE if it was not |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

This method is the final call in a set of related
functions that are designed to construct a trimmed surface from a base
surface (possibly infinite) and a set of trimming curves. Before you use
this method, you must call one of the base surface creation methods (such
as Body::CreatePlanarSurface) and the trimming-curve creation method Surface::AddTrimmingLoop.

If you want to construct a solid body from trimmed
surfaces, then you must first call PartDoc::CreateNewBody, which arranges
for a place-holder for this trimmed surface.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Body\Body__CreateTrimmedSurface.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
