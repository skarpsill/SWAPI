---
title: "ModelDoc::AddConfiguration"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__AddConfiguration.htm"
---

# ModelDoc::AddConfiguration

This
method is obsolete and has been superseded by[ModelDoc::AddConfiguration2](ModelDoc__AddConfiguration2.htm).

Description

This method creates a new configuration. Any component added to your
assembly inheritskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}these
settings if this configuration is the active configuration.

Syntax (OLE Automation)

void ModelDoc.AddConfiguration
( name, comment, alternateName, suppressByDefault, hideByDefault, minFeatureManager,
inheritProperties, flags)

(Table)=========================================================

| Input: | (BSTR) name | Name to be given to this new configuration |
| --- | --- | --- |
| Input: | (BSTR) comment | Comment string for documenting your configuration |
| Input: | (BSTR) alternateName | Alternate name for Bill of Materials |
| Input: | (BOOL) suppressByDefault | TRUE if you want newly added components to be suppressed, FALSE otherwise |
| Input: | (BOOL) hideByDefault | TRUE if you want newly added components to be hidden, FALSE otherwise |
| Input: | (BOOL) minFeatureManager | TRUE if you want newly added components to only display their component
name in the FeatureManager design tree, FALSE
if you want newly added components to display their name and each of their
features in the FeatureManager design tree |
| Input: | (BOOL) inheritProperties | TRUE if you want to inherit properties |
| Input: | (ULONG) flags | Additional control |

Syntax (COM)

status = ModelDoc->AddConfiguration
( name, comment, alternateName, suppressByDefault, hideByDefault, minFeatureManager,
inheritProperties, flags )

(Table)=========================================================

| Input: | (BSTR) name | Name to be given to this new configuration |
| --- | --- | --- |
| Input: | (BSTR) comment | Comment string for documenting your configuration |
| Input: | (BSTR) alternateName | Alternate name for Bill of Materials |
| Input: | (VARIANT_BOOL) suppressByDefault | TRUE if you want newly added components to be suppressed, FALSE otherwise |
| Input: | (VARIANT_BOOL) hideByDefault | TRUE if you want newly added components to be hidden, FALSE otherwise |
| Input: | (VARIANT_BOOL) minFeatureManager | TRUE if you want newly added components to only display their component
name in the FeatureManager design tree, FALSE
if you want newly added components to display their name and each of their
features in the FeatureManager design tree. |
| Input: | (VARIANT_BOOL) inheritProperties | TRUE if you want to inherit properties |
| Input: | (ULONG) flags | Additional control |
| Return: | (HRESULT) status | S_OK if the configuration was added successfully, S_FALSE otherwise |

Remarks

The Flags argument allows additional control of the created configuration.
It can take the values from the ConfigurationFlags_e enumeration. These
are:

- CONFIG_USE_ALTERNATENAME - When set, indicates
  that the alternateName specified is used in the Bill of Materials.
- CONFIG_DONT_SHOW_PARTS_IN_BOM - When set,
  specifies that sub-assemblies show in the Bill of Materials, otherwise
  the child components are listed in the Bill of Materials.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name=_Version value="65536" >
<param name=_ExtentX value="1323" >
<param name=_ExtentY value="556" >
<param name=_StockProps value="13" >
<param name=ForeColor value="0" >
<param name=BackColor value="13160660" >
<param name=UseButton value="0" >
<param name=ControlLabel value="See Also" >
<param name=UseIcon value="0" >
<param name=Items value="ModelDoc_Object$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="C:\Home\Oneill\ModelDoc\ModelDoc__AddConfiguration.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan
