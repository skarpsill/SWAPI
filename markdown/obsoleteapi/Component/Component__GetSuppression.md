---
title: "Component::GetSuppression"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetSuppression.htm"
---

# Component::GetSuppression

This
method is obsolete and has been superseded by[Component2::GetSuppression](sldworksAPI.chm::/Component2/Component2__GetSuppression.htm).

Description

This method provides access to the suppression state of this component.

Syntax (OLE Automation)

Suppression= Component.GetSuppression

(Table)=========================================================

| Return: | (long) Suppression | Suppression state of this component instance as defined in swComponentSuppressionState_e |
| --- | --- | --- |

Syntax (COM)

status = Component->GetSuppression(
&Suppression )

(Table)=========================================================

| Output: | (long) Suppression | Suppression state of this component instance as defined in swComponentSuppressionState_e |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Use this method to determine if the component is suppressed, lightweight,
or fully resolved. Knowing the suppression state of the component is critical
because lightweight and suppressed components contain only a small subset
of data compared with a fully resolved component. For more information,
see Working With Lightweight Components.

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\Component\Component__GetSuppression.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
