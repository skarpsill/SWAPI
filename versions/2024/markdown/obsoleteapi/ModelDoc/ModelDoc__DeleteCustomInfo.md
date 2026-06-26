---
title: "ModelDoc::DeleteCustomInfo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__DeleteCustomInfo.htm"
---

# ModelDoc::DeleteCustomInfo

This method is obsolete
and has been superseded by[ModelDoc2::DeleteCustomInfo](../ModelDoc2/ModelDoc2__DeleteCustomInfo.htm).

Description

This method deletes a custom
property field that has been defined for the document.

Syntax (OLE Automation)

FieldType = ModelDoc.DeleteCustomInfo(
FieldName )

(Table)=========================================================

| Input: | (BSTR) FieldName | Name of custom property |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if deleted, FALSE if not |

Syntax (COM)

status = ModelDoc->DeleteCustomInfo(
FieldName, &retval)

(Table)=========================================================

| Input: | (BSTR) FieldName | Name of custom property |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if deleted, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZFileOperations$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__DeleteCustomInfo.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
