---
title: "Body2::SetXform"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body2/Body2__ISetXform.htm"
---

# Body2::SetXform

This method is obsolete and has been superseded
byBody2::ApplyTranform .

Description

This method is intended for use with the Body2::GetIntersectionEdges
method.

Syntax (OLE Automation)

retval = Body2.SetXform ( xformIn )

(Table)=========================================================

| Input: | (VARIANT) xformIn | SafeArray of 16 doubles representing the transform |
| --- | --- | --- |
| Return: | (VARIANT_BOOL) retval | TRUE if the Xform is set successfully, FALSE if not |

Syntax
(COM)

status = Body2->ISetXform ( xformIn,
&retval )

(Table)=========================================================

| Input: | (double*) xformIn | Pointer to an array of 16 doubles representing a transform |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the Xform is set successfully, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If there are two bodies in an assembly, then Body2::GetIntersectionEdges
edges generates a list of the intersection edges between the two bodies.
To do this, the second body must be transformed in its coordinate space
so that it is positioned the same with respect to the first body as it
is in assembly space.

To align the two bodies before call Body2::GetIntersectionEdges, calculate
the transformation from the first body to the second body and set this
as the transform for the second body using Body2::SetXform.

The xformIn argument contains a 16 element array defining the transform.
The first nine are elements of 3x3 matrix, the next three define translation
and the next one is scaling. The last three elements are unused. Specify
the transform in relation to the model.

Body2::SetXform is intended for use with temporary body objects. If
you call this method on the actual part or component body object, you
might corrupt your file. You can make a copy of a Body object using Body2::Copy.

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\body2\Body2__ISetXform.htm" >
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
<param name="Items" value="Body2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\body2\Body2__ISetXform.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
