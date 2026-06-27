---
title: "ModelView::Scale"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelView/ModelView__Scale.htm"
---

# ModelView::Scale

This
property is obsolete and has been superseded by[ModelView::Scale2](sldworksAPI.chm::/ModelView/ModelView__Scale2.htm).

Description

This property gets and sets the scale factor for the view.

Syntax (OLE Automation)

scale = ModelView.Scale (VB Get
property)

ModelView.Scale = scale (VB Set
property)

scale = ModelView.GetScale ( ) (C++
Get property)

ModelView.SetScale ( scale ) (C++
Set property)

(Table)=========================================================

| Property: | (double) scale | View scale |
| --- | --- | --- |

Syntax (Com)

status = ModelView->get_Scale (
&scale )

status = ModelView->put_Scale( scale
)

(Table)=========================================================

| Property: | (double) scale | View scale |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Using data returned from this property along with information from ModelView::Orientation2
and ModelView::Tranlation2 should be multiplied in this order: orientation
-> scale -> transform.

To map your coordinates from 3D space to the screen, use ModelView::Xform.

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
<param name="Items" value="ModelView_Object$$**$$ZGetInfoModelView$$**$$ZModifyModelView$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelView\ModelView__Scale.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
