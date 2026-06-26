---
title: "ModelDoc::ListExternalFileReferencesCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__ListExternalFileReferencesCount.htm"
---

# ModelDoc::ListExternalFileReferencesCount

This
method is obsolete and has been superseded by[ModelDoc2::ListExternalFileReferencesCount](../ModelDoc2/ModelDoc2__ListExternalFileReferencesCount.htm).

Description

This method gets the number of external file
references on this model. Use this method with ModelDoc.ListExternalFileReferences
to determine the array size required.

Syntax (OLE Automation)

retval = ModelDoc.ListExternalFileReferencesCount
( useSearchRules )

(Table)=========================================================

| Input: | (BOOL) useSearchRules | TRUE uses the search rules, FALSE does not |
| --- | --- | --- |
| Return: | (long) retval | Number of external references |

Syntax (COM)

status = ModelDoc->ListExternalFileReferencesCount
( useSearchRules, &retval )

(Table)=========================================================

| Input: | (VARIANT_BOOL) useSearchRules | TRUE uses the search rules, FALSE does not |
| --- | --- | --- |
| Output: | (long) retval | Number of external references |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="16777215" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZReferences$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__ListExternalFileReferencesCount.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
