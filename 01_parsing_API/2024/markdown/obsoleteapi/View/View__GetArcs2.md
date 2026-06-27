---
title: "View::GetArcs2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetArcs2.htm"
---

# View::GetArcs2

This
method is obsolete and has been superseded by View::GetArcs3 .

Description

This method returns information for each arc that was sketched in this
drawing view.

Syntax (OLE Automation)

retval = View.GetArcs2 ()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray containing an array of doubles |
| --- | --- | --- |

Syntax (COM)

status = View->IGetArcs2 ( retval
)

(Table)=========================================================

| Output: | (double*) retval | Pointer to an array of doubles as |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method returns arcs that have been deliberately sketched in this
drawing view. All part and assembly geometry shown in a drawing view is
represented by polylines. To access the polylines, use View::GetPolylines3.

Return value is an array of doubles with the format:

[LineType, StartPt[3], EndPt[3], CenterPt[3],
RotDir, ...]

where:

LineTypethe
line type. Valid returns are found in the swLineTypes_e enumeration. A
lineType is a combination of a lineStyle and lineWeight.

StartPt[3]an
array of 3 doubles (X,Y,Z) describing the start point.

EndPt[3]an
array of 3 doubles (X,Y,Z) describing the end point. If the arc is closed,
then this is the same point as the StartPt.

CenterPt[3]an
array of 3 doubles (X,Y,Z) describing the center point.

RotDirthe
rotational direction (CW = -1, CCW = 1)

...

This set of data repeats for each arc in the view. The size of the array
is (NumArcs * 11). To determine the number of arcs, use View::GetArcCount.

The data returned from this method is in terms of view space. If you
want the data in terms of sheet space (for example, the 0,0 origin being
the lower-left corner of the sheet), then you combine this data with the
three return values from View::GetXForm.

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
<param name="Items" value="View_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\View\View__GetArcs2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
