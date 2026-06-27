---
title: "Component::IsHidden"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__IsHidden.htm"
---

# Component::IsHidden

This method is obsolete and has been superseded by[Component2::IsHidden](sldworksAPI.chm::/Component2/Component2__IsHidden.htm).

Description

This method determines if this component is hidden or suppressed.

Syntax (OLE Automation)

retval
= Component.IsHidden ( considerSuppressed )

(Table)=========================================================

| Input: | (BOOL)
considerSuppressed | Controls
whether suppressed components are considered hidden |
| --- | --- | --- |
| Return: | (BOOL)
retval | TRUE
or FALSE (see Remarks ) |

Syntax (COM)

status
= Component->IsHidden ( considerSuppressed, &retval )

(Table)=========================================================

| Input: | (VARIANT_BOOL)
considerSuppressed | Controls
whether suppressed components are considered hidden |
| --- | --- | --- |
| Output: | (VARIANT_BOOL)
retval | TRUE
or FALSE (see Remarks ) |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

The state of this component can vary based on the active configuration.

(Table)=========================================================

| ConsiderSuppressed | Component | Component | IsHidden |
| --- | --- | --- | --- |
| True | Hidden | Unsuppressed | True |
| True | Hidden | Suppressed | True |
| True | Shown | Unsuppressed | True |
| True | Shown | Suppressed | False |
| False | Hidden | Unsuppressed | True |
| False | Hidden | Suppressed | True |
| False | Shown | Unsuppressed | False |
| False | Shown | Suppressed | False |

NOTE:For lightweight components, Componet::IsHidden returns TRUE if considerSuppressed
is TRUE.

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
<param name="Items" value="Component_Object$$**$$ZGetObjectDisplay$$**$$ZModifyObjectDisplay$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\Component\Component__IsHidden.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
