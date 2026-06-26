---
title: "Component2::SetXformAndSolve"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component2/Component2__SetXformAndSolve.htm"
---

# Component2::SetXformAndSolve

This method is obsolete and has been superseded
by[Component2::SetTransformAndSolve](Component2__SetTransformAndSolve.htm).

Description

This method sets the component transform.

Syntax (OLE Automation)

retval
= Component2.SetXformAndSolve ( xformIn)

(Table)=========================================================

| Input: | (VARIANT)
xformIn | SafeArray
of 16 doubles; first 9 are elements of a standard 3x3 rotation matrix,
the next 3 define translation, the 13th one is scaling, and the last 3
elements are unused; the transform specified should be in relation to
the root component |
| --- | --- | --- |
| Return: | (VARIANT_BOOL)
retval | Not
used |

Syntax (COM)

status
= Component2->ISetXformAndSolve ( xformIn, retval )

(Table)=========================================================

| Input: | (double*)
xformIn | Array of 16 doubles;
first 9 are elements of a standard 3x3 rotation matrix, the next 3 define
translation, the 13th one is scaling, and the last 3 elements are unused;
the transform specified should be in relation to the root component |
| --- | --- | --- |
| Output: | (VARIANT_BOOL)
retval | Not
used |
| Return: | (HRESULT)status | S_OK
if successful |

Remarks

You must specify the transform in relation to the root component. See
Configuration::GetRootComponent.

This method does not support setting the transform of a component within
a subassembly. To do this, you must open the subassembly document and
get the desired component in the context of the subassembly document.
After the component is transformed, the constraints are solved.

Transforming an object with this call can cause SolidWorks to transform
several other mated or constrained objects.

After you have changed a component's transform, you can call AssemblyDoc::UpdateBox
to avoid clipping in shaded display mode.

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
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Component2\Component2__SetXformAndSolve.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Component2\Component2__SetXformAndSolve.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
