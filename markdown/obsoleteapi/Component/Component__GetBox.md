---
title: "Component::GetBox"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetBox.htm"
---

# Component::GetBox

This
method is obsolete and has been superseded by[Component2::GetBox](sldworksAPI.chm::/Component2/Component2__GetBox.htm).

Description

This method gets the bounding box for this component object.

Syntax (OLE Automation)

retval
= Component.GetBox ( includeRefPlanes, includeSketches)

(Table)=========================================================

| Input: | (BOOL)
includeRefPlanes | TRUE
if you want the bounding box returned to include reference planes, FALSE
if not |
| --- | --- | --- |
| Input: | (BOOL)
includeSketches | TRUE
if you want the bounding box returned to include sketches, FALSE if not |
| Return: | (VARIANT)
retval | VARIANT
containing the two diagonal points that bound the component; the format
of the VARIANT is a SafeArray of 6 doubles |

Syntax (COM)

status
= Component->IGetBox ( includeRefPlanes, includeSketches, retval )

(Table)=========================================================

| Input: | (VARIANT_BOOL)includeRefPlanes | TRUE
if you want the bounding box returned to include reference planes, FALSE
if not |
| --- | --- | --- |
| Input: | (VARIANT_BOOL)includeSketches | TRUE
if you want the bounding box returned to include sketches, FALSE if not |
| Output: | (double*)
retval | Two
diagonal points that bound the component in the form of a pointer to an
array of 6 doubles |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

The X, Y, Z points that this method returns are the lower- and upper-diagonal
corners that bound the component with the box sides parallel to the X,
Y, and Z axes. These box dimensions enclose the component and are typically,
but not always, close to the minimum possible size.

The return value is an array of doubles as follows:

[XCorner1, YCorner1, ZCorner1, XCorner2,
YCorner2, ZCorner2]

It is possible for this method to return S_FALSE for COM applications
or a NULL VARIANT for Dispatch applications. This occurs if your application
calls Component::GetBox with a component that represents a subassembly
and that subassembly is not loaded in SolidWorks. After the subassembly
is loaded, the correct bounds are returned and Component::IGetBox returns
S_OK.

The user interface behavior is the same. When the user selects a subassembly
that has not been loaded, there is no selection box around the subassembly.
However, after the subassembly loads, there is a selection box.

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
<param name="Items" value="Component_Object$$**$$ZGetInfoBox$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\Component\Component__GetBox.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
