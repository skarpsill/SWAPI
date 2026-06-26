---
title: "ModelDoc::AddRelation"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AddRelation.htm"
---

# ModelDoc::AddRelation

This
method is obsolete and has been superseded by[ModelDoc2::AddRelation](../ModelDoc2/ModelDoc2__AddRelation.htm).

Description

This method adds a new relation. For example, to set the D2 dimension
to be twice the value of the D1 dimension, you could use this method.

Syntax (OLE Automation)

void ModelDoc.AddRelation ( relStr)

(Table)=========================================================

| Input: | (BSTR) relStr | String containing the relationship to add |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->AddRelation (
relStr )

(Table)=========================================================

| Input: | (BSTR) relStr | String containing the relationship to add |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method adds a new relation. For example, to set the D2 dimension
to be twice the value of the D1 dimension, you could specify this value
for relStr:

"""D2@Sketch1""
= (""D1@Sketch1"" * 2)"

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
<param name=Items value="ModelDoc_Object$$**$$ZCreateRelation$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="C:\Home\Oneill\ModelDoc\ModelDoc__AddRelation.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan
