---
title: "Component::FindAttribute"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__FindAttribute.htm"
---

# Component::FindAttribute

This
method is obsolete and has been superseded by[Component2::FindAttribute](sldworksAPI.chm::/Component2/Component2__FindAttribute.htm).

Description

This method finds an attribute on a component.

Syntax (OLE Automation)

retval = Component.FindAttribute ( attributeDef,
whichOne )

(Table)=========================================================

| Input: | (LPDISPATCH) attributeDef | Pointer to an attribute definition that you are
looking for on this component |
| --- | --- | --- |
| Input: | (long) whichOne | Index number of the attribute that you want to
return (there can be several attributes on a component) |
| Return: | (LPDISPATCH) retval | Pointer to the attribute object for which you
searched the component |

Syntax (COM)

status = Component->IFindAttribute ( attributeDef,
whichOne, &retval)

(Table)=========================================================

| Input: | (LPATTRIBUTEDEF) attributeDef | Pointer to an attribute definition that you are
looking for on this component |
| --- | --- | --- |
| Input: | (long) whichOne | Index number of the attribute that you want to
return (there can be several attributes on a component) |
| Output: | (LPATTRIBUTE) retval | Pointer to the attribute object for which you
searched the component |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\Component\Component__FindAttribute.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\Component\Component__FindAttribute.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
