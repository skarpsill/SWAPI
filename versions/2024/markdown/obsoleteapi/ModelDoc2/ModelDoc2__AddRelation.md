---
title: "ModelDoc2::AddRelation"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__AddRelation.htm"
---

# ModelDoc2::AddRelation

This
method is obsolete and has been superseded by EquationMgr::Add .

Description

This method adds a new relation.

Syntax (OLE Automation)

void ModelDoc2.AddRelation ( relStr)

(Table)=========================================================

| Input: | (BSTR) relStr | String containing the relationship to add |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->AddRelation
( relStr )

(Table)=========================================================

| Input: | (BSTR) relStr | String containing the relationship to add |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method adds a new equation based on a relationship
between two items. For example, you could use the following relStr to
set the D2 dimension to twice the value of the D1 dimension:

"""D2@Sketch1""
= (""D1@Sketch1"" * 2)"

For information about adding constraints,
see ModelDoc2::SketchAddConstraints.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc2\ModelDoc2__AddRelation.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
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
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc2\ModelDoc2__AddRelation.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
