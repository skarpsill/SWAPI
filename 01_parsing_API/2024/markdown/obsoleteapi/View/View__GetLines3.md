---
title: "View::GetLines3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetLines3.htm"
---

# View::GetLines3

This method is obsolete and has been superseded
by[View::GetLines4](sldworksAPI.chm::/View/View__GetLines4.htm).

Description

This method returns information for each line that was sketched in this
drawing view.

NOTE: This method only returns
lines that have been deliberately sketched in this drawing view. All part
and assembly geometry shown in a drawing view is represented by Polylines.
To access the polylines, use View::GetPolylines3.

Syntax (OLE Automation)

retval = View.GetLines3 ( )

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = View->IGetLines3 ( retval
)

(Table)=========================================================

| Output: | (double*) retval | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value is the following array of doubles:

[Color,
LineType, LineStyleIndex, LineWidth, LayerID, LayerOverride,StartPt[3], EndPt[3], ...]

where all data values are returned as doubles:

Color=
COLORREF returned as an integer. Return value could be 0 or -1 for default
color.

LineType=
line type. Valid returns as defined in swLineTypes_e. AlineTypeis a combination of a lineStyle and lineWeight.

LineStyleIndex= line style. Valid line styles as defined in swLineStyles_e.

LineWidth=
integer value defining the line width. Valid width values as defined in
swLineWeights_e .

LayerID=
integer value indicating which layer holds this entity. Obtain the Layer
object by passing this integer value to LayerMgr::GetLayerById.

LayerOverride=
integer with bit flags set to determine which properties, if any, have
been overridden with respect to the Layer default properties. If the bit
value is set, then the specific property or properties have been overridden.
The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore,
ifLayerOverrideis returned
as 3, you know the color and style have been specifically set for this
item and may not match the default values associated with this item's
layer.

StartPt[3]=
array of 3 doubles (X,Y,Z) describing the line start point

EndPt[3]=
array of 3 doubles (X,Y,Z) describing the line end point.

This set of data repeats for each line
in the view. The number of doubles returned are (lineCount* 12). To determine the number of lines in the view, use View::GetLineCount.

The data returned from this method is in terms of view space. If you
want the data in terms of sheet space (that is, the 0,0 origin being the
lower-left corner of the sheet), then combine this data with the three
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
<param name="Items" value="View_Object$$**$$ZGetInfoView$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\sw2003\View\View__GetLines3.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
