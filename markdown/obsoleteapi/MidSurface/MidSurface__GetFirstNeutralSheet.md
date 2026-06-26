---
title: "MidSurface::GetFirstNeutralSheet"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MidSurface/MidSurface__GetFirstNeutralSheet.htm"
---

# MidSurface::GetFirstNeutralSheet

This method is obsolete
and has been superseded by[MidSurface2::GetFirstNeutralSheet](sldworksAPI.chm::/MidSurface2/MidSurface2__GetFirstNeutralSheet.htm).

Description

This method return the first reference surface in this MidSurface feature.
Each reference surface in the MidSurface feature is considered a sheet
body. If the reference surfaces are sewn together during the creation
of the MidSurface feature (ModelDoc::InsertMidSurfaceExt), then the MidSurface
feature will contain only one reference surface sheet body.

Syntax (OLE Automation)

retval = MidSurface.GetFirstNeutralSheet
()

(Table)=========================================================

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the first reference surface sheet body
in this MidSurface feature |
| --- | --- | --- |

Syntax (COM)

status = MidSurface->IGetFirstNeutralSheet
( &retval )

(Table)=========================================================

| Output: | (LPBODY) retval | First reference surface sheet body in this MidSurface feature |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The sheet body returned from this method has the normal topology that
you would expect to find on a body object (for example, faces, edges,
and so on). See the Body object for the methods that provide access to
this topology.

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
<param name="Items" value="MidSurface_Object$$**$$ZGetBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\MidSurface\MidSurface__GetFirstNeutralSheet.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
