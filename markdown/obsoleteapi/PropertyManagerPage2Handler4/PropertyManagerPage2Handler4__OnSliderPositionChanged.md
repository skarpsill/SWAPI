---
title: "PropertyManagerPage2Handler4::OnSliderPositionChanged"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnSliderPositionChanged.htm"
---

# PropertyManagerPage2Handler4::OnSliderPositionChanged

This method is obsolete and has been superseded
by[PropertyManagerPage2Handler5::OnSliderPositionChanged](sldworksAPI.chm::/PropertyManagerPage2Handler5/PropertyManagerPage2Handler5__OnSliderPositionChanged.htm).

Description

This method is called whenever
the user changes the position of a slider control on this PropertyManager.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler4.OnSliderPositionChanged
( Id, Value)

(Table)=========================================================

| Input: | (long) Id | ID of slider control |
| --- | --- | --- |
| Input: | (double) Value | Value indicating the new position
of the slider |

Syntax (COM)

status = PropertyManagerPage2Handler4->OnSliderPositionChanged
( Id, Value)

Parameters Table Start

(Table)=========================================================

| Input: | (long) Id | ID of slider control |
| --- | --- | --- |
| Input: | (double) Value | Value indicating the new position
of the slider |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Although Value is declared
as a double, the value of a slider is always a long. When this method
is called, Value can be cast to a long.

If PropertyManagerPageSlider::Style
is set to swPropMgrPageSliderStyle_NotifyWhileTracking, then you can use:

- PropertyManagerPage2Handler4::OnSliderPositionChanged
  to receive notifications every time the position of the slider changes
  because the slider is being dragged.NOTE:This might result in numerous calls to the handler, which
  is fine if the add-in responds quickly to each call. However, if the add-in
  responds slowly, then a performance bottleneck might occur.
- PropertyManagerPage2Handler4::OnSliderTrackingCompleted
  to receive one notification when dragging of the slider is completed.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes006$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PropertyManagerPage2Handler4\PropertyManagerPage2Handler4__OnSliderPositionChanged.htm" >
<param name="_ID" value="RelatedTopic2" >
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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="PropertyManagerPage2Handler4_Object$$**$$PropertyManagerPageHandlerOnSliderPositionChanged$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PropertyManagerPage2Handler4\PropertyManagerPage2Handler4__OnSliderPositionChanged.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
