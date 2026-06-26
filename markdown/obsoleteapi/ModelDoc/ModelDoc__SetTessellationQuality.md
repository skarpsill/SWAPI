---
title: "ModelDoc::SetTessellationQuality"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetTessellationQuality.htm"
---

# ModelDoc::SetTessellationQuality

This method is obsolete
and has been superseded by[ModelDoc2::SetTessellationQuality](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetTessellationQuality.htm).

Description

This method sets the tessellation quality index for the application.

Syntax (OLE Automation)

void ModelDoc.SetTessellationQuality
( qualityNum)

(Table)=========================================================

| Input: | (long) qualityNum | Number between 0 and 100, which indicates the quality of tessellation
to use for this part; a higher index means finer tessellation |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->SetTessellationQuality
( qualityNum )

(Table)=========================================================

| Input: | (long) qualityNum | Number between 0 and 100, which
indicates the quality of tessellation to use for this part; a higher index
means finer tessellation |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method changes the shaded-display quality setting that you find
on theTools, Option, Performancemenu.

The numeric deviation value will change based on the current part. This
deviation is calculated as follows:

Deviation = 0.025 * (BodyDiameter) / qualityIndex;

where BodyDiameter is the diagonal distance across the bounds of the
part box . See PartDoc::GetPartBox.

The resulting Deviation value is in meters.

NOTE:This method sets the quality in the overall environment, not just the
current part.

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
<param name="Items" value="ModelDoc_Object$$**$$ZTessellation$$**$$ZModifyUserPreference$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__SetTessellationQuality.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
