---
title: "SketchEllipse::GetCenterPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchEllipse/SketchEllipse__GetCenterPoint.htm"
---

# SketchEllipse::GetCenterPoint

T his method
is obsolete and has been superseded by[SketchEllipse::GetCenterPoint2](sldworksAPI.chm::/SketchEllipse/SketchEllipse__GetCenterPoint2.htm).

Description

This method gets the center point of this sketch
ellipse.

Syntax (OLE Automation)

retval = SketchEllipse.GetCenterPoint ( )

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type docking state of the toolbar
as defined in swToolbarDockStatePosition_e
of 3 doubles (x,y,z), the ellipse center point |
| --- | --- | --- |

Syntax (COM)status = SketchEllipse->IGetCenterPoint
( retval )

status = SketchEllipse->IGetCenterPoint2 ( &retval
)

(Table)=========================================================

| Output: | (double*) retval | Pointer to an array of 3 doubles (x,y,z), the
ellipse center point |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

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
<param name="Items" value="SketchEllipse_Object$$**$$ZGetInfoSketchEllipse$$**$$ZGetSketchEllipse$$**$$ZGetSketchSegment$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\SketchEllipse\SketchEllipse__GetCenterPoint.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
