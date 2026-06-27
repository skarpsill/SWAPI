---
title: "Component::EnumSectionedBodies"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__EnumSectionedBodies.htm"
---

# Component::EnumSectionedBodies

This
method is obsolete and has been superseded by[Component2::EnumSectionedBodies](sldworksAPI.chm::/Component2/Component2__EnumSectionedBodies.htm).

Description

This method gets the sectioned bodies seen in the specified view and
returns them in an enumerated list. To determine if the desired model
view is currently displaying a sectioned view, see ModelView::GetDisplayState.

Syntax (OLE Automation)

Not
available.

Syntax (COM)

status
= Component->EnumSectionedBodies ( viewIn, &retval )

(Table)=========================================================

| Input: | (LPMODELVIEW)
viewIn | Pointer
to the model view object displaying the sectioned view |
| --- | --- | --- |
| Output: | (LPENUMBODIES)
retval | Pointer
to the enumerated list of bodies |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

If you need the full body representation, use Component::GetBody or[PartDoc::Body](../PartDoc/PartDoc__Body.htm), which ignores
the sectioning operation.

For Dispatch implementations, use[Component::GetSectionedBodies](Component__GetSectionedBodies.htm).

If a component is suppressed or lightweight, this method might return
NULL because the component was not loaded into memory by SolidWorks. For
more information on lightweight components, see Working With Lightweight
Components.

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
<param name="_CURRENTFILEPATH" value="D:\sw2003\Component\Component__EnumSectionedBodies.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
