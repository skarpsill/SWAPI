---
title: "Component::EnumRelatedBodies"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__EnumRelatedBodies.htm"
---

# Component::EnumRelatedBodies

This
method is obsolete and has been superseded by[Component2::EnumRelatedBodies](sldworksAPI.chm::/Component2/Component2__EnumRelatedBodies.htm).

Description

This method creates an enumerated list of bodies. The list contains
only those bodies associated with reference surfaces. The list of bodies
is related to the model, but it does not include the part body itself.

Syntax (OLE Automation)

Not
available.

Syntax (COM)

status
= Component->EnumRelatedBodies ( &retval )

(Table)=========================================================

| Output: | (LPENUMBODIES*)
retval | Pointer
to the enumerated list of bodies |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

A reference surface feature might consist of one or more surfaces sewn
together. SolidWorks represents each reference surface feature with two
body objects; one to represent the front faces and one to represent the
back faces. Each body object has 1 or more faces depending on whether
the reference surface feature is a set of sewn surfaces or a single underlying
surface. The corresponding faces for each body pair have opposite normal
vectors.

To use the enumerated list, use EnumBodies2::Next, EnumBodies2::Skip,
EnumBodies2::Reset, and EnumBodies2::Clone.

If a component is suppressed or lightweight, this method might return
NULL because the component has not been loaded into memory by SolidWorks.
For more information on lightweight components, refer to Working With
Lightweight Components.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\Component\Component__EnumRelatedBodies.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Enumerate_Bodies_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\Component\Component__EnumRelatedBodies.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
