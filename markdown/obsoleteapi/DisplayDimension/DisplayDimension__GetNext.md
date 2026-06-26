---
title: "DisplayDimension::GetNext"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/DisplayDimension__GetNext.htm"
---

# DisplayDimension::GetNext

This
method is obsolete and has been superseded by[DisplayDimension::GetNext2](DisplayDimension__GetNext2.htm).

Description

This method gets the next display dimension.

Syntax (OLE Automation)

retval
= DisplayDimension.GetNext ( )

(Table)=========================================================

| Return: | (LPDISPATCH)
retval | pointer
to a Dispatch object, the next DisplayDimension |
| --- | --- | --- |

Syntax (COM)

status
= DisplayDimension->IGetNext ( &retval )

(Table)=========================================================

| Output: | (LPDISPLAYDIMENSION
retval | Pointer
to a the next DisplayDimension |
| --- | --- | --- |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

SolidWorks can display a dimension more than once. For example, a base-extrude
dimension can be brought into three different views on a drawing. These
three dimensions are referred to as "Display Dimensions" and
are represented by the DisplayDimension object in the SolidWorks API.
The original base-extrude dimension is represented by the Dimension object
in the SolidWorks API.

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
<param name="Items" value="DisplayDimension_Object$$**$$ZGetDisplayDimension$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\DisplayDimension\DisplayDimension__GetNext.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
