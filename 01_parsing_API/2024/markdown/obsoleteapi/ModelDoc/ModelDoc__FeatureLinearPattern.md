---
title: "ModelDoc::FeatureLinearPattern"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FeatureLinearPattern.htm"
---

# ModelDoc::FeatureLinearPattern

This
method is obsolete and has been superseded by[ModelDoc2::FeatureLinearPattern](../ModelDoc2/ModelDoc2__FeatureLinearPattern.htm).

Description

This method creates a linear pattern of the selected feature.

Syntax (OLE Automation)

void ModelDoc.FeatureLinearPattern
( num1, spacing1, num2, spacing2, flipDir1, flipDir2, dName1, dName2)

(Table)=========================================================

| Input: | (long) num1 | Number of copies in first direction, including original |
| --- | --- | --- |
| Input: | (double) spacing1 | Spacing in meters |
| Input: | (long) num2 | Number of copies in second direction, including original |
| Input: | (double) spacing2 | Spacing in meters |
| Input: | (BOOL) flipDir1 | TRUE for other way for first direction |
| Input: | (BOOL) flipDir2 | TRUE for other way for second direction |
| Input: | (BSTR) dName1 | Name of dimension defining the first direction of the pattern |
| Input: | (BSTR) dName2 | Name of dimension defining the second direction of the pattern |

Syntax (COM)

status = ModelDoc->FeatureLinearPattern
( num1, spacing1, num2, spacing2, flipDir1, flipDir2, dName1, dName2 )

(Table)=========================================================

| Input: | (long) num1 | Number of copies in first direction, including original |
| --- | --- | --- |
| Input: | (double) spacing1 | Spacing in meters |
| Input: | (long) num2 | Number of copies in second direction, including original |
| Input: | (double) spacing2 | Spacing in meters |
| Input: | (VARIANT_BOOL) flipDir1 | TRUE for other way for first direction |
| Input: | (VARIANT_BOOL) flipDir2 | TRUE for other way for second direction |
| Input: | (BSTR) dName1 | Name of dimension defining the first direction of the pattern |
| Input: | (BSTR) dName2 | Name of dimension defining the second direction of the pattern |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method requires ordered selection of the features.
Use ModelDoc::SelectByMark 1 and 2 for the directions and ModelDoc::SelectByMark 4 for the features to be patterned.

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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="AssemblyDoc::InsertDerivedPattern$$**$$ModelDoc::FeatureCirPattern$$**$$ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__FeatureLinearPattern.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
