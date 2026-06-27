---
title: "Component::SetXform"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__SetXform.htm"
---

# Component::SetXform

This method is obsolete and has been superseded by[Component2::SetXform](../Component2/Component2__SetXform.htm).

Description

This method sets the component transform.

Syntax (OLE Automation)

retval
= Component.SetXform ( xformIn)

(Table)=========================================================

| Input: | (VARIANT)
xformIn | SafeArray
of 16 doubles; the first 9 elements of a standard 3x3 rotation matrix,
the next 3 define translation, the next 1 is scaling, and the last 3 elements
are unused Specify
the transform in relation to the root component |
| --- | --- | --- |
| Return: | (BOOL)
retval | Not
used |

Syntax (COM)

status
= Component->ISetXform ( xformIn, retval )

(Table)=========================================================

| Input: | (double*)
xformIn | SafeArray
of 16 doubles; the first 9 elements of a standard 3x3 rotation matrix,
the next 3 define translation, the next 1 is scaling, and the last 3 elements
are unused Specify
the transform in relation to the root component |
| --- | --- | --- |
| Output: | (VARIANT_BOOL)
retval | Not used |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

The transform must be specified in relation to the root component (see
Configuration::GetRootComponent). This method does not currently support
the ability to set the transform of a component within a subassembly.
To do this, you need to open the subassembly document and get the desired
component in the context of the subassembly document.

To rebuild the model after transforming a component, you can call ModelDoc2::Rebuild
with the swUpdateMates argument. This is faster than using AssemblyDoc::EditRebuild
to rebuild the geometry for the model.

Be aware SetXform allows you to violate existing mate relationships.
If you place a component at an invalid location based on the mate definitions,
then the ModelDoc2::Rebuild method recalculates any existing mate relationships
and moves your components to the closest valid location.

When you change a component transform, you can use AssemblyDoc::UpdateBox
to avoid clipping in shaded display mode.

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
<param name=Items value="Component_Object$$**$$ZModifyComponent$$**$$ZGetInfoComponent$$**$$ZXform$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="C:\Home\Oneill\Component\Component__SetXform.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name=_Version value="65536" >
<param name=_ExtentX value="1217" >
<param name=_ExtentY value="556" >
<param name=_StockProps value="13" >
<param name=ForeColor value="0" >
<param name=BackColor value="12632256" >
<param name=UseButton value="0" >
<param name=ControlLabel value="See Also" >
<param name=UseIcon value="0" >
<param name=Items value="AddComponent_Example$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="C:\Home\Oneill\Component\Component__SetXform.htm" >
<param name=_ID value="RelatedTopic1" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan
