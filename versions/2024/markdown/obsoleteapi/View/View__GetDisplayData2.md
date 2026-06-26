---
title: "View::GetDisplayData2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDisplayData2.htm"
---

# View::GetDisplayData2

This
method is obsolete and has been superseded by[View::GetDisplayData3](sldworksAPI.chm::/View/View__GetDisplayData3.htm).

Description

This method gets the DisplayData object for this drawing view.

NOTE: The DisplayData object
provides information for additional display data, such as reference plane
display, reference axis display, unused sketch geometry from a part, and
so on. The data kept with the DisplayData object is strictly for display
purposes and allows you to recreate unintelligent geometry. It does not
provide associations or detailed information about the geometry.

Syntax (OLE Automation)

retval = View.GetDisplayData2 ()

(Table)=========================================================

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the DisplayData object for this drawing
view |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDisplayData2
( &retval )

(Table)=========================================================

| Output: | (LPDISPLAYDATA) retval | Pointer to the DisplayData object for this drawing view |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method supersedes the now obsolete View::GetDisplayData
and should be used in its place. The previous version of this method returned
sketch entities based on their hide or show setting from the model document.
This method returns the sketch entities based on the hide or show setting
from this drawing view. This behavior is more appropriate because it gives
you the display as seen in the drawing view.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
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
<param name="Items" value="View_Object$$**$$ZGetDisplayData$$**$$DisplayData_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\View\View__GetDisplayData2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
