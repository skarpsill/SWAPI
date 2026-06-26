---
title: "ModelDoc::GetCustomInfoNames"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetCustomInfoNames.htm"
---

# ModelDoc::GetCustomInfoNames

This
method is obsolete and has been superseded by[ModelDoc2::GetCustomInfoNames](../ModelDoc2/ModelDoc2__IGetCustomInfoNames.htm).

Description

This method returns a list of strings of the
names of the custom properties that have been defined in this document.

Syntax (OLE Automation)

retval = ModelDoc. GetCustomInfoNames(
)

(Table)=========================================================

| Return: | (VARIANT) retval | SafeArray of the custom property names |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetCustomInfoNames(
retval )

(Table)=========================================================

| Output: | (BSTR*) retval | Array of the custom property names |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To get the size of array needed by the COM version of this method, call
ModelDoc::GetCustomInfoCount.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__GetCustomInfoNames.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
