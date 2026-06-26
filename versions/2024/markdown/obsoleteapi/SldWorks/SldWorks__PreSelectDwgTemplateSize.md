---
title: "SldWorks::PreSelectDwgTemplateSize"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__PreSelectDwgTemplateSize.htm"
---

# SldWorks::PreSelectDwgTemplateSize

This method is obsolete and has been superseded
by[SldWorks::PresetNewDrawingParameters](sldworksAPI.chm::/SldWorks/SldWorks__PresetNewDrawingParameters.htm)and[SldWorks::ResetPresetDrawingParameters](sldworksAPI.chm::/SldWorks/SldWorks__ResetPresetDrawingParameters.htm).

Description

This method establishes which template to use when creating a drawing.
By calling this method and specifying a template size, no dialog appears
when the end-user interactively selectsFile,
New, Drawing.

Syntax (OLE Automation)

void SldWorks.PreSelectDwgTemplateSize
( templateToUse, templateName)

(Table)=========================================================

| Input: | (long) templateToUse | Type of template to use as defined in swDwgTemplates_e |
| --- | --- | --- |
| Input: | (BSTR) templateName | Reserved for future use; use NULL |

Syntax (COM)

status = SldWorks->PreSelectDwgTemplateSize
( templateToUse, templateName )

(Table)=========================================================

| Input: | (long) templateToUse | Type of template to use as defined in swDwgTemplates_e |
| --- | --- | --- |
| Input: | (BSTR) templateName | Reserved for future use; use NULL |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="SldWorks_Object$$**$$ZFileOperations$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\SldWorks\SldWorks__PreSelectDwgTemplateSize.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
