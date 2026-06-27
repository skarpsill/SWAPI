---
title: "Component::GetBody"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetBody.htm"
---

# Component::GetBody

This method is obsolete and has been superseded by[Component2::GetBody](sldworksAPI.chm::/Component2/Component2__GetBody.htm).

Description

This method gets the body that belongs to this component.

Syntax (OLE Automation)

retval
= Component.GetBody ()

(Table)=========================================================

| Return: | (LPDISPATCH)
retval | Pointer
to Dispatch object, the body |
| --- | --- | --- |

Syntax (COM)

status
= Component->IGetBody ( &retval )

(Table)=========================================================

| Output: | (LPBODY)
retval | Pointer
to the body |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK
if successful (see below) |

Remarks

This method only returns a valid body object
for fully resolved components that reference a PartDoc. For the root component,
lightweight components or components that reference an AssemblyDoc, this
method returns NULL.

For COM applications, this method returns
the status code ITF_E_COMPONENTNOTRESOLVED, defined in swhres.h.

This method is different
from the PartDoc::Body method in that it recognizes assembly-level features
and returns that information based on the component instance. The PartDoc::Body
method never recognizes assembly-level features because the feature information
is kept with the assembly, not propagated down to the part file.

For example, if PartABC is added to an assembly
twice, then changes to that PartDoc object affect both instances of the
assembly component. Likewise, querying information from that PartDoc object
does not recognize changes in the assembly that might have altered only
one of the components (for example, an assembly-level feature was added
to one of the components). However, the Component object recognizes the
two instances of PartABC as two distinct Component objects, and returns
information from the assembly level. For example, one assembly configuration
might have an assembly-level feature that cuts a hole through each of
the components in the assembly. When you use GetBody on each of the assembly
components, it returns the body of each component with the hole feature
that was applied in this particular configuration. If you switch to the
configuration without the assembly-level hole and re-traverse the component
objects, then GetBody returns the body object without the hole feature,
which was applied in the other configuration.

For more information on lightweight components
see Component::GetSuppression, Component::SetSuppression and AssemblyDoc::ResolveAllLightWeightComponents.

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
<param name="Items" value="Component_Object$$**$$ZGetBody$$**$$Assembly_Analysis$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\Component\Component__GetBody.htm" >
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
<param name="Items" value="Enumerate_Bodies_Example$$**$$Get_Component_Face_By_Name_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\Component\Component__GetBody.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
