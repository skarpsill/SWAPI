---
title: "Component::Solving"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__Solving.htm"
---

# Component::Solving

This
property is obsolete and has been superseded by[Component2::Solving](sldworksAPI.chm::/Component2/Component2__Solving.htm).

Description

This property provides access to the solving
option of this component.

Syntax (OLE Automation)

solving = Component.Solving (VB Get property)

solving = Component.GetSolving ( ) (C++ Get
property)

(Table)=========================================================

| Property: | (long) solving | Solving option of this component instance as
defined in swComponentSolvingOption_e |
| --- | --- | --- |

Syntax (COM)

status = Component->get_Solving( &solving
)

(Table)=========================================================

| Property: | (long) solving | Solving option of this component instance as
defined in swComponentSolvingOption_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can use AssemblyDoc::CompConfigProperties3
to set the solving state of a component.

This property applies only to subassembly components,
not part components. If you try to get the solving option of a part component,
SolidWorks returns -1.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Component\Component__Solving.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Component_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Component\Component__Solving.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
