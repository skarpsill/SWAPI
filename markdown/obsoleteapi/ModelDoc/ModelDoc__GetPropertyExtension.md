---
title: "ModelDoc::GetPropertyExtension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetPropertyExtension.htm"
---

# ModelDoc::GetPropertyExtension

This
method is obsolete and has been superseded by[ModelDoc2::GetPropertyExtension](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetPropertyExtension.htm).

Description

This method retrieves a float, string, or integer value from a document.
The VARIANT type returned is based on the how the data was placed on the
part. See ModelDoc::AddPropertyExtension for details.

Syntax (OLE Automation)

retval = ModelDoc.GetPropertyExtension
( Id)

(Table)=========================================================

| Input: | (long) Id | Unique identifier for the desired property extension |
| --- | --- | --- |
| Return: | (VARIANT) retval | Value that was stored using ModelDoc::AddPropertyExtension |

Syntax (COM)

status = ModelDoc->GetPropertyExtension
( Id, &retval )

(Table)=========================================================

| Input: | (long) Id | Unique identifier for the desired property extension |
| --- | --- | --- |
| Output: | (VARIANT) retval | Value that was stored using ModelDoc::AddPropertyExtension |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

It is recommended that you use the Attribute, AttributeDef, and Parameter
classes instead of this method. These three classes provide more flexibility.

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
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__GetPropertyExtension.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
