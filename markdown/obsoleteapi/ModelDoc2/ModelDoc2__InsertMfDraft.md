---
title: "ModelDoc2::InsertMfDraft"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertMfDraft.htm"
---

# ModelDoc2::InsertMfDraft

This method is obsolete and has been superseded
by[ModelDoc2::InsertMfDraft2](ModelDoc2__InsertMfDraft2.htm).

Description

This method creates a multi-face draft.

Syntax (OLE Automation)

void ModelDoc2.InsertMfDraft ( angle,
flipDir, isEdgeDraft, propType)

(Table)=========================================================

| Input: | (double) angle | Draft angle in radians |
| --- | --- | --- |
| Input: | (BOOL) flipDir | Flip the direction of the draft; the draft direction is determined by
the selected direction, which can be a planar face, a reference plane,
an edge, or two vertices; if you refer to the last argument in ModelDoc2::SelectByMark
and ModelDoc2::AndSelectByMark, these items would have a selection mark
of 1; faces to be drafted have a selection mark of 2 and the draft edges
have a selection mark of 4 |
| Input: | (BOOL) isEdgeDraft | Determines if it is an edge or neutral plane draft; TRUE if this is
an edge draft and the user select edges to draft, FALSE if this is a face
draft and the user selects
faces draft (the system automatically selects the faces next to the edge
to be drafted) |
| Input: | (long) propType | Propagation type |

Syntax (COM)

status = ModelDoc2->InsertMfDraft
( angle, flipDir, isEdgeDraft, propType )

(Table)=========================================================

| Input: | (double) angle | Draft angle in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) flipDir | Flip the direction of the draft; the draft direction is determined by
the selected direction, which can be a planar face, a reference plane,
an edge, or two vertices; if you refer to the last argument in ModelDoc2::SelectByMark
and ModelDoc2::AndSelectByMark, these items would have a selection mark
of 1; faces to be drafted have a selection mark of 2 and the draft edges
have a selection mark of 4 |
| Input: | (VARIANT_BOOL) isEdgeDraft | Determines if it is an edge or neutral plane draft; TRUE if this is
an edge draft and the user select edges to draft, FALSE if this is a face
draft and the user selects
faces draft (the system automatically selects the faces next to the edge
to be drafted) |
| Input: | (long) propType | Propagation type |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The propagation type argument propType can be one
of these values:

- 0 = no propagation.
- 1 = propagate
  to the next tangent faces that share the base neutral plane. You can specify
  this option for edge draft or neutral plane draft.
- 2 = propagate
  to all faces that are a neighbor of the neutral plane.
- 3 = propagate
  to all faces that are a neighbor of the neutral plane on all the inner
  loops (for example, all faces of a pocket or a boss).
- 4 = propagate
  to all faces that are a neighbor of the neutral plane on the outer loop
  (for example, the sides of a box with the bottom face as neutral plane).

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc2\ModelDoc2__InsertMfDraft.htm" >
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
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc2\ModelDoc2__InsertMfDraft.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
