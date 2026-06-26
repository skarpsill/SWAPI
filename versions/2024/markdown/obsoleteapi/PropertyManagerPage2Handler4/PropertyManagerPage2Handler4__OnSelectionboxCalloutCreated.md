---
title: "PropertyManagerPage2Handler4::OnSelectionboxCalloutCreated"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnSelectionboxCalloutCreated.htm"
---

# PropertyManagerPage2Handler4::OnSelectionboxCalloutCreated

This method is obsolete and has been superseded
by[PropertyManagerPage2Handler5::OnSelectionboxCalloutCreated](sldworksAPI.chm::/PropertyManagerPage2Handler5/PropertyManagerPage2Handler5__OnSelectionboxCalloutCreated.htm).

Description

This method does some processing
while the callout for the selection box is being created.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler4.OnSelectionboxCalloutCreated
( Id )

(Table)=========================================================

| Input: | (long) Id | ID of this selection box |
| --- | --- | --- |

Syntax (COM)

status = PropertyManagerPage2Handler4->OnSelectionboxCalloutCreated
( Id )

Parameters Table Start

(Table)=========================================================

| Input: | (long) Id | ID of this selection box |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is only called
if callouts have been enabled for the selection box as indicated by the
Id argument. Use PropertyManagerPageSelectionbox::SetCalloutLabel to enable
callouts.

You can collect information
using this method. For example, you can get the selection type from the
last selection. Next, use the PropertyManagerPageSelectionbox::Callout
property to get the Callout object. Then, use the various Callout properties
to control the callout text and display characteristics based on that
selection information.

This method is a pre-notification.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PropertyManagerPage2Handler4\PropertyManagerPage2Handler4__OnSelectionboxCalloutCreated.htm" >
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
<param name="Items" value="PropertyManagerPage2Handler4_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PropertyManagerPage2Handler4\PropertyManagerPage2Handler4__OnSelectionboxCalloutCreated.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
