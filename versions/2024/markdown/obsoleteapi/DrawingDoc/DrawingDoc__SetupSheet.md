---
title: "DrawingDoc::SetupSheet"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__SetupSheet.htm"
---

# DrawingDoc::SetupSheet

This method is obsolete and has been superseded
by[DrawingDoc::SetupSheet2](DrawingDoc__SetupSheet2.htm).

Description

This method changes the settings for the current sheet on this drawing.

Syntax (OLE Automation)

void DrawingDoc.SetupSheet ( name,
paperSize, templateIn, scale1, scale2)

(Table)=========================================================

| Input: | (BSTR) name | Name for the sheet |
| --- | --- | --- |
| Input: | (short) paperSize | Size of paper as defined in swDwgPaperSizes_e |
| Input: | (short) templateIn | Template index as defined in swDwgTemplates_e |
| Input: | (double) scale1 | Scale numerator |
| Input: | (double) scale2 | Scale denominator |

Syntax
(COM)

status = DrawingDoc->SetupSheet
( name, paperSize, templateIn, scale1, scale2 )

(Table)=========================================================

| Input: | (BSTR) name | Name for the sheet |
| --- | --- | --- |
| Input: | (short) paperSize | Size of paper as defined in swDwgPaperSizes_e |
| Input: | (short) templateIn | Template index as defined in swDwgTemplates_e |
| Input: | (double) scale1 | Scale numerator |
| Input: | (double) scale2 | Scale denominator |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can also use Sheet::SetProperties, Sheet::SetName, and Sheet::SetTemplateName.

This method does not support paperSize = swDwgPapersUserDefined or templateIn
= swDwgTemplateCustom. See DrawingDoc::SetupSheet2.

The templateIn argument overrides the paperSize argument if they do
not match.

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
<param name=Items value="DrawingDoc_Object$$**$$ZModifySheet$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="D:\sw2003\DrawingDoc\DrawingDoc__SetupSheet.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan
