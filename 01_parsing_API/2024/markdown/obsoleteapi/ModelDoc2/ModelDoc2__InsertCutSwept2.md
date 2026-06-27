---
title: "ModelDoc2::InsertCutSwept2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertCutSwept2.htm"
---

# ModelDoc2::InsertCutSwept2

This
method is obsolete and has been superseded by ModelDoc2:InsertCutSwept3 .

Description

This method inserts a swept cut from the selected profile and the selected
sweep curves.

Syntax (OLE Automation)

void ModelDoc2.InsertCutSwept2
( propagate, alignment, twistCtrlOption, keepTangency, forceNonRational)

(Table)=========================================================

| Input: | (BOOL) propagate | TRUE propagates the swept cut will propagate to the next edge, FALSE
causes the swept cut to occur only on the selected edge; to propagate
to the next edge, the next edge must be tangent to the current edge |
| --- | --- | --- |
| Input: | (BOOL) alignment | If the curve used to sweep goes from on face to another, or from one
edge to another, passing TRUE causes the sweep to cut completely through
the end faces of the cut, FALSE causes the swept cut to begin and end
perpendicular to the sweep curve; therefore, it may not break through
the two end faces of the body being cut |
| Input: | (short) twistCtrlOption | 0
= Follow path 1
= Keep constant normal 2
= Follow path and first guide curve 3
= Follow first and second guide curve |
| Input: | (BOOL) keepTangency | Follow path |
| Input: | (BOOL) forceNonRational | Keep constant normal |

Syntax (COM)

status = ModelDoc2->InsertCutSwept2
( propagate, alignment, twistCtrlOption, keepTangency, forceNonRational
)

(Table)=========================================================

| Input: | (VARIANT_BOOL) propagate | TRUE propagates the swept cut will propagate to the next edge, FALSE
causes the swept cut to occur only on the selected edge; to propagate
to the next edge, the next edge must be tangent to the current edge |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) alignment | If the curve used to sweep goes from on face to another, or from one
edge to another, passing TRUE causes the sweep to cut completely through
the end faces of the cut, FALSE causes the swept cut to begin and end
perpendicular to the sweep curve; therefore, it may not break through
the two end faces of the body being cut |
| Input: | (short) twistCtrlOption | 0
= Follow path 1
= Keep constant normal 2
= Follow path and first guide curve 3
= Follow first and second guide curve |
| Input: | (VARIANT_BOOL) keepTangency | Follow path |
| Input: | (VARIANT_BOOL) forceNonRational | Keep constant normal |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use ModelDocExtension::SelectByIDto select
the profile and sweep curves. The markfor the profile selection should be a 1 while the mark for the
sweep path should be4.If guide
curve selection is provided, markshould
be2.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc2\ModelDoc2__InsertCutSwept2.htm" >
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc2\ModelDoc2__InsertCutSwept2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
