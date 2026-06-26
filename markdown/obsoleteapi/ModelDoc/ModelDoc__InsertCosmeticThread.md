---
title: "ModelDoc::InsertCosmeticThread"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertCosmeticThread.htm"
---

# ModelDoc::InsertCosmeticThread

This
method is obsolete and has been superseded by[ModelDoc2::InsertCosmeticThread](../ModelDoc2/ModelDoc2__InsertCosmeticThread.htm).

Description

This method inserts a cosmetic-thread annotation based on the selected
edge.

Syntax (OLE Automation)

void ModelDoc.InsertCosmeticThread
( type, dia, length, note)

(Table)=========================================================

| Input: | (short) type | Thread type where Blind = 0 and UpToNext = 1 |
| --- | --- | --- |
| Input: | (double) dia | Major diameter |
| Input: | (double) length | Thread depth (length) |
| Input: | (BSTR) note | Callout string to display in the drawing document |

Syntax (COM)

status = ModelDoc->InsertCosmeticThread
( type, dia, length, note )

(Table)=========================================================

| Input: | (short) type | Thread type where Blind = 0 and UpToNext = 1 |
| --- | --- | --- |
| Input: | (double) dia | Mmajor diameter |
| Input: | (double) length | Thread depth (length) |
| Input: | (BSTR) note | Callout string to display in the drawing document |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__InsertCosmeticThread.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
