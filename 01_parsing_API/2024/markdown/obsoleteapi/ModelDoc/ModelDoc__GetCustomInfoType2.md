---
title: "ModelDoc::GetCustomInfoType2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetCustomInfoType2.htm"
---

# ModelDoc::GetCustomInfoType2

This
method is obsolete and has been superseded by[ModelDoc::GetCustomInfoType3](ModelDoc__GetCustomInfoType3.htm).

Description

This methodreturns
the type of a custom information field that has been defined for this
document.

Syntax (OLE Automation)

FieldType = ModelDoc.GetCustomInfoType2(
FieldName )

(Table)=========================================================

| Input: | (BSTR) FieldName | Name of custom property |
| --- | --- | --- |
| Return: | (long) FieldType | Type of custom property as defined in swCustomInfoType_e |

Syntax (COM)

status = ModelDoc->GetCustomInfoType2(
FieldName, &FieldType )

(Table)=========================================================

| Input: | (BSTR) FieldName | Name of custom property |
| --- | --- | --- |
| Output: | (long) FieldType | Type of custom property as defined in swCustomInfoType_e |
| Return: | (HRESULT) status | S_OK if successful |

RemarksMetadata type="DesignerControl" startspan
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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__GetCustomInfoType2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
