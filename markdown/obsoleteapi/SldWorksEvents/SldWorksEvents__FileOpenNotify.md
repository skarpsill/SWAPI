---
title: "FileOpenNotify - SldWorks Event"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorksEvents/SldWorksEvents__FileOpenNotify.htm"
---

# FileOpenNotify - SldWorks Event

This
event is obsolete and has been superseded bySldWorks
event[FileOpenNotify2](sldworksAPI.chm::/SldWorksEvents/SldWorksEvents__FileOpenNotify2.htm).

Description

Post-notifies the user program
when an existing file has been opened. SldWorks::GetOpenDocumentByName
can then be used with FileNameto get a pointer to the newly opened document.

status = FileOpenNotify ( FileName )

Parameters Table Start

(Table)=========================================================

| Input: | (BSTR) FileName | Name of the opened file |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This event is not sent to
any application when a file is opened programmatically using any SldWorks::OpenDoc*
method. Your application can detect the newly opened document by watching
the ActiveModelDocChangeNotify event.

SldWorks::OpenDoc2 and SldWorks::OpenDoc3
do send this event; however, to detect newly opened documents that are
opened from within some other application that still uses an SldWorks::OpenDoc*
method, you should still watch for the ActiveModelDocChangeNotify event.This event is not sent
when the user opens a file in view-only mode. However, an ActiveModelDocChangeNotify
event is sent.

With the exception of Parasolid
files (that is, *.x_t, *.x_b), this event is not sent for the opening
of non-native SolidWorks files (that is, *.igs, *.dxf, and so on).kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Non-native
file open are typically handled with the creation of a new SolidWorks
file (that is, *.sldprt, *.sldasm, *.slddrw) and the subsequent construction
of the foreign geometry within that file.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
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
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\SldWorksEvents\SldWorksEvents__FileOpenNotify.htm" >
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
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="FeatureData_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\SldWorksEvents\SldWorksEvents__FileOpenNotify.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
