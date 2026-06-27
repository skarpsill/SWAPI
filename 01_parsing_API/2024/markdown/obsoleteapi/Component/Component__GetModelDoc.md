---
title: "Component::GetModelDoc"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetModelDoc.htm"
---

# Component::GetModelDoc

This method is obsolete and has been superseded by[Component2::GetModelDoc](sldworksAPI.chm::/Component2/Component2__IGetModelDoc.htm).

Description

This method gets the ModelDoc object for this component.

Syntax (OLE Automation)

retval
= Component.GetModelDoc ()

(Table)=========================================================

| Return: | (LPDISPATCH)
retval | Pointer
to Dispatch object, the model for this component |
| --- | --- | --- |

Syntax (COM)

status
= Component->IGetModelDoc ( &retval )

(Table)=========================================================

| Output: | (LPMODELDOC)
retval | Pointer
to the model for this component |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

If a component is suppressed or lightweight, this method might return
NULL because the component has not been loaded into memory by SolidWorks.
For more information on lightweight components, see Working With Lightweight
Components.

When you use the ModelDoc object of a component, you do not have access
to whatever uniqueness might exist for this instance of the assembly component.
This happens because the ModelDoc object goes back to the local version
of the part file. By comparison, the Component object gathers its information
at the assembly level. This allows Component objects to recognize any
assembly-level changes made to a component instance (for example, assembly-level
features and material changes).

In addition, the ModelDoc returned from this method is representative
of the last saved state. If the component part is open, then the ModelDoc
represents the state of the opened document. For example, if the component
part is not open and it was last saved in the default configuration, then
Component::GetModelDoc returns a ModelDoc pointer representing that state.
To get access to other configuration information, such as features and
configuration properties, use[ShowConfiguration](../ModelDoc/ModelDoc__ShowConfiguration2.htm)to activate the part and display that configuration.

If this component is the root component, then this method returns a
NULL pointer. For more information, see Configuration::GetRootComponent.

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
<param name="Items" value="Component_Object$$**$$ZGetInfoComponent$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Component\Component__GetModelDoc.htm" >
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
<param name="Items" value="Part_Extents_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Component\Component__GetModelDoc.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
