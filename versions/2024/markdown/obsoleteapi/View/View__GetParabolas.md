---
title: "View::GetParabolas"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetParabolas.htm"
---

# View::GetParabolas

This
method is obsolete and has been superseded by[View::GetParabolas2](sldworksAPI.chm::/View/View__GetParabolas2.htm).

Description

This method gets all of the
parabolas in the view.

Syntax (OLE Automation)

retval = View.GetParabolas ( )

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = View->IGetParabolas ( &retval
)

(Table)=========================================================

| Output: | (double) retval | pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return values are in an array of doubles:

[Color, LineType, LineStyleIndex, LineWeight,
StartPt[3], EndPt[3], FocusPt[3], ApexPt[3] ...]

where:

Color = COLORREF returned as an integer.
Return value could be 0 or -1 for default color.

LineType = line type. Valid returns
as defined in swLineTypes_e. AlineTypeis a combination of a lineStyle and lineWeight.

LineStyleIndex = index location of this
line style inside SolidWorks Line Style Manager.

LineWeight = integer value defining
the line weight.

StartPt[3] = array of 3 doubles (X,Y,Z)
describing the parabola start point.

EndPt[3] = array of 3 doubles (X,Y,Z)
describing the parabola end point.

FocusPt[3] = array of 3 doubles (X,Y,Z)
describing the parabola focus Point.

ApexPt[3] = array of 3 doubles (X,Y,Z)
describing the parabola apex Point.

This set of data repeats for each parabola in the view. The size of
the array is (NumParabolas * 16). To determine the number of parabolas,
use View::GetParabolaCount.

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
<param name="Items" value="View_Object$$**$$ZGetParabola$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\View\View__GetParabolas.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
