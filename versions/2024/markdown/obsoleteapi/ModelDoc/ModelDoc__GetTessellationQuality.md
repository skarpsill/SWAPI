---
title: "ModelDoc::GetTessellationQuality"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetTessellationQuality.htm"
---

# ModelDoc::GetTessellationQuality

This
method is obsolete and has been superseded by[ModelDoc2::GetTessellationQuality](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetTessellationQuality.htm).

Description

This method getskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}the
tessellation quality index for the application.

Syntax (OLE Automation)

retval = ModelDoc.GetTessellationQuality
()

(Table)=========================================================

| Return: | (long) retval | Number between 0 and 100 that indicates the quality of tessellation
to use for this part; a higher index means finer tessellation |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetTessellationQuality
( &retval )

(Table)=========================================================

| Output: | (long) retval | Number between 0 and 100 that indicates the quality of tessellation
to use for this part; a higher index means finer tessellation |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method returns the shaded-display quality setting that you find
on theTools, Options, Performancemenu. The numeric deviation value changes based on the current part. This
deviation is calculated as follows:

Deviation = 0.025 * ( BodyDiameter )
/qualityIndex;

where the BodyDiameter is the diagonal distance across the bounds of the part box. SeePartDoc::GetPartBox
for details.

The Deviation value is in meters.

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__GetTessellationQuality.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
