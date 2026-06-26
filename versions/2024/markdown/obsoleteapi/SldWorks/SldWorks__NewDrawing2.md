---
title: "SldWorks::NewDrawing2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__NewDrawing2.htm"
---

# SldWorks::NewDrawing2

This
method is obsolete and has been superseded by[SldWorks::NewDocument](sldworksAPI.chm::/SldWorks/SldWorks__NewDocument.htm)or[SldWorks::INewDocument2](sldworksAPI.chm::/SldWorks/SldWorks__INewDocument2.htm).

Description

This method creates a new drawing document with a template or custom
size. The drawing document is named automatically.

Syntax (OLE Automation)

retval = SldWorks.NewDrawing2 ( templateToUse,
templateName, paperSize, width, height)

(Table)=========================================================

| Input: | (long) templateToUse | Type of template to use as defined as swDwgTemplates_e |
| --- | --- | --- |
| Input: | (BSTR) templateName | Name of custom template with full directory path if using swDwgTemplateCustom |
| Input: | (long) paperSize | Size of paper if using swDwgTemplateNone as defined in swDwgPaperSizes_e |
| Input: | (double) width | Paper width if using swDwgTemplateNone and swDwgPapersUserDefined |
| Input: | (double) height | Paper height if using swDwgTemplateNone and swDwgPapersUserDefined |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created drawing or NULL if the
operation fails |

Syntax (COM)

status = SldWorks->INewDrawing2
( templateToUse, templateName, paperSize, width, height, &retval )

(Table)=========================================================

| Input: | (long) templateToUse | Type of template to use as defined as swDwgTemplates_e |
| --- | --- | --- |
| Input: | (BSTR) templateName | Name of custom template with full directory path if using swDwgTemplateCustom |
| Input: | (long) paperSize | Size of paper if using swDwgTemplateNone as defined in swDwgPaperSizes_e |
| Input: | (double) width | Paper width if using swDwgTemplateNone and swDwgPapersUserDefined |
| Input: | (double) height | Paper height if using swDwgTemplateNone and swDwgPapersUserDefined |
| Output: | (LPDRAWINGDOC) retval | Pointer to a newly created drawing or NULL if the operation fails |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Calling this method erases any settings made with the SldWorks::PreSelectDwgTemplateSize.

If the custom template or standard template file
is not found, then the drawing is created without a template, as if swDwgTemplateNone
was specified. If that happens, the paperSize argument is used to determine
the size of the drawing. If the paper size is swDwgPapersUserDefined,
then the width and height values are used to determine the size of the
drawing. If the paperSize, width, or height is invalid, the paper size
defaults to swDwgPaperAsize.

To set the document title without saving the file,
see ModelDoc2::SetTitle2.

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
<param name="Items" value="SldWorks_Object$$**$$ZFileOperations$$**$$ModelDoc$$**$$DrawingDoc$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\SldWorks\SldWorks__NewDrawing2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Create_Sketch_Line_With_Visual_Properties_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\SldWorks\SldWorks__NewDrawing2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
