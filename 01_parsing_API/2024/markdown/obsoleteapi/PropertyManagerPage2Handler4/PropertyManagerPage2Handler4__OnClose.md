---
title: "PropertyManagerPage2Handler4::OnClose"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnClose.htm"
---

# PropertyManagerPage2Handler4::OnClose

This method is obsolete and has been superseded
by[PropertyManagerPage2Handler5::OnClose.](sldworksAPI.chm::/PropertyManagerPage2Handler5/PropertyManagerPage2Handler5__OnClose.htm)

Description

This method is called when
this PropertyManager page is closing.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler4.OnClose ( Reason
)

(Table)=========================================================

| Input: | (long) Reason | Reason this method is called as defined in swPropertyManagerPageCloseReasons_e |
| --- | --- | --- |

Syntax (COM)

status = PropertyManagerPage2Handler4->OnClose
( Reason )

Parameters Table Start

(Table)=========================================================

| Input: | (long) Reason | Reason this method is called as defined in swPropertyManagerPageCloseReasons_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This handler method is called
when the PropertyManager page is about to close.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

SolidWorks controls when add-ins
can do work. An add-in is unable to do any real work within the PropertyManager2Handler::OnClose
handler because the PropertyManager page and command are closing. So,
typically the PropertyPage2Handler4::AfterClose handler is called after
PropertyManager2Handler4::OnClose to allow an add-in to do work. However:

(Table)=========================================================

| If PropertyManager page is... | And you implemented the handler in... | Then you... |
| --- | --- | --- |
| Not pinned | C++ | Can prevent the PropertyManager page from closing by setting the HRESULT
return value to S_FALSE. |
|  | Visual Basic | Should use the Err.Raise method with a value of 1 to prevent the PropertyManager
page from closing. In VB.NET, use 0 with Err.Raise. |
|  | NOTE: When
control returns to SolidWorks: The
PropertyManager page remains displayed on the screen. The
PropertyManagerPage2Handler4::AfterClose handler is not called. |  |
| Pinned | C++ or Visual Basic | Set HRESULT to S_FALSE to close the PropertyManager page (i.e., ignore
the fact that the page is pinned). This allows your add-in to call the PropertyManagerPage2Handler4::AfterClose
handler and do its work. To avoid aggravating your user, who expected
the PropertyManager page to
remain pinned, you should re-display and re-pin the PropertyManager page
after the add-in finishes its work. |

NOTE:In the previous version of this method, PropertyManagerPage2Handler3::OnClose,
if the user clicked the Cancel button and the PropertyManager page had
a pushpin, then this method returned swPropertyManagerPageClose_Closed.
This version of this method returns swPropertyManagerPageClose_Cancel
in this scenario.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PropertyManagerPage2Handler4\PropertyManagerPage2Handler4__OnClose.htm" >
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
<param name="Items" value="PropertyManagerPage2Handler4_Object$$**$$PropertyManagerPage2Pushpin$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PropertyManagerPage2Handler4\PropertyManagerPage2Handler4__OnClose.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic5
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
<param name="Items" value="EXTrapErrorWhenClosingPropertyManagerPage$$**$$EXCreatePropertyManagerPage$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PropertyManagerPage2Handler4\PropertyManagerPage2Handler4__OnClose.htm" >
<param name="_ID" value="RelatedTopic5" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
