---
title: "ModelDoc::AlignDimensions"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AlignDimensions.htm"
---

# ModelDoc::AlignDimensions

This
method is obsolete and has been superseded by[ModelDoc2::AlignDimensions](sldworksAPI.chm::/ModelDoc2/ModelDoc2__AlignDimensions.htm).

Description

This method aligns the selected dimensions co-linearly.

Syntax (OLE Automation)

(void) ModelDoc.AlignDimensions
( )

Syntax (COM)

status = ModelDoc->AlignDimensions
( )

(Table)=========================================================

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

This method attempts to sort the dimensions selected
into three groups: linear, ordinate, and angular dimensions. Within the
linear group, this method sorts by measured direction. Each of these dimensions
are then aligned with the other like dimensions. These dimensions are
then updated and dragged together.

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
<param name="Items" value="ModelDoc_Object$$**$$ZModifyDimension$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__AlignDimensions.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
