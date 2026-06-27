---
title: "SketchBlockDefinition::GetSplines"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchBlockDefintion/SketchBlockDefinition__GetSplines.htm"
---

# SketchBlockDefinition::GetSplines

This method is obsolete and has been superseded
by[SketchBlockDefinition::GetSplines2](sldworksAPI.chm::/SketchBlockDefinition/SketchBlockDefinition__GetSplines2.htm).

Description

This method gets information
about all of the splines in this block definition.

Syntax (OLE Automation)

Splines = SketchBlockDefinition.GetSplines ()

(Table)=========================================================

| Output: | (VARIANT) Splines | VARIANT of type SafeArray of
doubles (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = SketchBlockDefinition->IGetSplines (
ArraySize, Splines)

Parameters Table Start

(Table)=========================================================

| Input: | (long) ArraySize | Number of elements in the array
(see Remarks ) |
| --- | --- | --- |
| Output: | (double) Splines | Array of doubles (see Remarks ) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Before using the COM version
of this method, use the value returned by SketchBlockDefinition::GetSplineCount's
PointCount argument to size the array.

The returned array of doubles has the format:

[[Color,
LineType, NumSplinePoints, [x,y,z]]… ]

This complete set of data repeats itself for each spline found in the
sketch. For each spline, the array returned contains the color, the line
type, the number of spline points in the spline, and the x,y,z value for
each of those points. Therefore, the[x,y,z]parameter is an array ofNumSplinePoints,which may vary in size from spline
to spline.

The[x,y,z]points for each
spline are not the same as the points used to generate the spline. This
methodkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}tessellates
the spline based on the display quality and places points along the spline
appropriately.

LineTypemay take one of the values in swLineTypes_e.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes007$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\SketchBlockDefintion\SketchBlockDefinition__GetSplines.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="SketchBlockDefinition_Object$$**$$ZGetSketchBlockDefinitionSplines$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\SketchBlockDefintion\SketchBlockDefinition__GetSplines.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
