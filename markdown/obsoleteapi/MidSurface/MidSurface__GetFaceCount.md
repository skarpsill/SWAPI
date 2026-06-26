---
title: "MidSurface::GetFaceCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MidSurface/MidSurface__GetFaceCount.htm"
---

# MidSurface::GetFaceCount

This method is obsolete
and has been superseded by[MidSurface2::GetFaceCount](sldworksAPI.chm::/MidSurface2/MidSurface2__GetFaceCount.htm).

Description

This method gets the total number of faces in the MidSurface feature.
If more than one reference surface exists in the MidSurface feature, then
those faces are included in the total count returned.

Syntax (OLE Automation)

retval = MidSurface.GetFaceCount ()

(Table)=========================================================

| Return: | (long) retval | Face count |
| --- | --- | --- |

Syntax (COM)

status = MidSurface->GetFaceCount
( &retval )

(Table)=========================================================

| Output: | (long) retval | Face count |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="MidSurface_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\MidSurface\MidSurface__GetFaceCount.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
