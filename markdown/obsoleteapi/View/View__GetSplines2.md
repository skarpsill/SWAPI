---
title: "View::GetSplines2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetSplines2.htm"
---

# View::GetSplines2

This
method is obsolete and has been superseded by[View::GetSplines3](sldworksAPI.chm::/View/View__GetSplines3.htm).

Description

This method returns information for each spline that was sketched in
this drawing view.

NOTE: This method only returns splines that have been deliberately sketched
in this drawing view. All part and assembly geometry shown in a drawing
view is represented by polylines. To access the Polylines, use View::GetPolylines3.

Syntax (OLE Automation)

retval = View.GetSplines2 ( )

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = View->IGetSplines2 ( &retval
)

(Table)=========================================================

| Output: | (double) retval | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Format of return values is an array of doubles with the format:

[
[Color, LineType, LineStyleIndex,
LineWeight, NumSplinePoints, [x,y,z] ] …]

where:

Color=kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}COLORREF
returned as an integer. Return value could be 0 or -1 for default color.

LineType=
line type. Valid returns as defined in swLineTypes_e. AlineTypeis a combination of a lineStyle and lineWeight.

LineStyleIndex=
index location of this line style inside SolidWorks Line Style Manager

LineWeight=
integer value defining the line weight

This complete set of data repeats itself for each spline found in the
view. For each spline, the array returned contains the color, line type,
number of spline points in the spline, and X,Y,Z value for each of those
points. Therefore, the[x,y,z]parameter is an array ofNumSplinePointsthat canvary in size
from spline to spline.

The[x,y,z]points for each
spline are not the same as the points used to generate the spline. This
method tessellates the spline based on the display quality and place points
along the spline appropriately.

The data returned from this method is in terms of vew space. If you
want the data in terms of sheet space (that is, the 0,0 origin being the
lower-left corner of the sheet), then combine this data with the three
return values from View::GetXForm.

To determine the number of splines in
the view, refer to View::GetSplineCount or get the number of elements
in the SafeArray returned by the call to GetSplines.

If you are using COM, then your call to IGetSplines must be preceded
by a call to GetSplineCount.

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
<param name="Items" value="View_Object$$**$$ZGetInfoView$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\View\View__GetSplines2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
