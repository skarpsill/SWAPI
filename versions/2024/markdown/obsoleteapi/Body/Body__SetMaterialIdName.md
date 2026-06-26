---
title: "Body::SetMaterialIdName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__SetMaterialIdName.htm"
---

# Body::SetMaterialIdName

This method is obsolete and has been superseded by[Body2::SetMaterialIdName](../Body2/Body2__SetMaterialIdName.htm).

Description

This method sets the material ID for this body. This value is not visible
to the user.

Syntax (OLE Automation)

retval = Body.SetMaterialIdName ( name)

(Table)=========================================================

| Input: | (BSTR) name | Material's ID name for this body |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the material ID name is set successfully, FALSE if not |

Syntax
(COM)

status = Body->SetMaterialIdName
( name, &retval )

(Table)=========================================================

| Input: | (BSTR) name | Material's ID name for this body |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the material ID name is set successfully, FALSE if not |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

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
<param name=Items value="Body_Object$$**$$ZGetNames$$**$$ZModifyNames$$**$$ZGetSetMaterialIdName$$**$$" >
<param name=Image value="" >
<param name=FontInfo value="MS Sans Serif,8,0,," >
<param name=_CURRENTFILEPATH value="C:\Home\Oneill\Body\Body__SetMaterialIdName.htm" >
<param name=_ID value="RelatedTopic0" >
<param name=DialogDisplay value="0" >
<param name=Frame value="" >
<param name=Window value="" >
<param name=ChmFile value="" >
<param name=DisableJump value="0" >
</object>Metadata type="DesignerControl" endspan
