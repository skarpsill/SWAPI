---
title: "Sketch::GetUserPoints"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sketch/Sketch__GetUserPoints.htm"
---

# Sketch::GetUserPoints

This method is obsolete and has been superseded
by[Sketch::GetUserPoints2](sldworksAPI.chm::/Sketch/Sketch__GetUserPoints2.htm).

Description

This method returns all of the user points in this sketch.

Syntax (OLE Automation)

retval = Sketch.GetUserPoints ()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = Sketch->IGetUserPoints
( retval )

(Table)=========================================================

| Output: | (double*) retval | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

See Sketch::GetSketchPoints or Sketch::IEnumSketchPoints
for access to individual SketchPoint objects.

The return value is an array of 3 doubles with
the format:

- 0,1,2
  XYZ of first point
- 3,4,5
  XYZ of next point
- ...

size = Number of Points * 3

To determine the number of points in the sketch,
see Sketch::GetUserPointsCount.

The data returned from this method is in terms
of sketch space. If you want the data in terms of model space, then you
should combine this data with the transform property Sketch::ModelToSketchXform.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Sketch_Object$$**$$ZGetInfoSketch$$**$$ZGetSketchPoint$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\Sketch\Sketch__GetUserPoints.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
