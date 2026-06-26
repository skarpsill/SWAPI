---
title: "Sketch::GetArcs"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sketch/Sketch__GetArcs.htm"
---

# Sketch::GetArcs

This method is obsolete and has been superseded
by[Sketch::GetArcs2](sldworksAPI.chm::/Sketch/Sketch__GetArcs2.htm).

Description

This method returns all of the arcs in this sketch.

Syntax (OLE Automation)

retval = Sketch.GetArcs ()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray of arc information |
| --- | --- | --- |

Syntax (COM)

status = Sketch->IGetArcs ( retval
)

(Table)=========================================================

| Output: | (double*) retval | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

See Sketch::GetSketchSegments or Sketch::IEnumSketchSegments
for access to individual SketchSegment and SketchArc objects.

Return value is an array of doubles with the format:

[LineType,StartPt[3],EndPt[3],CenterPt[3],RotDir,...
]

where:

(Table)=========================================================

| LineType | Line type as defined in swLineTypes_e. A lineType is a combination of
a lineStyle and lineWeight. |
| --- | --- |
| StartPt[3] | Array of 3 doubles (X,Y,Z) describing the arc start point. |
| EndPt[3] | Array of 3 doubles (X,Y,Z) describing the arc end point. If the arc
is closed, then this will be the same point as the StartPt. |
| CenterPt[3] | Array of 3 doubles (X,Y,Z) describing the center point. |
| RotDir | Rotational direction (CW = -1, CCW = 1). |

This set of data repeats for each arc in the sketch. The size of the
array is (NumArcs * 11). To determine the number of arcs, see Sketch::GetArcCount.

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\Sketch\Sketch__GetArcs.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
