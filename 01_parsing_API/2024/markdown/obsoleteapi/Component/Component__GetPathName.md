---
title: "Component::GetPathName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetPathName.htm"
---

# Component::GetPathName

This
method is obsolete and has been superseded by[Component2::GetPathName](sldworksAPI.chm::/Component2/Component2__GetPathName.htm).

Description

This method gets the full path name of this component.

Syntax (OLE Automation)

retval
= Component.GetPathName ( )

(Table)=========================================================

| Return: | (BSTR)retval | Full
path name for this component, including the file name |
| --- | --- | --- |

Syntax (COM)

status
= Component->GetPathName ( &retval )

(Table)=========================================================

| Output: | (BSTR)retval | Full
path name for this component, including the file name |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK
if Successful |

Remarks

It is possible that the underlying document for this component is not
loaded into memory. This can happen if the component is lightweight or
suppressed. When this happens,[Component::GetModelDoc](Component__GetModelDoc.htm)returns NULL, and this method returns the as-saved file and path name
for the component. Component::GetPathName does not apply search criteria
or look in the current working directory for the component file reference
if the component is lightweight or suppressed.

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
<param name="Items" value="Component_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Component\Component__GetPathName.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
