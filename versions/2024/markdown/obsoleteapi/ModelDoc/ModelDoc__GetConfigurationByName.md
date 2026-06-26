---
title: "ModelDoc::GetConfigurationByName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetConfigurationByName.htm"
---

# ModelDoc::GetConfigurationByName

This
method is obsolete and has been superseded by[ModelDoc2::GetConfigurationByName](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetConfigurationByName.htm).

Description

This function returns the Configuration object
based on the specified configuration name.

Syntax (OLE Automation)

retval = ModelDoc.GetConfigurationByName ( name )

(Table)=========================================================

| Input: | (BSTR) name | Name of the configuration |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the specified Configuration
object; this value is NULL if the operation fails |

Syntax (COM)

status = ModelDoc->IGetConfigurationByName ( name,
&retval )

(Table)=========================================================

| Input: | (BSTR) name | Name of the configuration |
| --- | --- | --- |
| Output: | (LPCONFIGURATION) retval | Pointer to the specified Configuration object;
this value is NULL if the operation fails |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If the specified configuration has not been activated,
then certain data may be unavailable. For example, attempting to traverse
assembly components for a configuration that has not been activated results
in a NULL root component being returned from Configuration::GetRootComponent.
However, the Configuration object returned is useful for obtaining data
that is stored with the Configuration object, such as, the AlternateName
value. The specified configuration does not have to be activated to obtain
this type of stored information.

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
<param name="Items" value="ModelDoc_Object$$**$$ZGetConfiguration$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__GetConfigurationByName.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
