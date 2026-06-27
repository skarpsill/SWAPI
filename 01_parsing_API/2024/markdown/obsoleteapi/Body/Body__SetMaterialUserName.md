---
title: "Body::SetMaterialUserName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__SetMaterialUserName.htm"
---

# Body::SetMaterialUserName

This method is obsolete and has been superseded by[Body2::SetMaterialUserName](../Body2/Body2__SetMaterialUserName.htm).

Description

This method sets the material user name for this body. This material
name is visible to the user.

Syntax (OLE Automation)

retval = Body.SetMaterialUserName (
name)

(Table)=========================================================

| Input: | (BSTR) name | Material's user name property for this body |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the material user name was set successfully, FALSE if it was
not |

Syntax
(COM)

status = Body->SetMaterialUserName
( name, &retval )

(Table)=========================================================

| Input: | (BSTR) name | Material's user name property for this body |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the material user name was set successfully, FALSE if it was
not |
| Return: | (HRESULT)status | S_OK if successful |

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name=_Version value="65536" >
<param name=_ExtentX value="1217" >
<param name=_ExtentY value="556" >
<param name=_StockProps value="13" >
<param name=ForeColor value="0" >
<param name=BackColor value="12632256" >
<param name=UseButton value="0" >
<param name=ControlLabel value="See Also" >
<param name=UseIcon value="0" >
<param name=Items value="Body_Object$$**$$ZGetNames$$**$$ZModifyNames$$**$$ZGetSetMaterialUserName$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="C:\Home\Oneill\Body\Body__SetMaterialUserName.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan
