---
title: "Component::GetXform"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetXform.htm"
---

# Component::GetXform

This method is obsolete and has been superseded by[Component2::GetXform](../Component2/Component2__GetXform.htm).

Description

This method gets the transform of this Component object. The transform
is returned in relation of the root component (see Configuration::GetRootComponent).

Syntax (OLE Automation)

retval
= Component.GetXform ()

(Table)=========================================================

| Return: | (VARIANT)
retval | VARIANT
containing a SafeArray of 16 doubles |
| --- | --- | --- |

Syntax (COM)

status
= Component->IGetXform ( retval )

(Table)=========================================================

| Output: | (double*)
retval | Pointer
to an array of 16 doubles |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

If this configuration is exploded, then this method returns an exploded
transform.

This method returns the transform as an array of 16 elements. The first
9 are elements of a standard 3x3 rotation matrix, the next 3 define translation,
the next 1 is scaling. The last 3 elements are unused.

The transform is returned in relation to
the root component.

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
<param name=Items value="Component_Object$$**$$Component_SetXform$$**$$ZGetInfoComponent$$**$$ZXform$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="C:\Home\Oneill\Component\Component__GetXform.htm" >
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
<param name=_CURRENTFILEPATH value="C:\Home\Oneill\Component\Component__GetXform.htm" >
<param name=_ID value="RelatedTopic1" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan
