---
title: "SldWorks::ShowToolbar2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__ShowToolbar2.htm"
---

# SldWorks::ShowToolbar2

This method is obsolete. SolidWorks manages
the display of the toolbars based on the user's action; therefore, this
method is not needed. There are no alternative methods available to use.

Description

This method displays a toolbar that was created
with SldWorks::AddToolbar3.

Syntax (OLE Automation)

Status = SldWorks.ShowToolbar2 ( Cookie, ToolbarID
)

(Table)=========================================================

| Input: | (long) Cookie | Resource ID of the toolbar; this is the same cookie that you specified
in SwAddin::ConnectToSW |
| --- | --- | --- |
| Input: | (long) ToolbarID | Toolbar ID |
| Output: | (VARIANT_BOOL) Status | TRUE if successful, FALSE if unsuccessful |

Syntax (COM)

status = SldWorks->ShowToolbar2 ( Cookie, ToolbarID,
&Status )

Parameters Table Start

(Table)=========================================================

| Input: | (long) Cookie | Resource ID of the toolbar; this is the same cookie that you specified
in SwAddin::ConnectToSW |
| --- | --- | --- |
| Input: | (long) ToolbarID | Toolbar ID |
| Output: | (VARIANT_BOOL) Status | TRUE if successful, FALSE if unsuccessful |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For information about using this method with the
SwAddin object, see Using SwAddin to Create a SolidWorks Add-in.

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\SldWorks\SldWorks__ShowToolbar2.htm" >
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
<param name="Items" value="SldWorks Method$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\SldWorks\SldWorks__ShowToolbar2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
