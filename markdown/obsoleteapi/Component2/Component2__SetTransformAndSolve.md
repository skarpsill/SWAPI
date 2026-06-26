---
title: "Component2::SetTransformAndSolve"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component2/Component2__SetTransformAndSolve.htm"
---

# Component2::SetTransformAndSolve

This method is obsolete and has been superseded
by[Component2::SetTransformAndSolve2](sldworksAPI.chm::/Component2/Component2__SetTransformAndSolve2.htm).

Description

This method sets the transform and solves for
the mates.

Syntax (OLE Automation)

retval = Component2.SetTransformAndSolve ( xformIn,
&retval )

(Table)=========================================================

| Input: | (LPMATHTRANSFORM) xformIn | Transform to set and solve |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the transform was set and solved, FALSE if not |

Syntax (COM)

status = Component2->SetTransformAndSolve ( xformIn,
&retval )

Parameters Table Start

(Table)=========================================================

| Input: | (LPMATHTRANSFORM) xformIn | Transform to set and solve |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the transform was set and solved, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The transform must be in relation to the root component. See Configuration::GetRootComponent.

This method does not currently support setting the transform of a component
within a subassembly. To do this, you must open the subassembly document
and get the desired component in the context of the subassembly document.
After the component is transformed, the constraints are solved.

Transforming an object with this call can cause SolidWorks to transform
several other mated or constrained objects.

After you have changed a component's transform,
you can call AssemblyDoc::UpdateBox to avoid clipping in shaded display
mode.

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
<param name="Items" value="Component2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\Component2\Component2__SetTransformAndSolve.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan
