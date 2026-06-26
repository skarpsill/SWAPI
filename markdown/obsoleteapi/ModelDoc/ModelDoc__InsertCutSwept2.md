---
title: "ModelDoc::InsertCutSwept2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertCutSwept2.htm"
---

# ModelDoc::InsertCutSwept2

This method is obsolete
and has been superseded by[ModelDoc::InsertCutBlend3](ModelDoc__InsertCutBlend4.htm)

Description

This method inserts a swept cut from the selected profile and the selected
sweep curves.

Syntax (OLE Automation)

void ModelDoc.InsertCutSwept2 ( propagate,
alignment, twistCtrlOption, keepTangency, forceNonRational)

(Table)=========================================================

| Input: | (BOOL) propagate | If TRUE, then the swept cut will propagate to the next edge, FALSE will
cause the swept cut to occur only on the selected edge; to propagate to
the next edge, the next edge must be tangent to the current edge |
| --- | --- | --- |
| Input: | (BOOL) alignment | If the curve used to sweep goes from on face to another, or from one
edge to another, passing TRUE will cause the sweep to cut completely through
the end faces of the cut; if you choose FALSE, then the swept cut will
begin and end perpendicular to the sweep curve and, therefore, may not
break through the two end faces of the body being cut |
| Input: | (short) twistCtrlOption | Specify one of the following twist control options: 0 = Follow path 1 = Keep constant normal 2 = Follow path and
first guide curve 3 = Follow first and
second guide curve |
| Input: | (BOOL) keepTangency | Follow path |
| Input: | (BOOL) forceNonRational | Keep constant normal |

Syntax (COM)

status = ModelDoc->InsertCutSwept2
( propagate, alignment, twistCtrlOption, keepTangency, forceNonRational
)

(Table)=========================================================

| Input: | (VARIANT_BOOL) propagate | If TRUE, then the swept cut will propagate to the next edge, FALSE will
cause the swept cut to occur only on the selected edge; to propagate to
the next edge, the next edge must be tangent to the current edge |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) alignment | If the curve used to sweep goes from on face to another, or from one
edge to another, passing TRUE will cause the sweep to cut completely through
the end faces of the cut; if you choose FALSE, then the swept cut will
begin and end perpendicular to the sweep curve and, therefore, may not
break through the two end faces of the body being cut |
| Input: | (short) twistCtrlOption | Specify one of the following twist control options: 0 = Follow path 1 = Keep constant normal 2 = Follow path and
first guide curve 3 = Follow first and
second guide curve |
| Input: | (VARIANT_BOOL) keepTangency | Follow path |
| Input: | (VARIANT_BOOL) forceNonRational | Keep constant normal |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use a SelectByMark method to select the profile and sweep curves. The
markfor the profile selection
should be a 1 while the mark for the sweep path should be4.If guide curve selection is provided, the SelectByMark markshould be2.

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
<param name="Items" value="ModelDoc_Object$$**$$ZInsertFeature$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__InsertCutSwept2.htm" >
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
<param name="Items" value="Entity::SelectByMark$$**$$ModelDoc::SelectByMark$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__InsertCutSwept2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
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
<param name="Items" value="Entity::SelectByMark$$**$$ModelDoc::SelectByMark$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__InsertCutSwept2.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
