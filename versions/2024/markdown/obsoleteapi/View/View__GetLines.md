---
title: "View::GetLines"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetLines.htm"
---

# View::GetLines

This
method is obsolete and has been superseded by[View::GetLines2](View__GetLines2.htm).

Description

This method returns information for each line that was sketched in this
drawing view.

NOTE: This method only return
lines that have been deliberately sketched in this drawing view. All part
and assembly geometry shown in a drawing view is represented by polylines.
To access the polylines, use View::GetPolylines3 method.

Syntax (OLE Automation)

retval = View.GetLines ()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = View->IGetLines ( &retval
)

(Table)=========================================================

| Output: | (double) retval | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The return value is the following array of doubles:

[LineType, StartPtX, StartPtY, StartPtZ, EndPtX,
EndPtY, EndPtZ,... ]

where this array of 7 values repeats
itself for each line in the view. The number of doubles returned is (lineCount* 7). To determine the number
of lines in the view, refer to View::GetLineCount.

See swLineTypes_e for valid line types.

The data returned from this method is in terms of view space. If you
want the data in terms of sheet space (for example, the 0,0 origin being
the lower-left corner of the sheet), then combine this data with the three
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
<param name="Items" value="View_Object$$**$$GetLines$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\sw2003\View\View__GetLines.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
