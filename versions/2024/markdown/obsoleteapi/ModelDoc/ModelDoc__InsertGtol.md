---
title: "ModelDoc::InsertGtol"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertGtol.htm"
---

# ModelDoc::InsertGtol

This
method is obsolete and has been superseded by[ModelDoc2::InsertGtol](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertGtol.htm).

Description

This method creates a new geometric tolerance symbol in this document.

Syntax (OLE Automation)

gtol = ModelDoc.InsertGtol ( )

(Table)=========================================================

| Return: | (LPDISPATCH) gtol | Dispatch pointer to the new Gtol object |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IInsertGtol ( >ol )

(Table)=========================================================

| Output: | (LPGTOL) gtol | Pointer to the new Gtol object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The leader attachment points for the Gtol that
is created come from the selections made before calling this method. The
initial location of the symbol will also be near the selection location.
If there are no selections, the Gtol will not have a leader, be free standing,
and initially be at the origin of the model or drawing.

This method creates an empty symbol. To fill in
the text and symbols of this Gtol, you should use the pointer that is
returned by this method to access the various get and set methods of the
Gtol interface, such as Gtol::SetFrameSymbols2 and Gtol::SetFrameValues.
Use the Gtol::GetAnnotation method to retrieve the Annotation object,
which has other useful methods, such as Annotation::SetLeader2 and Annotation::SetPosition.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__InsertGtol.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
