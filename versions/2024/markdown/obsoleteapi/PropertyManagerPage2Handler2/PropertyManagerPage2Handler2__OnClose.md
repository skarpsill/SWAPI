---
title: "PropertyManagerPage2Handler2::OnClose"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler2/PropertyManagerPage2Handler2__OnClose.htm"
---

# PropertyManagerPage2Handler2::OnClose

This method is obsolete and has been superseded
by[PropertyManagerPage2Handler3::OnClose](../PropertyManagerPage2Handler3/PropertyManagerPage2Handler3__OnClose.htm).

Description

This method is called when
this PropertyManager is closing.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler2.OnClose ( Reason
)

(Table)=========================================================

| Input: | (long) Reason | Reason this method is called as defined in swPropertyManagerPageCloseReasons_e |
| --- | --- | --- |

Syntax (COM)

status = PropertyManagerPage2Handler2->OnClose
( Reason )

Parameters Table Start

(Table)=========================================================

| Input: | (long) Reason | Reason this method is called as defined in swPropertyManagerPageCloseReasons_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This handler method is called
when the page is about to close.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

(Table)=========================================================

| If you implemented the handler in... | Then you... |
| --- | --- |
| C++ | Can prevent the page from closing by setting the HRESULT return value
to S_FALSE |
| VB | Should use the Err.Raise method with a value of 1 to prevent the page
from closing |
| NOTE: When
control returns to SolidWorks: These
values are recognized. The
page remains displayed on the screen. The
PropertyManagerPage2Handler2::AfterClose handler is not called. |  |

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
<param name="Items" value="ZReleaseNotes2003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\PropertyManagerPage2Handler2\PropertyManagerPage2Handler2__OnClose.htm" >
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
<param name="Items" value="PropertyManagerPage2Handler2_Object$$**$$PropertyManagerPage2Pushpin$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\PropertyManagerPage2Handler2\PropertyManagerPage2Handler2__OnClose.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
