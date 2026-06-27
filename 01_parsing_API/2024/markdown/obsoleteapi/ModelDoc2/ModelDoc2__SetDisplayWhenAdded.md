---
title: "ModelDoc2::SetDisplayWhenAdded"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SetDisplayWhenAdded.htm"
---

# ModelDoc2::SetDisplayWhenAdded

This method is obsolete and has been superseded
by[SketchManager::DisplayWhenAdded](sldworksAPI.chm::/SketchManager/SketchManager__DisplayWhenAdded.htm).

Description

This method sets whether new sketch entities are displayed when created.

Syntax (OLE Automation)

void ModelDoc2.SetDisplayWhenAdded
( setting)

(Table)=========================================================

| Input: | (BOOL) setting | TRUE to display new sketch entities when added, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->SetDisplayWhenAdded
( setting )

(Table)=========================================================

| Input: | (VARIANT_BOOL) setting | TRUE to display new sketch entities when added, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The sketch entities appear on the screen after performing ModelDoc2::GraphicsRedraw2
or ModelDoc2::EditRebuild3 is performed. Also, ModelDoc2::SetAddToDB must
be TRUE to use this method's settings.

This display setting remains even after your program run has ended.
Therefore, it is recommended that you reset this parameter to TRUE at
the end of your program. For example, if you have ended your program and
the display is set to FALSE, then the user would have difficulty performing
selections and newly created entities would not be seen until a redraw
or a rebuild.

NOTES:

- ModelDoc2::GraphicsRedraw2 is much faster than
  ModelDoc2::EditRebuild3.
- ModelDoc2::SetAddToDB and ModelDoc2::SetDisplayWhenAdded
  also increase performance during sketch entity creation.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__SetDisplayWhenAdded.htm" >
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
<param name="Items" value="ModelDoc2_Object$$**$$SketchDBDisplay$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__SetDisplayWhenAdded.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic5
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
<param name="Items" value="EXOutsideEdgesFace$$**$$EXReturnUntrimmedCurve$$**$$EXGetBoundingBox$$**$$EXGetSplineEllipticalEdge$$**$$EXTessellateBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__SetDisplayWhenAdded.htm" >
<param name="_ID" value="RelatedTopic5" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
