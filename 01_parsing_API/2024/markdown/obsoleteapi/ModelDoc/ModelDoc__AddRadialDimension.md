---
title: "ModelDoc::AddRadialDimension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AddRadialDimension.htm"
---

# ModelDoc::AddRadialDimension

This
method is now obsolete and has been superseded by[ModelDoc::AddRadialDimension2](ModelDoc__AddRadialDimension2.htm).

Description

This method adds a radial dimension at the specified location for the
selected item.

Syntax (OLE Automation)

retval = ModelDoc.AddRadialDimension
( x, y, z)

(Table)=========================================================

| Input: | (double) x | X location for the dimension |
| --- | --- | --- |
| Input: | (double) y | Y location for the dimension |
| Input: | (double) z | Z location for the dimension |
| Return: | (BOOL) retval | TRUE if the dimension was added successfully, FALSE otherwise |

Syntax (COM)

status = ModelDoc->AddRadialDimension
( x, y, z, &retval )

(Table)=========================================================

| Input: | (double) x | X location for the dimension |
| --- | --- | --- |
| Input: | (double) y | Y location for the dimension |
| Input: | (double) z | Z location for the dimension |
| Output: | (VARIANT_BOOL) retval | TRUE if the dimension was added successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name=_Version value="65536" >
<param name=_ExtentX value="1323" >
<param name=_ExtentY value="556" >
<param name=_StockProps value="13" >
<param name=ForeColor value="0" >
<param name=BackColor value="13160660" >
<param name=UseButton value="0" >
<param name=ControlLabel value="See Also" >
<param name=UseIcon value="0" >
<param name=Items value="ModelDoc_Object$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="C:\Home\Oneill\ModelDoc\ModelDoc__AddRadialDimension.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan
