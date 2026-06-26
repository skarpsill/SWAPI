---
title: "View::GetDisplayData"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetDisplayData.htm"
---

# View::GetDisplayData

This
method is obsolete and has been superseded by[View::GetDisplayData2](View__GetDisplayData2.htm).

Description

This method gets the DisplayData object for this drawing view.

NOTE: The DisplayData object
provides information for additional display data, such as reference plane
display, reference axis display, unused sketch geometry from a part, and
so on. The data kept with the DisplayData object is strictly for display
purposes and allows you to recreate unintelligentkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}geometry.
It does not provide associations or detailed information about the geometry.

Syntax (OLE Automation)

retval = View.GetDisplayData ()

(Table)=========================================================

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the DisplayData object for this drawing
view. |
| --- | --- | --- |

Syntax (COM)

status = View->IGetDisplayData (
&retval )

(Table)=========================================================

| Output: | (LPDISPLAYDATA) retval | Pointer to the DisplayData object for this drawing view. |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

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
<param name="Items" value="View_Object$$**$$ZGetDisplayData$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\sw2003\View\View__GetDisplayData.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
