---
title: "DrawingDoc::NewSheet"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__NewSheet.htm"
---

# DrawingDoc::NewSheet

This method is obsolete and has been superseded
by[DrawingDoc::NewSheet2](DrawingDoc__NewSheet2.htm).

Description

This
method creates a new sheet for the selected drawing.

Syntax (OLE Automation)

void DrawingDoc.NewSheet ( name, paperSize,
templateIn, scale1, scale2)

(Table)=========================================================

| Input: | (BSTR) name | Name for the sheet |
| --- | --- | --- |
| Input: | (short) paperSize | Size of paper as defined in swDwgPaperSizes_e |
| Input: | (short) templateIn | Template index as defined in swDwgTemplates_e |
| Input: | (double) scale1 | Scale numerator |
| Input: | (double) scale2 | Scale denominator |

Syntax (COM)

status = DrawingDoc->NewSheet (
name, paperSize, templateIn, scale1, scale2 )

(Table)=========================================================

| Input: | (BSTR) name | Name for the sheet |
| --- | --- | --- |
| Input: | (short) paperSize | Size of paper as defined in swDwgPaperSizes_e |
| Input: | (short) templateIn | Template index as defined in swDwgTemplates_e |
| Input: | (double) scale1 | Scale numerator |
| Input: | (double) scale2 | Scale denominator |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method does not support paperSize = swDwgPapersUserDefined or templateIn
= swDwgTemplateCustom.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name=_Version value="65536" >
<param name=_ExtentX value="1323" >
<param name=_ExtentY value="556" >
<param name=_StockProps value="13" >
<param name=ForeColor value="0" >
<param name=BackColor value="12632256" >
<param name=UseButton value="0" >
<param name=ControlLabel value="See Also" >
<param name=UseIcon value="0" >
<param name=Items value="DrawingDoc_Object$$**$$ZCreateSheet$$**$$ZModifySheet$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="D:\sw2003\DrawingDoc\DrawingDoc__NewSheet.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan
