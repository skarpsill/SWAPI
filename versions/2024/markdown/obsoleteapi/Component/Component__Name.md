---
title: "Component::Name"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__Name.htm"
---

# Component::Name

(Generated Script Links)========================================

(Generated Code)================================================

(WARNING: DO NOT EDIT OR DELETE THIS SECTION!)==================

begin!kadov{{===================================================

}}end!kadov=====================================================

(==============================================================)

This
property is obsolete and has been superseded by[Component::Name2](Component__Name2.htm).

Description

This property gets the component name.

Syntax
(OLE Automation)

Name
= Component.Name (VB Get property)

Name
= Component.GetName ( ) (C++ Get property)

(Table)=========================================================

| Property: | (BSTR)
Name | Name
of this component instance |
| --- | --- | --- |

Syntax
(COM)

status = Component->get_Name( &Name)

(Table)=========================================================

| Property: | (BSTR) Name | Name of this component instance |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This name of the component appears in the FeatureManager design tree
and is not necessarily the same as the name of the underlying part or
assembly file.

This property returns a name that includes an instance number. For example:

Part1-1

indicates that this is the first instance of the Part1 Component2. If
you are examining a component that is within a subassembly, then this
property returns a name that includes the full hierarchical path of component
names. For example:

subAssem1-2/Part1-1

indicates that this component (Part1) is the first instance within the
subAssem1 Component2. It also shows that this is the second instance of
subAssem1 .

As a side note, there is aUser Option,External Referencesetting that
allows or prohibits changes to this name. This setting affects only interactive
user operations.

If you are setting the name of a component,
remember that some special charactersbegin!kadov{{}}end!kadovare reserved by SolidWorks.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name=_Version value="65536" >
<param name=_ExtentX value="1323" >
<param name=_ExtentY value="556" >
<param name=_StockProps value="13" >
<param name=ForeColor value="0" >
<param name=BackColor value="12632256" >
<param name=UseButton value="0" >
<param name=ControlLabel value="See Also" >
<param name=UseIcon value="0" >
<param name=Items value="Component_Object$$**$$ZGetInfoComponent$$**$$ZModifyComponent$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="C:\Home\Oneill\Component\Component__Name.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan
