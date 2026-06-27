---
title: "Body::CreateNewSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__CreateNewSurface.htm"
---

# Body::CreateNewSurface

This
method is obsolete and has been superseded by[Body2::CreateNewSurface](sldworksAPI.chm::/Body2/Body2__CreateNewSurface.htm).

Description

This method creates a handle for a new surface to be used as geometry
for a face to be added to the body.

Syntax (OLE Automation)

retval
= Body.CreateNewSurface ()

(Table)=========================================================

| Return: | (LPDISPATCH)
retval | Pointer
to dispatch object, a new surface |
| --- | --- | --- |

Syntax (COM)

status
= Body->ICreateNewSurface ( &retval )

(Table)=========================================================

| Output: | (LPSURFACE)
retval | Pointer
to the new surface |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

This method is the first in a set of related functions
that construct a body from trimmed surfaces.

Internally, this method also creates a list that
serves as a place-holder for trimming curves when trimming the surface.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Body\Body__CreateNewSurface.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
