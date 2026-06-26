---
title: "ModelDoc::EditConfiguration2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__EditConfiguration2.htm"
---

# ModelDoc::EditConfiguration2

This
method is obsolete and has been superseded by[ModelDoc2::EditConfiguration2](../ModelDoc2/ModelDoc2__EditConfiguration2.htm).

Description

This method edits the named configuration. Any component added to your
assembly inheritskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}these
settings if this configuration is the active configuration. To edit the
configuration of an individual component, see AssemblyDoc::CompConfigProperties.

Syntax (OLE Automation)

retval = ModelDoc.EditConfiguration2
( name, newname, comment, alternateName, suppressByDefault, hideByDefault,
minFeatureManager, inheritProperties, flags )

(Table)=========================================================

| Input: | (BSTR) name | Name of the configuration to edit |
| --- | --- | --- |
| Input: | (BSTR) newname | New name for the configuration, if desired, or a NULL string |
| Input: | (BSTR) comment | Comment string for documenting your configuration |
| Input: | (BSTR) alternateName | Alternate name for Bill of Materials |
| Input: | (VARIANT_BOOL) suppressByDefault | TRUE if you want newly added components to be suppressed, FALSE otherwise |
| Input: | (VARIANT_BOOL) hideByDefault | TRUE if you want newly added components to be hidden, FALSE otherwise |
| Input: | (VARIANT_BOOL) minFeatureManager | TRUE if you want newly added components to only display their component
name in the FeatureManager design tree. FALSE if you want newly added
components to display their name and each of their features in the FeatureManager
design tree |
| Input: | (VARIANT_BOOL) inheritProperties | TRUE if you want to inherit properties, FALSE if not |
| Input: | (ULONG) flags | Additional control |
| Return: | (VARIANT_BOOL) retval | TRUE if the configuration was edited successfully, FALSE if not |

Syntax (COM)

status = ModelDoc->EditConfiguration2
( name, newname, comment, alternateName, suppressByDefault, hideByDefault,
minFeatureManager, inheritProperties, flags, &retval )

(Table)=========================================================

| Input: | (BSTR) name | Name of the configuration to edit |
| --- | --- | --- |
| Input: | (BSTR) newname | New name for the configuration, if desired, or a NULL string |
| Input: | (BSTR) comment | Comment string for documenting your configuration |
| Input: | (BSTR) alternateName | Alternate name for Bill of Materials |
| Input: | (VARIANT_BOOL) suppressByDefault | TRUE if you want newly added components to be suppressed, FALSE otherwise |
| Input: | (VARIANT_BOOL) hideByDefault | TRUE if you want newly added components to be hidden, FALSE otherwise |
| Input: | (VARIANT_BOOL) minFeatureManager | TRUE if you want newly added components to only display their component
name in the FeatureManager design tree. FALSE if you want newly added
components to display their name and each of their features in the FeatureManager
design tree |
| Input: | (VARIANT_BOOL) inheritProperties | TRUE if you want to inherit properties, FALSE if not |
| Input: | (ULONG) flags | Additional control |
| Output: | (VARIANT_BOOL) retval | TRUE if the configuration was edited successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The flags argument allows additional control of the created configuration.
It can take the values from the ConfigurationFlags_e enumeration inswoptions.h. These are:

- CONFIG_USE_ALTERNATENAME - When set indicates
  that the alternateName specified is used in the Bill of Materials.
- CONFIG_DONT_SHOW_PARTS_IN_BOM - When set,
  specifies that sub-assemblies show in the Bill of Materials, otherwise
  the child components are listed in the Bill of Materials.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name=_Version value="65536" >
<param name=_ExtentX value="26" >
<param name=_ExtentY value="26" >
<param name=_StockProps value="13" >
<param name=ForeColor value="0" >
<param name=BackColor value="13160660" >
<param name=UseButton value="0" >
<param name=ControlLabel value="See Also" >
<param name=UseIcon value="0" >
<param name=Items value="ModelDoc_Object$$**$$ZModifyConfiguration$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__EditConfiguration2.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan
