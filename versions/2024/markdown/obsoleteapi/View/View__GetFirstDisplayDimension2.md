---
title: "View::GetFirstDisplayDimension2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetFirstDisplayDimension2.htm"
---

# View::GetFirstDisplayDimension2

This
method is obsolete and has been superseded by[View::GetFirstDisplayDimension3](View__GetFirstDisplayDimension3.htm).

Description

This method returns the first display dimension in this drawing view.

Syntax (OLE Automation)

retval = View.GetFirstDisplayDimension2
( )

(Table)=========================================================

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the first DisplayDimension object |
| --- | --- | --- |

Syntax (COM)

status = View->IGetFirstDisplayDimension2
( &retval )

(Table)=========================================================

| Output: | (LPDISPLAYDIMENSION) retval | Pointer to the first DisplayDimension object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

A SolidWorks dimension can be displayed more than once. For example,
the Base-Extrude dimension could be brought into three different views
on a drawing. These three dimensions are referred to as display dimensions
and are represented by the DisplayDimension object in the SolidWorks API.
The original Base-Extrude dimension is represented by the Dimension object
in the SolidWorks API.

This function is identical to the now obsolete View::GetFirstDisplayDimension
except when a base ordinate is not visible, the subordinates were not
previously output, whether they were visible or not. Withthis methodthe output of each subodinate, if it is visible, occurs whether or not
its base ordinate is visible.

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
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\View\View__GetFirstDisplayDimension2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
