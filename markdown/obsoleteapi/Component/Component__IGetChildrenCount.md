---
title: "Component::IGetChildrenCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__IGetChildrenCount.htm"
---

# Component::IGetChildrenCount

This
method is obsolete and has been superseded by[Component2::IGetChildrenCount](sldworksAPI.chm::/Component2/Component2__IGetChildrenCount.htm).

Description

This method gets the number of direct child components for this component
object.

Syntax (OLE Automation)

Not
available.

Syntax (COM)

status
= Component->IGetChildrenCount ( &retval )

(Table)=========================================================

| Output: | (int*)
retval | Number
of children |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

The value returned is a single-level count. This method does not count
subassemblies.

To get the number of children in a Dispatch application, check the size
of the VARIANT returned by Component::GetChildren.

For more information, see SafeArray Return Values.

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
<param name="_CURRENTFILEPATH" value="D:\sw2003\Component\Component__IGetChildrenCount.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
