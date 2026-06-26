---
title: "Body2::AddPropertyExtension"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body2/Body2__AddPropertyExtension.htm"
---

# Body2::AddPropertyExtension

This method is obsolete and has been superseded
byBody2::AddPropertyExtension2.

Description

This method allows you to store a float, string, or integer value on
a body.

Syntax (OLE Automation)

retval = Body2.AddPropertyExtension
( PropertyExtension)

(Table)=========================================================

| Input: | (VARIANT) PropertyExtension | Value you wish to store |
| --- | --- | --- |
| Return: | (long) retval | Unique identifier returned to allow you to access the property extension
in the future using Body2::GetPropertyExtension |

Syntax (COM)

status = Body2->AddPropertyExtension
( PropertyExtension, &retval )

(Table)=========================================================

| Input: | (VARIANT) PropertyExtension | Value you want to store |
| --- | --- | --- |
| Output: | (long) retval | Unique identifier returned to allow you to access the property extension
in the future using Body2::GetPropertyExtension |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

To do this, you must first define the VARIANT type
(float, string, or integer), give your variable a value, and then call
this method to place the value on the body for future reference.

It is recommended that you use the Attribute, AttributeDef,
and Parameter classes instead of this method. These three classes are
newer and provide more flexibility.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
dtcid=2
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
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Body2\Body2__AddPropertyExtension.htm" >
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
dtcid=3
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
<param name="Items" value="Body2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Body2\Body2__AddPropertyExtension.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
