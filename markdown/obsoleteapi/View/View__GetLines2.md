---
title: "View::GetLines2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetLines2.htm"
---

# View::GetLines2

This
method is obsolete and has been superseded by[View::GetLines3](View__GetLines3.htm).

Description

This method returns information for each line that was sketched in this
drawing view.

NOTE: This method only returns
lines that have been deliberately sketched in this drawing view. All part
and assembly geometry shown in a drawing view is represented by polylines.
To access the polylines, use View::GetPolylines3.

Syntax (OLE Automation)

retval = View.GetLines2 ( )

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = View->IGetLines2 ( &retval
)

(Table)=========================================================

| Output: | (double)retval | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The return value is the following array of doubles:

[color, lineType, lineStyleIndex,
lineWeight, StartPtX, StartPtY, StartPtZ, EndPtX, EndPtY, EndPtZ, ...]

where all data values are returned as doubles:

color=
COLORREF returned as an integer. Return value could be 0 or -1 for default
color.

LineType= line type. Valid returns as defined in swLineTypes_e. AlineTypeis a combination of a lineStyle and lineWeight.

LineStyleIndex=
index location of this line style inside SolidWorks Line Style Manager.

lineWeight=
integer value defining the line weight.

where this array of 10 values repeats
itself for each line in the view. The number of doubles returned will
be (lineCount* 10). To determine
the number of lines in the view, usekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}View::GetLineCount.

The data returned from this method is in terms of view space. If you
want the data in terms of sheet space (that is, the 0,0 origin being the
lower-left corner of the sheet), then combine this data with the three
return values from View::GetXForm.

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
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\View\View__GetLines2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
