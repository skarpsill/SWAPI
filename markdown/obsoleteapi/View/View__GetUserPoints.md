---
title: "View::GetUserPoints"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetUserPoints.htm"
---

# View::GetUserPoints

This
method is obsolete and has been superseded by[View::GetUserPoints2](sldworksAPI.chm::/View/View__GetUserPoints2.htm).

Description

This method returns all of the user points in this drawing view.

Syntax (OLE Automation)

retval = View.GetUserPoints ()

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = View->IGetUserPoints (
&retval )

(Table)=========================================================

| Output: | (double) retval | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value is the following array of doubles:

[[X,
Y, Z], ..]

size = Number of Points * 3

This set of data repeats itself for each user point in the view. The
size of the array is (NumPts * 3). To determine the number of points in
the view, see View::GetUserPointsCount.

The data returned from this method is in terms of view space. If you
want the data in terms of sheet space (that is, - the 0,0 origin being
the lower-left corner of the sheet), then combine this data with the three
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
<param name="Items" value="View_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\sw2003\View\View__GetUserPoints.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
