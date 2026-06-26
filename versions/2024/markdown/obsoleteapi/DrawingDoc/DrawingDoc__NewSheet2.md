---
title: "DrawingDoc::NewSheet2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__NewSheet2.htm"
---

# DrawingDoc::NewSheet2

This method is obsolete and has been superseded
byDrawingDoc::NewSheet3.

Description

This method creates a new drawing sheet.

Syntax (OLE Automation)

retval = DrawingDoc.NewSheet2 ( name, paperSize,
templateIn, scale1, scale2, firstAngle, templateName, width, height)

(Table)=========================================================

| Input: | (BSTR) name | Name to be given to the new sheet |
| --- | --- | --- |
| Input: | (short) paperSize | Size of paper as defined in swDwgPaperSizes_e |
| Input: | (short) templateIn | Template index as defined in swDwgTemplates_e |
| Input: | (double) scale1 | Scale numerator |
| Input: | (double) scale2 | Scale denominator |
| Input: | (BOOL) firstAngle | TRUE for first angle projection, FALSE otherwise |
| Input: | (BSTR) templateName | Name of custom template with full directory path if templateIn = swDwgTemplateCustom |
| Input: | (double) width | Custom paper width if paperSize = swDwgPapersUserDefined |
| Input: | (double) height | Custom paper height if paperSize = swDwgPapersUserDefined |
| Return: | (BOOL) retval | TRUE if sheet creation was successful, FALSE if not |

Syntax (COM)

status = DrawingDoc->NewSheet2 ( name, paperSize,
templateIn, scale1, scale2, firstAngle, templateName, width, height, &retval
)

(Table)=========================================================

| Input: | (BSTR) name | Name to be given to the new sheet |
| --- | --- | --- |
| Input: | (short) paperSize | Size of paper as defined in swDwgPaperSizes_e |
| Input: | (short) templateIn | Template index as defined in swDwgTemplates_e |
| Input: | (double) scale1 | Scale numerator |
| Input: | (double) scale2 | Scale denominator |
| Input: | (VARIANT_BOOL) firstAngle | TRUE for first angle projection, FALSE otherwise |
| Input: | (BSTR) templateName | Name of custom template with full directory path if templateIn = swDwgTemplateCustom |
| Input: | (double) width | Custom paper width if paperSize = swDwgPapersUserDefined |
| Input: | (double) height | Custom paper height if paperSize = swDwgPapersUserDefined |
| Output: | (VARIANT_BOOL) retval | TRUE if sheet creation was successful, FALSE if not |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The templatetIn argument overrides the paperSize
argument if they do not match.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="DrawingDoc_Object$$**$$ZCreateSheet$$**$$ZModifySheet$$**$$SldWorks::NewDrawing2$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\sw2003\DrawingDoc\DrawingDoc__NewSheet2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
