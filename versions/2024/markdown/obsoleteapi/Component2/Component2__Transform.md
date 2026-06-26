---
title: "Component2::Transform"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component2/Component2__Transform.htm"
---

# Component2::Transform

This property is obsolete and has been superseded
by[Component2::Transform2](sldworksAPI.chm::/Component2/Component2__Transform2.htm).

Description

This property gets or sets the component transform.

Syntax (OLE Automation)

form
= Component2.Transform ( ) (VB Get property)

Component2.Transform
= form (VB Set property)

form
= Component2.GetTransform ( ) (C++ Get property)

void
Component2.SetTransform ( form ) (C++ Set property)

(Table)=========================================================

| Property: | (LPMATHTRANSFORM)
form | Component
transform |
| --- | --- | --- |

Syntax (COM)

status = Component2->get_Transform ( &form
)

status = Component2->put_Transform ( form )

(Table)=========================================================

| Property: | (LPMATHTRANSFORM) form | Component transform |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

You must specify the transform in relation to the root component. See
Configuration::GetRootComponent.

This property does not support setting the transform of a component
within a subassembly. To do this, open the subassembly document and get
the desired component in the context of the subassembly document.

You can call ModelDoc2::Rebuild with the swUpdateMates argument to rebuild
the model after transforming a component. This is much faster than rebuilding
all of the geometry for the model using[Assembly_Doc::EditRebuild](../AssemblyDoc/AssemblyDoc__EditRebuild.htm).

This property lets you violate existing mate relationships. If you place
a component at an invalid location based on the mate definitions, then
ModelDoc2::Rebuild recalculates existing mate relationships and moves
your components to the closest valid location.

After you change a component's transform, you can call AssemblyDoc::UpdateBox
to avoid clipping in shaded display mode.

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Component2_Object$$**$$MathTransform_Object$$**$$Component2::SetTransformAndSolve$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Component2\Component2__Transform.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan
