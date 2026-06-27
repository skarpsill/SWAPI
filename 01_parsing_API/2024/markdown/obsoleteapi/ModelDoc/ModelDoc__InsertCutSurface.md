---
title: "ModelDoc::InsertCutSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertCutSurface.htm"
---

# ModelDoc::InsertCutSurface

This
method is obsolete and has been superseded by[ModelDoc2::InsertCutSurface](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertCutSurface.htm).

Description

This method creates a surface cut feature.

Syntax (OLE Automation)

void ModelDoc.InsertCutSurface ( flip,
keepPieceIndex )

(Table)=========================================================

| Input: | (BOOL) flip | TRUE to flip the direction |
| --- | --- | --- |
| Input: | (long) keepPieceIndex | Piece to keep if there is ambiguity |

Syntax (COM)

status = ModelDoc->InsertCutSurface
( flip, keepPieceIndex )

(Table)=========================================================

| Input: | (VARIANT_BOOL) flip | TRUE to flip the direction |
| --- | --- | --- |
| Input: | (long) keepPieceIndex | Piece to keep if there is ambiguity |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method creates a cut from a selected surface.

When there is ambiguity in the result of a cut, the keepPieceIndex is
used to resolve which of the possible results is used. This can be set
to -1 if there is no ambiguity; otherwise, it should be the index of the
result, starting from 0 (up to 1 less than the possible number of outcomes).

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__InsertCutSurface.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
