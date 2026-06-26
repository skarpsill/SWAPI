---
title: "Component2::Name"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component2/Component2__Name.htm"
---

# Component2::Name

This
property is obsolete and has been superseded by[Component2::Name2](sldworksAPI.chm::/Component2/Component2__Name2.htm).

Description

This property gets the component name that appears in the FeatureManager
design tree, and is not necessarily the same as the name of the underlying
part or assembly file.

Syntax (OLE Automation)

Name
= Component2.Name (VB Get property)

Name
= Component2.GetName ( ) (C++ Get property)

(Table)=========================================================

| Property: | (BSTR)
Name | Name
of this component instance |
| --- | --- | --- |

Syntax (COM)

status
= Component2->get_Name( &Name )

(Table)=========================================================

| Property: | (BSTR)
Name | Name
of this component instance |
| --- | --- | --- |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

This property returns a name that includes an instance number. For example:

Part1-1

indicates that this is the first instance of the Part1 Component2. If
you are examining a component that is within a subassembly, then this
property returns a name that includes the full hierarchical path of component
names. For example:

subAssem1-2/Part1-1

indicates that this component (Part1) is the first instance within the
subAssem1 Component2. It also shows that the second instance of subAssem1
is referenced.

Additionally, theUser Option,External Referencesetting allows
or prohibits changes to this name. This setting affects only interactive
user operations.

If you are setting the name of a component, remember that some special
characters are reserved by SolidWorks.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\Component2\Component2__Name.htm" >
<param name="_ID" value="RelatedTopic2" >
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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Component2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\Component2\Component2__Name.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
