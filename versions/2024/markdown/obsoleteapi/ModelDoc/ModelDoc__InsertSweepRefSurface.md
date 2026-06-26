---
title: "ModelDoc::InsertSweepRefSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertSweepRefSurface.htm"
---

# ModelDoc::InsertSweepRefSurface

This
method is obsolete and has been superseded by[ModelDoc::InsertSweepRefSurface2](ModelDoc__InsertSweepRefSurface2.htm).

Description

This method creates a reference surface by sweeping the selected profile
along the selected sweep curves. Because you are creating a surface, the
sections can be open.

Syntax (OLE Automation)

void ModelDoc.InsertSweepRefSurface
( propagate, twistCtrlOption, keepTangency, forceNonRational)

(Table)=========================================================

| Input: | (BOOL) propagate | If TRUE, then the sweep will propagate to the next edge, FALSE will
cause the sweep to occur only on the selected edge NOTE: To propagate to the next
edge, the next edge must be tangent to the current edge. |
| --- | --- | --- |
| Input: | (short) twistCtrlOption | Twist control options |
| Input: | (BOOL) keepTangency | Follow path |
| Input: | (BOOL) forceNonRational | Keep constant normal |

Syntax (COM)

status = ModelDoc->InsertSweepRefSurface
( propagate, twistCtrlOption, keepTangency, forceNonRational )

(Table)=========================================================

| Input: | (VARIANT_BOOL) propagate | If TRUE, then the sweep will propagate to the next edge, FALSE will
cause the sweep to occur only on the selected edge NOTE: To propagate to the next
edge, the next edge must be tangent to the current edge. |
| --- | --- | --- |
| Input: | (short) twistCtrlOption | Twist control options |
| Input: | (VARIANT_BOOL) keepTangency | Follow path |
| Input: | (VARIANT_BOOL) forceNonRational | Keep constant normal |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Use SelectByMark and AndSelectByMark to select the profile and sweep
curves. The markfor the profile
selection should be a 1; mark for the sweep path should be 4.If guide curve selection is provided, thenkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SelectByMark
markshould be 2.

The twistCtrlOption
may take one of the following values:

- 0
  = Follow path
- 1
  = Keep constant normal
- 2
  = Follow path and first guide curve
- 3
  = Follow first and second guide curve

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
<param name="Items" value="ModelDoc_Object$$**$$ZCreateRefSurface$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__InsertSweepRefSurface.htm" >
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__InsertSweepRefSurface.htm" >
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
<param name="Items" value="Entity::SelectByMark$$**$$ModelDoc::AndSelectByMark$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__InsertSweepRefSurface.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
