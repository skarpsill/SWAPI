---
title: "ModelDoc::GetConfigurationNames"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetConfigurationNames.htm"
---

# ModelDoc::GetConfigurationNames

This
method is obsolete and has been superseded by[ModelDoc2::GetConfigurationNames](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetConfigurationNames.htm).

Description

This method returns a list of configuration names existing in this document.

Syntax (OLE Automation)

retval = ModelDoc.GetConfigurationNames(
)

(Table)=========================================================

| Return: | (VARIANT) retval | VARIANT of type SafeArray of the names of the configurations in this
part |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetConfigurationNames(
&configCount, configList )

(Table)=========================================================

| In/Out: | (long) configCount | Number of configurations in this part |
| --- | --- | --- |
| Output: | (BSTR) configList | Array of the names of the configurations in this part of size configCount |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ModelDoc::GetConfigurationCount
before calling this method.

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
<param name="Items" value="ModelDoc_Object$$**$$ZConfigurations$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__GetConfigurationNames.htm" >
<param name="_ID" value="RelatedTopic0" >
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
<param name="Items" value="ZExample_Get_List_Of_Configurations_Example_VB$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__GetConfigurationNames.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
