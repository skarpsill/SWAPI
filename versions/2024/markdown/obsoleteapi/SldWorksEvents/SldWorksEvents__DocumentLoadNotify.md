---
title: "DocumentLoadNotify - SldWorks Event"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorksEvents/SldWorksEvents__DocumentLoadNotify.htm"
---

# DocumentLoadNotify - SldWorks Event

## D ocumentLoadNotify - SldWorks Event

This event is obsolete and has been superseded
by[SldWorksEvent::DocumentLoadNotify2](sldworksAPI.chm::/SldWorksEvents/SldWorksEvents__DocumentLoadNotify2.htm).

Description

Post-notifies the user program
when a SolidWorks document is loaded.

NOTE:If developing a C++ application, use swAppDocumentLoadNotify to register
for this notification.

status = DocumentLoadNotify ( docTitle , docPath
)

(Table)=========================================================

| Input: | (BSTR) docTitle | Document title |
| --- | --- | --- |
| Input: | (BSTR) docPath | Document path |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This event is fired for documents
referenced by assemblies and drawings. Client code should expect multiple
calls to this event handler when an assembly or drawing is loaded.

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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\SldWorksEvents\SldWorksEvents__DocumentLoadNotify.htm" >
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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="SldWorks_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\SldWorksEvents\SldWorksEvents__DocumentLoadNotify.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
