---
title: "ModelDoc2::GetCustomInfoValue"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__GetCustomInfoValue.htm"
---

# ModelDoc2::GetCustomInfoValue

This
method is obsolete and has been superseded by ModelDocExtension::CustomPropertyManager .

Description

This method gets the resolved custom information
value.

Syntax (OLE Automation)

retval = ModelDoc2.GetCustomInfoValue ( configuration,
FieldName )

(Table)=========================================================

| Input: | (BSTR) configuration | Name of the configuration (see Remarks ) |
| --- | --- | --- |
| Input: | (BSTR) FieldName | Name of the custom information |
| Return: | (BSTR) retval | Resolved value |

Syntax (COM)

status = ModelDoc2->GetCustomInfoValue ( configuration,
FieldName, &retval )

Parameters Table Start

(Table)=========================================================

| Input: | (BSTR) configuration | Name of the configuration (see Remarks ) |
| --- | --- | --- |
| Input: | (BSTR) FieldName | Name of the custom information |
| Output: | (BSTR) retval | Resolved value |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If a custom information is associated with dimension
name,

ModelDoc2.AddCustominfo2("Test","myDim",
swCustomInfoText, "D1@Base-Extrude")

then

ModelDoc2.GetCustomInfoValue("Test","myDim")

returns the value of the dimension.

If the specified configuration is not the active
configuration, the specified configuration becomes the active configuration
and is assigned the custom information value. Then, the original configuration
then becomes the active configuration.

To get a document-level property, pass an empty
stringkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}("")
to the configuration argument.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDoc2\ModelDoc2__GetCustomInfoValue.htm" >
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
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc2_Object$$**$$ModelDoc2CustomProperty$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDoc2\ModelDoc2__GetCustomInfoValue.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic5
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="EXListCustomProperties$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDoc2\ModelDoc2__GetCustomInfoValue.htm" >
<param name="_ID" value="RelatedTopic5" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
