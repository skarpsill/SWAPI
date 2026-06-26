---
title: "ModelDoc2::ListExternalFileReferencesCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__ListExternalFileReferencesCount.htm"
---

# ModelDoc2::ListExternalFileReferencesCount

This method is obsolete and has been superseded
by[ModelDoc2::ListExternalFileReferencesCount2](ModelDoc2__ListExternalFileReferencesCount2.htm).

Description

This method gets the number of external file references
on this model.

Syntax (OLE Automation)

retval = ModelDoc2.ListExternalFileReferencesCount
( useSearchRules )

(Table)=========================================================

| Input: | (BOOL) useSearchRules | TRUE uses the search rules,
FALSE does not |
| --- | --- | --- |
| Return: | (long) retval | Number of external references |

Syntax (COM)

status = ModelDoc2->ListExternalFileReferencesCount
( useSearchRules, &retval )

(Table)=========================================================

| Input: | (VARIANT_BOOL) useSearchRules | TRUE uses the search rules,
FALSE does not |
| --- | --- | --- |
| Output: | (long) retval | Number of external references |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use this method with ModelDoc2::ListExternalFileReferences
to determine the array size required.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc2\ModelDoc2__ListExternalFileReferencesCount.htm" >
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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc2\ModelDoc2__ListExternalFileReferencesCount.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
