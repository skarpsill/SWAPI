---
title: "Sketch::GetEllipses2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sketch/Sketch__GetEllipses2.htm"
---

# Sketch::GetEllipses2

This method is obsolete and has been superseded
by[Sketch::GetEllipses3](sldworksAPI.chm::/Sketch/Sketch__GetEllipses3.htm).

Description

This method gets all of the
ellipses in the sketch.

Syntax (OLE Automation)

retval = Sketch.GetEllipses2 ( )

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = Sketch->IGetEllipses2 (
&retval )

(Table)=========================================================

| Output: | (double) retval | Pointer to an array of doubles (see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if Successful |

Remarks

See Sketch::GetSketchSegments or Sketch::IEnumSketchSegments
for access to individual SketchSegment and SketchEllipse objects.

The return values are in an array of doubles:

[Unused, LineType, Unused, Unused, StartPt[3],
EndPt[3], CenterPt[3], MajorPt[3], MinorPt[3],Direction ...]

where:

(Table)=========================================================

| Unused : | This return value is unused,and is returned as 0. |
| --- | --- |
| LineType : | Line type. Valid returns are defined in swLineTypes_e. A lineType is
a combination of a lineStyle and lineWeight. |
| Unused : | This return value is unused and is returned as 0. |
| Unused : | This return value is unused and is returned as 0. |
| StartPt[3] : | An array of 3 doubles (X,Y,Z) describing the ellipse start point |
| EndPt[3] : | An array of 3 doubles (X,Y,Z) describing the ellipse end point. If the
ellipse is closed, then this will be the same point as the StartPt. |
| CenterPt[3] : | An array of 3 doubles (X,Y,Z) describing the ellipse center point. |
| MajorPt[3] : | An array of 3 doubles (X,Y,Z) describing a point on the ellipse and
on the major axis. |
| MinorPt[3] : | An array of 3 doubles (X,Y,Z) describing a point on the ellipse and
on the minor axis. |
| Direction : | -1 for clockwise, +1 for counter-clockwise. |

This set of data repeats for each ellipse in the sketch. The size of
the array is (NumEllipses * 20). To determine the number of ellipses,
see Sketch::GetEllipseCount.

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
<param name="Items" value="Sketch_Object$$**$$ZGetInfoSketch$$**$$ZGetSketchSegment$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\Sketch\Sketch__GetEllipses2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
