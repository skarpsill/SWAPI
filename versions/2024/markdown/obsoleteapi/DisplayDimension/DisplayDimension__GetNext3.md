---
title: "DisplayDimension::GetNext3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/DisplayDimension__GetNext3.htm"
---

# DisplayDimension::GetNext3

This method is obsolete and has been superseded
by[DisplayDimension::GetNext4](DisplayDimension__GetNext4.htm).

Description

This method gets the next display dimension.

Syntax (OLE Automation)

retval = DisplayDimension.GetNext3
( )

(Table)=========================================================

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the next DisplayDimension |
| --- | --- | --- |

Syntax (COM)

status = DisplayDimension->IGetNext3
( &retval )

(Table)=========================================================

| Output: | (LPDISPLAYDIMENSION) retval | Pointer to the next DisplayDimension object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

SolidWorks can display a dimension more than once. For example, a base-extrude
dimension can be brought into three different views on a drawing. These
three dimensions are referred to as "Display Dimensions" and
are represented by the DisplayDimension object in the SolidWorks API.
The original base-extrude dimension is represented by the Dimension object
in the SolidWorks API.

This method is identical to DisplayDimension::GetNext2, except that
it returns dangling dimensions.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="DisplayDimension_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\DisplayDimension\DisplayDimension__GetNext3.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
