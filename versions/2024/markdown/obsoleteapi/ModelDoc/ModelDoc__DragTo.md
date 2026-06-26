---
title: "ModelDoc::DragTo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__DragTo.htm"
---

# ModelDoc::DragTo

This
method is obsolete and has been superseded by[ModelDoc2::DragTo](sldworksAPI.chm::/ModelDoc2/ModelDoc2__DragTo.htm).

Description

This method drags the specified end point.

Syntax (OLE Automation)

void ModelDoc.DragTo ( flags, x, y,
z)

(Table)=========================================================

| Input: | (long) flags | The flags represent the mouse event flags that come from the operating
system as defined by the operating system. They can be combined to indicate
the selection state. For
example: Left-mouse button is pressed: 0x0001 Right-mouse button is pressed: 0x0002 Shift key is pressed: 0x0004 Ctrl key is pressed: 0x0008 Middle-mouse button is pressed: 0x0010 |
| --- | --- | --- |
| Input: | (double) x | X coordinate of end point |
| Input: | (double) y | Y coordinate of end point |
| Input: | (double) z | Z coordinate of end point |

Syntax (COM)

status = ModelDoc->DragTo ( flags,
x, y, z )

(Table)=========================================================

| Input: | (long) flags | The flags represent the mouse event flags that come from the operating
system as defined by the operating system. They can be combined to indicate
the selection state. For
example: Left-mouse button is pressed: 0x0001 Right-mouse button is pressed: 0x0002 Shift key is pressed: 0x0004 Ctrl key is pressed: 0x0008 Middle-mouse button is pressed: 0x0010 |
| --- | --- | --- |
| Input: | (double) x | X coordinate of end point |
| Input: | (double) y | Y coordinate of end point |
| Input: | (double) z | Z coordinate of end point |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__DragTo.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
