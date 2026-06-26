---
title: "ModelDoc::SketchConvertIsoCurves"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchConvertIsoCurves.htm"
---

# ModelDoc::SketchConvertIsoCurves

This method is obsolete
and has been superseded by[ModelDoc2::SketchConvertIsoCurves](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SketchConvertIsoCurves.htm).

Description

This method converts an ISO-parametric curve
or curves on a selected surface into a sketch entity.

Syntax (OLE Automation)

void ModelDoc.SketchConvertIsoCurves ( percentRatio,
vORuDir, doConstrain, skipHoles)

(Table)=========================================================

| Input: | (double) percentRatio | Value for percent ratio |
| --- | --- | --- |
| Input: | (BOOL) vORuDir | TRUE for V direction, FALSE for U direction |
| Input: | (BOOL) doConstrain | TRUE if you want to constrain these new sketch
entities, FALSE otherwise |
| Input | (BOOL) skipHoles | TRUE if you want to skip the holes in this surface,
FALSE otherwise |

Syntax (COM)

status = ModelDoc->SketchConvertIsoCurves ( percentRatio,
vORuDir, doConstrain)

(Table)=========================================================

| Input: | (double) percentRatio | Value for percent ratio |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) vORuDir | TRUE for V direction, FASLE for U direction |
| Input: | (VARIANT_BOOL) doConstrain | TRUE if you want to constrain these new sketch
entities, FALSE otherwise |
| Input | (VARIANT_BOOL) skipHoles | TRUE if you want to skip the holes in this surface,
FALSE otherwise |
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SketchConvertIsoCurves.htm" >
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SketchConvertIsoCurves.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
