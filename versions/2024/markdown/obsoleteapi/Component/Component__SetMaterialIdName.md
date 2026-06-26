---
title: "Component::SetMaterialIdName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__SetMaterialIdName.htm"
---

# Component::SetMaterialIdName

This method is obsolete and has been superseded by[Component2::SetMaterialIdName](sldworksAPI.chm::/Component2/Component2__SetMaterialIdName.htm).

Description

This method sets the material ID for this component.

Syntax (OLE Automation)

retval
= Component.SetMaterialIdName ( name )

(Table)=========================================================

| Input: | (BSTR)
name | Material
ID name for this component |
| --- | --- | --- |
| Return: | (BOOL)
retval | TRUE
if the material ID name was set successfully, FALSE if it was not |

Syntax (COM)

status
= Component->SetMaterialIdName ( name, &retval )

(Table)=========================================================

| Input: | (BSTR)
name | Material
ID name for this component |
| --- | --- | --- |
| Output: | (VARIANT_BOOL)
retval | TRUE
if the material ID name was set successfully, FALSE if it was not |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

This value is not visible to the user.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Component_Object$$**$$ZGetNames$$**$$ZModifyNames$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\Component\Component__SetMaterialIdName.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
