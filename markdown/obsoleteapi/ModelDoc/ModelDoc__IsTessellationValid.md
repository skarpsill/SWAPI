---
title: "ModelDoc::IsTessellationValid"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__IsTessellationValid.htm"
---

# ModelDoc::IsTessellationValid

This
method is obsolete and has been superseded by[ModelDoc2::IsTessellationValid](sldworksAPI.chm::/ModelDoc2/ModelDoc2__IsTessellationValid.htm).

Description

This method is designed to work in coordination
with Face2::IGetFacetData to determine if the current set of facets is
valid.

Syntax (OLE Automation)

retval = ModelDoc.IsTessellationValid ( )

(Table)=========================================================

| Return: | (BOOL) retval | TRUE if the facet data is valid, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IsTessellationValid ( &retval
)

(Table)=========================================================

| Return: | (VARIANT_BOOL) retval | TRUE if the facet data is valid, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is used to capture operations that
invalidate the current set of facets, yet does not send a RegenNotify
event. For example, if the user changes the rendering tolerance, the RegenNotify
event would not be sent, yet the current set of facets would be invalid.
However, this action would trigger a SolidWorks RepaintNotify from where
you could call this mehtod before attempting to use your current set of
facet data.

If FALSE is returned from IsTessellationValid,
then valid facet information would not be available until SolidWorks completes
a repaint operation (RepaintPostNotify). In other words, SolidWorks does
not have any valid facet information at this time, and any facet data
obtained in earlier calls is invalid. Not until the repaint operation
is complete (RepaintPostNotify) can you call IGetFacetData again. As a
result, the user would see a flash of SolidWorks tessellation in the graphics
window before your application would be able to obtain the facet data
again and redraw it to the SolidWorks display.

See Face2::IGetFacetData for more information.

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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZTessellation$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__IsTessellationValid.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
