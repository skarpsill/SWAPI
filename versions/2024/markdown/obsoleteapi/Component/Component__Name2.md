---
title: "Component::Name2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__Name2.htm"
---

# Component::Name2

This
property is obsolete and has been superseded by[Component2::Name2](sldworksAPI.chm::/Component2/Component2__Name2.htm).

Description

This property gets and sets the component name.

Syntax (OLE Automation)

newName = Component.Name2 ( ) (VB Get property)

Component.Name2 = newName (VB
Set property)

newName = Component.GetName2 ( ) (C++
Get property)

void Component.SetName2(newName
) (C++ Set property)

(Table)=========================================================

| Property: | (BSTR) newName | Name of this component instance |
| --- | --- | --- |

Syntax (COM)

status = Component->get_Name2 ( &newName )

status = Component->put_Name2 ( newName )

(Table)=========================================================

| Property: | (BSTR) newName | Name of this component instance |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This name of the component appears in the FeatureManager
design tree and is not necessarily the same as the name of the underlying
part or assembly file.

This property returns a name that includes an instance
number. For example:

Part1-1

indicates that this is the first instance of the Part1 Component2. If
you are examining a component that is within a subassembly, then this
property returns a name that includes the full hierarchical path of component
names. For example:

subAssem1-2/Part1-1

indicates that this component (Part1) is the first instance within the
subAssem1 Component2. It also shows that this is the second instance of
subAssem1.

If you are setting the name of a component, remember
that some special characters are reserved by SolidWorks. Before executing
a name change, this property checks the swExtRefUpdateCompNames setting.
If it is TRUE, the name change fails; if it is FALSE, the name change
continues. You can use SldWorks::GetUserPreferenceToggle to change the
swExtRefUpdateCompNames setting.

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\Component\Component__Name2.htm" >
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
<param name="Items" value="Component_Object$$**$$ZGetInfoComponent$$**$$ZModifyComponent$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\Component\Component__Name2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
