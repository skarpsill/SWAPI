---
title: "PropertyManagerPage2Handler::OnClose"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler/PropertyManagerPage2Handler__OnClose.htm"
---

# PropertyManagerPage2Handler::OnClose

This method is obsolete and has been superseded
by[PropertyManagerPage2Handler2::OnClose](../PropertyManagerPage2Handler2/PropertyManagerPage2Handler2__OnClose.htm).

Description

This method is called when the PropertyManager
page is about to be closed.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler.OnClose ( Reason
)

(Table)=========================================================

| Input: | (long) Reason | Reason this method is being called as defined in swPropertyManagerPageCloseReasons_e |
| --- | --- | --- |

Syntax (COM)

status = PropertyManagerPage2Handler->OnClose
( Reason )

Parameters Table Start

(Table)=========================================================

| Input: | (long) Reason | Reason this method is being called as defined in swPropertyManagerPageCloseReasons_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful, S_FALSE to discontinue the
Close operation and leave the PropertyManager page open |

Remarks

This method is meant to be a pre-notification of
when a page is going close. At this point, before the page is gone, you
can collect the information that is currently in the page and save it.

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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\PropertyManagerPage2Handler\PropertyManagerPage2Handler__OnClose.htm" >
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
<param name="Items" value="PropertyManagerPage2Handler Method$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\PropertyManagerPage2Handler\PropertyManagerPage2Handler__OnClose.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
