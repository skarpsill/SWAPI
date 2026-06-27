---
title: "Sketch::GetLines"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sketch/Sketch__GetLines.htm"
---

# Sketch::GetLines

This method is obsolete and has been superseded
by[Sketch::GetLines2](sldworksAPI.chm::/Sketch/Sketch__GetLines2.htm).

Description

This method returns information about each line in this sketch.

Syntax (OLE Automation)

retval = Sketch.GetLines ()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = Sketch->IGetLines ( retval
)

(Table)=========================================================

| Output: | (double*) retval | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The return value is the following array of doubles:

[LineType, StartPtX, StartPtY, StartPtZ, EndPtX,
EndPtY, EndPtZ,... ]

where this array of 7 values repeats
itself for each line in the sketch. The number of doubles returned is
(lineCount* 7). To determine
the number of lines in the sketch, see Sketch::GetLineCount.

LineStyle may take one of the values in swLineTypes_e.

See Sketch::GetSketchSegments or Sketch::IEnumSketchSegments for access
to individual SketchSegment and SketchLine objects.

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
<param name="Items" value="Sketch_Object$$**$$ZGetInfoSketch$$**$$GetLines$$**$$ZGetSketchSegment$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Sketch\Sketch__GetLines.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
