---
title: "FileSaveAsNotify - AssemblyDoc Event"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDocEvents/AssemblyDocEvents__FileSaveAsNotify.htm"
---

# FileSaveAsNotify - AssemblyDoc Event

This event is obsolete and has been superseded
by the AssemblyDoc event[FileSaveAsNotify2](sldworksAPI.chm::/AssemblyDocEvents/AssemblyDocEvents__FileSaveAsNotify2.htm).

Description

This event pre-notifies the
user program when a file is about to be saved with a new name and passes
the new document name.

status = FileSaveAsNotify ( FileName )

(Table)=========================================================

| Input: | (BSTR) FileName | New document name |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You might want to check the file extension on the
filename passed to your application because the user may have saved this
document as IGES, DXF, and so on. When a user saves a document for the
first time, SolidWorks generates a FileSaveAsNotify event instead of a
FileSaveNotify event.

You can return S_FALSE to stop SolidWorks from
proceeding with the action that caused the notification.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\AssemblyDocEvents\AssemblyDocEvents__FileSaveAsNotify.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
