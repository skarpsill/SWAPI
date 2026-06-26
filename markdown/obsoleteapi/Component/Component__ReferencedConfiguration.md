---
title: "Component::ReferencedConfiguration"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__ReferencedConfiguration.htm"
---

# Component::ReferencedConfiguration

This
property is obsolete and has been superseded by[Component2::ReferencedConfiguration](sldworksAPI.chm::/Component2/Component2__ReferencedConfiguration.htm).

Description

This property gets or sets the active configuration used by this component.

Syntax (OLE Automation)

ConfigName
= Component.ReferencedConfiguration (VB Get property)

Component.ReferencedConfiguration
= ConfigName (VB Set property)

ConfigName
= Component.GetReferencedConfiguration ( ) (C++ Get property)

Component.SetReferencedConfiguration
( ConfigName ) (C++ Set property)

(Table)=========================================================

| Property: | (BSTR)
ConfigName | Name
of the configuration for this component |
| --- | --- | --- |

Syntax (COM)

status
= Component->get_ReferencedConfiguration( &ConfigName)

status
= Component->put_ReferencedConfiguration ( ConfigName )

(Table)=========================================================

| Property: | (BSTR)
ConfigName | Name
of the configuration for this component |
| --- | --- | --- |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

After changing the referenced
configuration, call[AssemblyDoc::EditRebuild](../AssemblyDoc/AssemblyDoc__EditRebuild.htm)to display the changes.

When the configuration is changed, components might become suppressed
or unsuppressed. This invalidates the array previously returned by Component::GetChildren.
If an application calls this method while it is traversing an assembly,
the applications must stop the traversal and start it again using the
ModelDoc and active configuration of the assembly. The application should
also free the array previously returned by Component::GetChildren before
calling this method. To hold onto the component with the changed configuration,
you can make an extra call to AddRef() for that component before freeing
the array.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Component_Object$$**$$ZModifyConfiguration$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\Component\Component__ReferencedConfiguration.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
