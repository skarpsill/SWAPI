---
title: "ModelDoc::AddCustomInfo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AddCustomInfo.htm"
---

# ModelDoc::AddCustomInfo

This
method is obsolete and has been superseded by[ModelDoc::AddCustomInfo2](ModelDoc__AddCustomInfo2.htm).

Description

This method adds a custom property field to the document.

Syntax (OLE Automation)

retval = ModelDoc.AddCustomInfo(
FieldName, FieldType, FieldValue )

(Table)=========================================================

| Input: | (BSTR)FieldName | Name of custom property |
| --- | --- | --- |
| Input: | (BSTR)FieldType | Type of custom property |
| Input: | (BSTR)FieldValue | Value of custom property |
| Return: | (BOOL)retval | TRUE if added |

Syntax (COM)

status = ModelDoc->AddCustomInfo(
FieldName, FieldType, FieldValue, &retval )

(Table)=========================================================

| Input: | (BSTR)FieldName | Name of custom property |
| --- | --- | --- |
| Input: | (BSTR)FieldType | Type of custom property |
| Input: | (BSTR)FieldValue | Value of custom property |
| Output: | (VARIANT_BOOL)retval | TRUE if added, FALSE if not |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The FieldTypeargument can be
one of these values:

- "Text"
- "Date"
- "Number"
- "Yes
  or no"

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__AddCustomInfo.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
