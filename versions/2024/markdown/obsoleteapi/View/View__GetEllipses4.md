---
title: "View::GetEllipses4"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetEllipses4.htm"
---

# View::GetEllipses4

This
method is obsolete and has been superseded by[View::GetEllipses5](sldworksAPI.chm::/View/View__GetEllipses5.htm).

Description

This method gets all the ellipses
that were sketched in this drawing view.

Syntax (OLE Automation)

retval = View.GetEllipses4 ( )

(Table)=========================================================

| Return: | (VARIANT)retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = View->IGetEllipses4 ( &retval
)

(Table)=========================================================

| Output: | (double)retval | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method only returns ellipses
that have been deliberately sketched in this drawing view. All part and
assembly geometry shown in a drawing view is represented by polylines.
To access the polylines, use View::GetPolylines3.

The return values are in an array of doubles:

[Color, LineType, LineStyleIndex, LineWeight,
StartPt[3], EndPt[3], CenterPt[3], MajorPt[3], MinorPt[3],Direction ...]

where:

Color:COLORREF returned as an integer. Return value could be 0 or -1 for default
color.

LineType:line type. Valid returns as defined in swLineTypes_e. AlineTypeis a combination of a lineStyle and lineWeight.

LineStyleIndex:index location of this line style inside SolidWorks line style manager.

LineWeight:integer value defining the line weight.

StartPt[3]:array of 3 doubles (X,Y,Z) describing the ellipse start point

EndPt[3]:
array of 3 doubles (X,Y,Z) describing the ellipse end point. If the ellipse
is closed, then this will be the same point as theStartPt..

CenterPt[3]:array of 3 doubles (X,Y,Z) describing the ellipse center point.

MajorPt[3]:array of 3 doubles (X,Y,Z) describing a point on the ellipse and
on the major axis.

MinorPt[3]:array of 3 doubles (X,Y,Z) describing a point on the ellipse and on the
minor axis.

Direction:-1 for Clockwise, +1 for counterclockwise.

This set of data repeats for each ellipse in the view. The size of the
array is (NumEllipses * 20). To determine the number of ellipses, use
View::GetEllipseCount.

The data returned from this method is in terms of view space. If you
want the data in terms of sheet space (for example, the 0,0 origin being
the lower-eft corner of the sheet), then combine this data with the three
return values from View::GetXForm.

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
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="C:\Home\sw2003\View\View__GetEllipses4.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
