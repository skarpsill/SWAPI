---
title: "View::GetPolylineCount4"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetPolylineCount4.htm"
---

# View::GetPolylineCount4

This method is obsolete and has been superseded
by[View::GetPolyLineCount5](sldworksAPI.chm::/View/View__GetPolyLineCount5.htm).

Description

This method returns the number of polylines in the view and the array
size needed for a call View::IGetPolylines4.

Syntax (OLE Automation)

Not available. Use the upper bound on the SareArray returned from View::GetPolyLines3.

Syntax (COM)

status = View->GetPolylineCount4 ( &PointCount,
&retval )

(Table)=========================================================

| Output: | (long) PointCount | Size of array needed to allocate in doubles for View::GetPolylines4 |
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
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2000$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\View\View__GetPolylineCount4.htm" >
<param name="_ID" value="RelatedTopic0" >
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="View_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\View\View__GetPolylineCount4.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
