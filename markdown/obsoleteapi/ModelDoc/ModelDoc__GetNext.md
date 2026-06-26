---
title: "ModelDoc::GetNext"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetNext.htm"
---

# ModelDoc::GetNext

This
method is obsolete and has been superseded by[ModelDoc2::GetNext](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetNext.htm).

Description

This methodgets
the next document in the current SolidWorks session.

Syntax (OLE Automation)

nextDoc = ModelDoc.GetNext
( )

(Table)=========================================================

| Return: | (LPDISPATCH) nextDoc | Pointer to a Dispatch object, the next ModelDoc
object |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetNext
( &nextDoc )

(Table)=========================================================

| Output: | (LPMODELDOC) nextDoc | Pointer to the next ModelDoc object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The COM version of this method
is available in[datecode](../SldWorks/SldWorks__DateCode.htm)1999/207 and later.

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
<param name="Items" value="ModelDoc_Object$$**$$ZEnumDocuments$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__GetNext.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
