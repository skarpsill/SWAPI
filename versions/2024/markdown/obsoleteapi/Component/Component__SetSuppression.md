---
title: "Component::SetSuppression"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__SetSuppression.htm"
---

# Component::SetSuppression

This
method is obsolete and has been superseded by[Component2::SetSuppression](../Component2/Component2__SetSuppression.htm).

Description

This method controls the suppression state of this component.

Syntax (OLE Automation)

retval = Component.SetSuppression(
Suppression )

(Table)=========================================================

| Input: | (long) Suppression | Suppression state of this component instance as defined in swComponentSuppressionState_e |
| --- | --- | --- |
| Return: | (long) retval | Error code as defined in swSuppressionError_e |

Syntax (COM)

status = Component->SetSuppression(
Suppression, &retval )

(Table)=========================================================

| Input: | (long) Suppression | Suppression state of this component instance as defined in swComponentSuppressionState_e |
| --- | --- | --- |
| Output: | (long) retval | Error code as defined in swSuppressionError_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You cannot set a component to lightweight (for example, Suppression
= swComponentLightweight is not valid).

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
<param name="Items" value="Component_Object$$**$$ZGetInfoComponent$$**$$ZModifyComponent$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\Component\Component__SetSuppression.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
