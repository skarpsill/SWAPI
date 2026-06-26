---
title: "PropertyManagerPage2Handler4::OnKeystroke"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnKeystroke.htm"
---

# PropertyManagerPage2Handler4::OnKeystroke

This method is obsolete and has been superseded
by[PropertyManagerPage2Handler5::OnKeystroke](sldworksAPI.chm::/PropertyManagerPage2Handler5/PropertyManagerPage2Handler5__OnKeystroke.htm).

Description

This method processes a keystroke
that occurred on this PropertyManager page.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler4.OnKeystroke (
Wparam, Message, Lparam, Id)

(Table)=========================================================

| Input: | (long) Wparam | wparam argument from Windows
processing; indicates the keystroke that occurred NOTE: From the standard set of virtual keys from Windows. Refer
to the Virtual Key Code information from Microsoft documentation; for
example, the Alt key is VK_MENU. |
| --- | --- | --- |
| Input: | (long) Message | Message being processed by Windows;
one of these values: WM_KEYDOWN
0x0100 WM_KEYUP
0x0101 WM_CHAR
0x0102 WM_DEADCHAR
0x0103 WM_SYSKEYDOWN
0x0104 WM_SYSKEYUP
0x0105 WM_SYSCHAR
0x0106 WM_SYSDEADCHAR
0x0107 |
| Input: | (long) Lparam | lparam argument from Windows
processing; bitmask containing various pieces of information; dependent
on specific message |
| Input: | (long) Id | ID of the control that has focus
when the keystroke was made; this is the ID specified when the control
was created in PropertyManagerPage2::
AddControl or PropertyManagerPage2::AddGroupBox |

Syntax (COM)

status = PropertyManagerPage2Handler4->OnKeystroke
( Wparam, Message, Lparam, Id)

Parameters Table Start

(Table)=========================================================

| Input: | (long) Wparam | wparam argument
from Windows processing; indicates the keystroke that occurred NOTE: From the standard set of virtual keys from Windows. Refer
to the Virtual Key Code information from Microsoft documentation; for
example, the Alt key is VK_MENU. |
| --- | --- | --- |
| Input: | (long) Message | Message being processed by Windows;
one of these values: WM_KEYDOWN
0x0100 WM_KEYUP
0x0101 WM_CHAR
0x0102 WM_DEADCHAR
0x0103 WM_SYSKEYDOWN
0x0104 WM_SYSKEYUP
0x0105 WM_SYSCHAR
0x0106 WM_SYSDEADCHAR
0x0107 |
| Input: | (long) Lparam | lparam argument from Windows
processing; bitmask containing various pieces of information; dependent
on specific message |
| Input: | (long) Id | ID of the control that has focus
when the keystroke was made; this is the ID specified when the control
was created in PropertyManagerPage2::
AddControl or PropertyManagerPage2::AddGroupBox |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

After the add-in has finished
processing the keystroke, the message continues on and is processed by
Windows. Because processing must occur, nothing should be done to destroy
the page nor any action performed that could disrupt normal Windows processing
while the add-in is handling this keystroke.

To enable this functionality
for this PropertyManager page, set the Options argument of SldWorks::CreatePropertyManagerPage
to swPropertyManagerOptions_HandleKeystrokes. By default, this style is
not enabled because most applications are not interested in processing
keystrokes, and it is a potential performance bottleneck if lots of keystrokes
are occurring.

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
<param name="Items" value="ZReleaseNotes007$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PropertyManagerPage2Handler4\PropertyManagerPage2Handler4__OnKeystroke.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PropertyManagerPage2Handler4\PropertyManagerPage2Handler4__OnKeystroke.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
