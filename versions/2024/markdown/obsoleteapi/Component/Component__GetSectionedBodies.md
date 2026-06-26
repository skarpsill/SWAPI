---
title: "Component::GetSectionedBodies"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetSectionedBodies.htm"
---

# Component::GetSectionedBodies

This
method is obsolete and has been superseded by[Component2::GetSectionedBodies](sldworksAPI.chm::/Component2/Component2__GetSectionedBodies.htm).

Description

This method gets the sectioned bodies seen in the specified view and
returns them as a SafeArray of Dispatch pointers to each individual Body
object.

Syntax (OLE Automation)

retval
= Component.GetSectionedBodies ( viewIn)

(Table)=========================================================

| Input: | (LPDISPATCH)
viewIn | Dispatch
pointer to the model view object displaying the sectioned view |
| --- | --- | --- |
| Return: | (VARIANT)
retval | VARIANT
of type SafeArray of Dispatch pointers to the sectioned bodies in the
specified view |

Syntax (COM)

status
= Component->GetSectionedBodies ( viewIn, &retval )

(Table)=========================================================

| Input: | (LPDISPATCH)
viewIn | Dispatch
pointer to the model view object displaying the sectioned view |
| --- | --- | --- |
| Output: | (VARIANT)
retval | VARIANT
of type SafeArray of Dispatch pointers to the sectioned bodies in the
specified view |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

To determine if the desired model view
is currently displaying a sectioned view, use ModelView::GetDisplayState.

If you need the full body representation,
use Component::GetBody or PartDoc::Body, which ignore the sectioning operation.

For COM implementations, refer to Component::EnumSectionedBodies.

If a component is suppressed or lightweight, this method might return
NULL because the component is loaded into memory. For more information
on lightweight components, refer to Working With Lightweight Components.

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
<param name="Items" value="Component_Object$$**$$ZGetBody$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Component\Component__GetSectionedBodies.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
