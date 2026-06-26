---
title: "View::GetPolyLineCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetPolyLineCount.htm"
---

# View::GetPolyLineCount

This
method is obsolete and has been superseded by[View::GetPolyLineCount2](View__GetPolyLineCount2.htm).

Description

This method gets the number of polylines in the view along with the
array size needed for View::IGetPolyLines .

Syntax (OLE Automation)

Not available. Use the upper bound on the SafeArray returned from View::GetPolyLines.

Syntax (COM)

status = View->GetPolyLineCount
( &PointCount, &retval )

(Table)=========================================================

| Output: | (long) PointCount | Size of array needed to allocate in doubles for View::IGetPolylines |
| --- | --- | --- |
| Output: | (long) retval | Number of polylines found in the view |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="_ExtentX" value="1323" >
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
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\View\View__GetPolyLineCount.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
