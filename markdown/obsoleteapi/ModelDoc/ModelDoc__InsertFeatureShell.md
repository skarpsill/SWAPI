---
title: "ModelDoc::InsertFeatureShell"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertFeatureShell.htm"
---

# ModelDoc::InsertFeatureShell

This
method is obsolete and has been superseded byM[odelDoc2::InsertFeatureShell](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertFeatureShell.htm).

Description

This method creates a shell feature.

Syntax (OLE Automation)

void ModelDoc.InsertFeatureShell (
thickness, outward)

(Table)=========================================================

| Input: | (double) thickness | Shell thickness in meters |
| --- | --- | --- |
| Input: | (BOOL) outward | TRUE for outside, FALSE for inside |

Syntax (COM)

status = ModelDoc->InsertFeatureShell
( thickness, outward )

(Table)=========================================================

| Input: | (double) thickness | Shell thickness in meters |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) outward | TRUE for outside, FALSE for inside |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is the same as interactively creating a planar surface by
selectingInsert,
Features,Shell.

See the SolidWorks Help for more information about what
entities are valid for selection.

Make the selections using ModelDoc::SelectByID before calling this method.

To make a multi-thickness shell, you can make additional calls to ModelDoc::InsertFeatureShellAddThickness
after making the selections and before calling this method.

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
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__InsertFeatureShell.htm" >
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
<param name="Items" value="MultiThicknessShell_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__InsertFeatureShell.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
