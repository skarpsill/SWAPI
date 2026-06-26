---
title: "DrawingDoc::SetupSheet2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__SetupSheet2.htm"
---

# DrawingDoc::SetupSheet2

This method is obsolete and has been superseded
by[DrawingDoc::SetupSheet3](DrawingDoc__SetupSheet3.htm).

Description

This method changes the settings for the current sheet on this drawing
document.

Syntax (OLE Automation)

void DrawingDoc.SetupSheet2 ( name,
paperSize, templateIn, scale1, scale2, skPointsFlag)

(Table)=========================================================

| Input: | (BSTR) name | Name for the sheet |
| --- | --- | --- |
| Input: | (short) paperSize | Size of paper as defined in swDwgPaperSizes_e |
| Input: | (short) templateIn | Template index as defined in swDwgTemplates_e |
| Input: | (double) scale1 | Scale numerator |
| Input: | (double) scale2 | Scale denominator |
| Input: | (long) skPointsFlag | Display of user points as defined in swSkInternalPntOpts_e |

Syntax
(COM)

status = DrawingDoc->SetupSheet2
( name, paperSize, templateIn, scale1, scale2, skPointsFlag )

(Table)=========================================================

| Input: | (BSTR) name | Name for the sheet |
| --- | --- | --- |
| Input: | (short) paperSize | Size of paper as defined in swDwgPaperSizes_e |
| Input: | (short) templateIn | Template index as defined in swDwgTemplates_e |
| Input: | (double) scale1 | Scale numerator |
| Input: | (double) scale2 | Scale denominator |
| Input: | (long) skPointsFlag | Display of user points as defined in swSkInternalPntOpts_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can also use Sheet::SetProperties,
Sheet::SetName and Sheet::SetTemplateName.

The templateIn value overrides paperSize
if they do not match.

The skPointsFlag is not available through
the SolidWorks user interface on a per-document level. This overrides
the global user option setting for the display of entity points.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name=_Version value="65536" >
<param name=_ExtentX value="1217" >
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
<param name=_CURRENTFILEPATH value="D:\sw2003\DrawingDoc\DrawingDoc__SetupSheet2.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan
