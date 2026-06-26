---
title: "ModelDoc::AddPropertyExtension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AddPropertyExtension.htm"
---

# ModelDoc::AddPropertyExtension

This
method is obsolete and has been superseded by[ModelDoc2::AddPropertyExtension.](sldworksAPI.chm::/ModelDoc2/ModelDoc2__AddPropertyExtension.htm)

Description

This method stores a float, string, or integer value with this document.
To do this, you must first define the VARIANT type (float, string, or
integer), give your variable a value, and then call this method to place
the value on the document for future reference.

Syntax (OLE Automation)

retval = ModelDoc.AddPropertyExtension
( PropertyExtension)

(Table)=========================================================

| Input: | (VARIANT) PropertyExtension | Value you wish to store with the SolidWorks document |
| --- | --- | --- |
| Return: | (long) retval | Unique identifier returned that allows access to this property extension
in the future |

Syntax (COM)

status = ModelDoc->AddPropertyExtension
( PropertyExtension, &retval )

(Table)=========================================================

| Input: | (VARIANT) PropertyExtension | Value you wish to store with the SolidWorks document |
| --- | --- | --- |
| Output: | (long) retval | Unique identifier returned that allows access to this property extension
in the future |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

It is recommended that you use the Attribute, AttributeDef, and Parameter
classes instead of this method. These three classes provide more flexibility.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__AddPropertyExtension.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
