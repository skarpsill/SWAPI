---
title: "DisplayDimension::GetDimension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DisplayDimension/DisplayDimension__GetDimension.htm"
---

# DisplayDimension::GetDimension

This method is obsolete and has been superseded
by[DisplayDimension::GetDimension2](sldworksAPI.chm::/DisplayDimension/DisplayDimension__GetDimension2.htm).

Description

This
method gets the model dimension that was used to create this display dimension.

Syntax (OLE Automation)

retval
= DisplayDimension.GetDimension ( )

(Table)=========================================================

| Return: | (LPDISPATCH)
retval | Pointer
to a Dispatch object, the model Dimension object |
| --- | --- | --- |

Syntax (COM)

status
= DisplayDimension->IGetDimension ( &retval )

(Table)=========================================================

| Output: | (LPDIMENSION)
retval | Pointer
to the Dimension object |
| --- | --- | --- |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

SolidWorks can display a dimension more than once. For example, a base-extrude
dimension can be brought into three different views on a drawing. These
three dimensions are referred to as display dimensions and are represented
by the DisplayDimension object in the SolidWorks API. The original base-extrude
dimension is represented by the Dimension object in the SolidWorks API.

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
<param name="Items" value="DisplayDimension_Object$$**$$ZGetDimension$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\DisplayDimension\DisplayDimension__GetDimension.htm" >
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
<param name="Items" value="Getting_DisplayDimension_Properties_Example$$**$$Traverse_Feature_Dimensions_Example$$**$$EXBlocks$$**$$IterateDimensions_Example$$**$$EXComponentDimension$$**$$EXDimensionTextValue$$**$$EXDimMidTolerance$$**$$EXUnlinkDimensions$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\DisplayDimension\DisplayDimension__GetDimension.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
