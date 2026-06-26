---
title: "View::GetPolylines"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetPolylines.htm"
---

# View::GetPolylines

This
method is obsolete and has been superseded by[View::GetPolylines2](View__GetPolylines2.htm).

Description

This method returns information about the polylines in this view.

NOTE: All geometry from a part
or assembly shown in a drawing view is represented by polylines. If you
need this geometry to be output to your system as lines, arcs, and so
on, then you must create routines that recognize the polyline information
as a straight line, arc, and so on, and then generate the appropriate
geometry.

Syntax (OLE Automation)

retval = View.GetPolylines ()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray of polylines |
| --- | --- | --- |

Syntax (COM)

status = View->IGetPolylines ( &retval
)

(Table)=========================================================

| Output: | (double) retval | Pointer to array of doubles |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

To get items sketched in this drawing view, use one of View::GetArcs4,
View::GetLines3, View::GetSplines3, or View::GetEllipses5.

Format of return values is an array ofdoubleswith the format:

[Color, LineTypeIndex, NumPolyPoints,
[x,y,z]]

where the[x,y,z]parameter
is an array ofNumPolyPoints.

NOTE: The polyline data is stored
with the accuracy of a float. The return array contains doubles, but these
are float values converted to doubles.

To determine the number of polylines
in the view, refer to View::GetPolyLineCount.

(Table)=========================================================

| If... | Then... |
| --- | --- |
| Changes are made to the parts or assemblies shown in this drawing | Polylines are only generated that are in the visible viewing bounds
when the drawing is opened. |
| Drawing is already open | All polylines in the drawing
are generated. If you open a drawing that is zoomed in to a particular
region, then the polylines that are outside the zoomed region do not exist
if the parts or assemblies shown in this drawing have been changed. To
force the generation of all possible polyline data, call ModelDoc2::ViewZoomtofit. |

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\sw2003\View\View__GetPolylines.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
