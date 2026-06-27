---
title: "Sketch::GetParabolas"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sketch/Sketch__GetParabolas.htm"
---

# Sketch::GetParabolas

This method is obsolete and has been superseded
by[Sketch::GetParabolas2](sldworksAPI.chm::/Sketch/Sketch__GetParabolas2.htm).

Description

This method gets all of the
parabolas in the sketch.

Syntax (OLE Automation)

retval = Sketch.GetParabolas ( )

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray (See Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = Sketch->IGetParabolas (
&retval )

(Table)=========================================================

| Output: | (double) retval | Pointer to an array of doubles (See Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

See Sketch::GetSketchSegments or Sketch::IEnumSketchSegments
for access to individual SketchSegment and SketchParabola objects.

The return values are in an array of doubles:

[Unused, LineType, Unused, Unused, StartPt[3],
EndPt[3], FocusPt[3], ApexPt[3] ...]

where:

(Table)=========================================================

| Unused : | This return value is unused and is returned as 0. |
| --- | --- |
| LineType : | Line type. Valid returns are defined in swLineTypes_e. A lineType is
a combination of a lineStyle and lineWeight. |
| Unused : | This return value is unused and is returned as 0. |
| Unused : | This return value is unused and is returned as 0. |
| StartPt[3] : | Array of 3 doubles (X,Y,Z) describing the parabola start point |
| EndPt[3] : | Array of 3 doubles (X,Y,Z) describing the parabola end point. |
| FocusPt[3] : | Array of 3 doubles (X,Y,Z) describing the parabola focus point. |
| ApexPt[3] : | Array of 3 doubles (X,Y,Z) describing the parabola apex point. |

This set of data repeats for each parabola in the sketch. The size of
the array is (NumParabolas * 16). To determine the number of parabolas,
see Sketch::GetParabolaCount.

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
<param name="Items" value="Sketch_Object$$**$$ZGetParabola$$**$$ZGetSketchSegment$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\Sketch\Sketch__GetParabolas.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
