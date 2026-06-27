---
title: "MidSurface::GetNeutralSheetCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/MidSurface/MidSurface__GetNeutralSheetCount.htm"
---

# MidSurface::GetNeutralSheetCount

This method is obsolete
and has been superseded by[MidSurface2::GetNeutralSheetCount](sldworksAPI.chm::/MidSurface2/MidSurface2__GetNeutralSheetCount.htm).

Description

This method determines the total number of reference surfaces found
in this MidSurface feature. Each reference surface in the MidSurve feature
is considered a sheet body. If the reference surfaces are sewn together
during the creation of the MidSurface feature (ModelDoc::InsertMidSurfaceExt),
then the MidSurface feature will contain only one reference surface sheet
body.

Syntax (OLE Automation)

retval = MidSurface.GetNeutralSheetCount
()

(Table)=========================================================

| Return: | (long) retval | Number of reference surface sheet bodies found in this MidSurface feature |
| --- | --- | --- |

Syntax (COM)

status = MidSurface->GetNeutralSheetCount
( &retval )

(Table)=========================================================

| Output: | (long) retval | Number of reference surface sheet bodies found in this MidSurface feature |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
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
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\MidSurface\MidSurface__GetNeutralSheetCount.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
